import math

def simulate(
    # S1 & S2
    hitl_variant="B",
    jobs_attempted=1000,
    containment_rate=0.82,
    # S3 LLM
    price_input=1.0, # $ / 1M
    price_output=5.0, # $ / 1M
    price_cache_write=1.25, # $ / 1M
    price_cache_read=0.10, # $ / 1M
    turns=8,
    tokens_cache=3000,
    tokens_fresh=800,
    tokens_out=250,
    batch_api=0,
    # S4 Speech
    price_stt=0.0077, # $ / min
    audio_mins=2.0, # min / job
    price_tts=50.0, # $ / 1M chars
    tts_chars=1200, # chars / job
    # S5 Infra
    infra_base=0.010, # $ / job
    telephony_per_min=0.012, # $ / min
    # S6 Retry
    retry_rate=0.08,
    # S7 HITL
    labor_rate=9.0, # $ / hr
    qa_pct=0.05,
    qa_mins=2.0,
    esc_mins=6.0,
    # S8 Overhead
    overhead=0.0,
    # Exchange rate
    fx_rate=26000.0,
    # Tab 2 Pricing
    markup_floor=3.0,
    val_saved_per_month=6000.0, # hospital saves $6,000/mo in nurse triage & readmission penalties
    jobs_per_client=500.0, # 1 hospital client has 500 discharge patients/mo
    salary_replaced=1200.0, # 2 nurse shifts cost $1,200/mo
    proposed_price=1.75 # $ / episode (hoặc $1.99 hay $1.50)
):
    jobs_completed = jobs_attempted * containment_rate
    jobs_escalated = jobs_attempted - jobs_completed

    # LLM calculation
    cache_write_job = tokens_cache * price_cache_write / 1e6
    cache_read_job = (turns - 1) * tokens_cache * price_cache_read / 1e6
    fresh_input_job = turns * tokens_fresh * price_input / 1e6
    output_job = turns * tokens_out * price_output / 1e6

    llm_with_cache = cache_write_job + cache_read_job + fresh_input_job + output_job
    llm_no_cache = turns * (tokens_cache + tokens_fresh) * price_input / 1e6 + output_job
    cache_savings = 1 - (llm_with_cache / llm_no_cache) if llm_no_cache > 0 else 0
    llm_job = llm_with_cache * (1 - batch_api * 0.5)

    # Speech calculation
    speech_job = price_stt * audio_mins + price_tts * tts_chars / 1e6

    # Infra calculation
    infra_job = infra_base + telephony_per_min * audio_mins

    # Retry calculation
    retry_job = (llm_job + speech_job) * retry_rate

    # Total variable cost per attempted job
    v = llm_job + speech_job + infra_job + retry_job
    var_cost_month = jobs_attempted * v

    # HITL
    qa_cost_month = jobs_attempted * qa_pct * (qa_mins / 60) * labor_rate
    q = qa_pct * (qa_mins / 60) * labor_rate # per attempted job
    esc_cost_month = jobs_escalated * (esc_mins / 60) * labor_rate if hitl_variant == "B" else 0
    e = (esc_mins / 60) * labor_rate if hitl_variant == "B" else 0 # per escalated job
    total_hitl_month = qa_cost_month + esc_cost_month

    total_cost_month = var_cost_month + total_hitl_month + overhead
    cost_per_job = (var_cost_month + total_hitl_month) / jobs_completed

    # Tab 2 Pricing
    price_floor = cost_per_job * markup_floor
    gross_margin = (proposed_price - cost_per_job) / proposed_price if proposed_price > 0 else 0
    markup_multiple = proposed_price / cost_per_job if cost_per_job > 0 else 0

    # Breakeven containment: R >= (v + q + e) / (P * (1 - GM_target) + e)
    gm_target = 0.60
    denom = proposed_price * (1 - gm_target) + e
    breakeven_containment = (v + q + e) / denom if denom > 0 else 0

    print("=== COST/JOB SUMMARY ===")
    print(f"Jobs Attempted: {jobs_attempted}, Completed: {jobs_completed}, Escalated: {jobs_escalated}")
    print(f"LLM/job: ${llm_job:.4f} (with cache: -{cache_savings*100:.1f}%)")
    print(f"Speech/job: ${speech_job:.4f}")
    print(f"Infra/job: ${infra_job:.4f}")
    print(f"Retry/job: ${retry_job:.4f}")
    print(f"Variable cost v/attempt: ${v:.4f}")
    print(f"HITL QA/mo: ${qa_cost_month:.2f}, Esc/mo: ${esc_cost_month:.2f}, Total HITL: ${total_hitl_month:.2f}")
    print(f"Total cost/mo: ${total_cost_month:.2f}")
    print(f"--> COST/JOB (divided by completed): ${cost_per_job:.4f} (~ {cost_per_job*fx_rate:,.0f} VND)")
    print(f"\n=== PRICING SANITY CHECK ===")
    print(f"Floor price (3x): ${price_floor:.4f}")
    print(f"Proposed price: ${proposed_price:.2f}")
    print(f"Gross Margin: {gross_margin*100:.2f}%")
    print(f"Markup multiple: {markup_multiple:.2f}x")
    print(f"Breakeven containment for GM>=60%: {breakeven_containment*100:.2f}% (Current: {containment_rate*100:.1f}%)")

    # Sensitivity table
    print("\n--- SENSITIVITY TABLE ---")
    for r in [0.5, 0.6, 0.7, 0.8, 0.82, 0.9, 0.95]:
        cpj = (v + q + e * (1 - r)) / r
        gm = (proposed_price - cpj) / proposed_price
        eval_str = "An toan" if gm >= 0.6 else ("Canh bao" if gm >= 0.5 else "Nguy hiem")
        print(f"Containment: {r*100:4.1f}% | Cost/Job: ${cpj:.4f} | Gross Margin: {gm*100:5.1f}% | {eval_str}")

simulate()
