# Track 1 — Day 22: AI Product GTM & Monetization Model

- **Họ và tên:** Mai Tiến Huy
- **Mã học viên:** 2A202602914
- **Lớp / Nhóm:** AI-IN-ACTION Track 1 · Nhóm DBH
- **Tên dự án:** CareLoop AI — AI Agent Hỗ trợ Chăm sóc Sau Xuất viện & Phòng Tái Nhập viện
- **Ngày thực hiện:** 08/10/2026

---

## 1. Danh mục Hồ sơ Nộp bài (Deliverables)

| Tệp tin | Vai trò & Mô tả | Liên kết |
|---|---|---|
| **`MaiTienHuy_Day22_model.xlsx`** | Mô hình tài chính hoàn chỉnh 5 tab tính toán + 2 tab tham chiếu (Cost/Job, Pricing, Value Metric, Channel Fit, 90-Day Plan). | [Bảng tính Excel](MaiTienHuy_Day22_model.xlsx) |
| **`MaiTienHuy_Day22_onepager.pdf`** | Bản Monetization One-Pager định dạng PDF chuẩn 3 khối, đối soát 100% dữ liệu với Excel. | [Bản PDF One-Pager](MaiTienHuy_Day22_onepager.pdf) |
| **`MaiTienHuy_Day22_onepager.docx`** | Bản soạn thảo Word gốc của One-Pager. | [Bản Word One-Pager](MaiTienHuy_Day22_onepager.docx) |
| **`ai-support-log.md`** | Báo cáo chi tiết quá trình chạy 2 prompt phản biện độc lập (§4.7.1 & §4.7.3) và quyết định Accept/Reject. | [Prompt Critique Log](ai-support-log.md) |

---

## 2. Đối chiếu 10 Tiêu chí Check-list Bắt buộc (10/10 PASS)

| # | Tiêu chí Check-list | Trạng thái | Bằng chứng cụ thể trong bài làm |
|---|---|:---:|---|
| **1** | **Tab 1 — đủ 5 thành phần chi phí, không ô nào trống vô lý** | **✅ PASS** | Đủ 5 thành phần: LLM ($0.0222 có cache giảm 44.9%), Speech ($0.0754 gồm STT Deepgram 2 phút + TTS ElevenLabs 1.200 ký tự), Infra ($0.0340 gồm DB/HIPAA log + Telephony), Retry ($0.0078 tỷ lệ 8%), HITL ($177.00/tháng gồm QA 5% và Escalation 180 ca Biến thể B). |
| **2** | **Tab 1 — mẫu số là JOB HOÀN THÀNH, không phải job thử** | **✅ PASS** | Ô `1_Cost_Job!B11` = 820 jobs hoàn thành (= 1.000 thử $\times$ 82% containment). Công thức Cost/Job `B66 = (B62+B63)/B11` = **$0.3859 / job** (nếu chia 1.000 job thử thì chỉ ra $0.3165 — sai lệch 21.9%). |
| **3** | **Tab 2 — Giá bán ≥ 3 × Cost/Job, Gross Margin ≥ 60%** | **✅ PASS** | Giá sàn (3×) = $1.1578; Giá bán đề xuất = **$1.7500** (bội số **4.53×**, `B22` = *"OK — ĐẠT"*); Gross Margin = **77.95%** (`B23` = *"OK — AN TOÀN"*, nằm trong dải 60%–85%, `B24` = *"OK"* không bị cờ đỏ quên chi phí). |
| **4** | **Tab 2 — Breakeven containment đã tính, đã so với eval** | **✅ PASS** | Breakeven containment `B33` = **65.90%**; Eval hiện tại `B34` = **82.00%** $\rightarrow$ `B35` = *"ĐẠT — mô hình có lãi lành mạnh"* (Biên an toàn vượt ngưỡng **+16.1%**). |
| **5** | **Tab 3 — Value Metric + Decision Note + 2 benchmark có link** | **✅ PASS** | Attribution = 8/10; Autonomy = 8/10. Model gợi ý Outcome, chọn **Hybrid (Usage theo Care Episode có sàn cam kết: $1.75/bệnh nhân)** kèm giải thích Market Override. Đủ 3 câu Decision Note (`B32:B34`). 2 benchmark thật: Memora Health ($4–$6/episode) và Intercom Fin ($0.99/resolution) kèm link URL. |
| **6** | **Tab 4 — Ngân sách CAC, deal/AE/ngày, 1 kênh duy nhất** | **✅ PASS** | ARPU = $700/tháng, Payback 12 tháng $\rightarrow$ Ngân sách CAC = **$6,547.80**. Deal/AE/ngày = 0.05 deal/ngày. CAC sales thực tế = $32,000 $\rightarrow$ Lệch **4.89 lần** (bất khả thi cho Sales-Led). Chốt đúng 1 kênh: **Partner-Led** (Scorecard 29/30 điểm). Tên đối tác: **VNPT Y tế (VNPT HIS)** và **FPT IS (eHospital)**, trạng thái: *"Đã trao đổi kỹ thuật về webhook"*. |
| **7** | **Tab 5 — 90-day plan có số; Evidence Pack có deadline** | **✅ PASS** | Pain Moment đủ 3 phần: Giờ (14:00–16:00 & 20:00–22:00) + Việc (Duyệt xuất viện & lo lắng ở nhà) + App (VNPT HIS & Zalo). Điểm nhúng: Webhook trên màn hình Duyệt Xuất Viện VNPT HIS. Kế hoạch 90 ngày có số khách (2 BV $\rightarrow$ 8 BV $\rightarrow$ 25 BV), KPI định lượng và người chịu trách nhiệm. Evidence Pack có nội dung cụ thể và deadline rõ ràng. |
| **8** | **Ghi ngày kiểm tra giá API ở tab 6_Benchmarks** | **✅ PASS** | Ô `6_Benchmarks!B3` đã ghi rõ: `2026-10-08 (Kiểm tra và cập nhật tại ngày làm bài)`. |
| **9** | **One-Pager — 3 khối, mọi số khớp Excel** | **✅ PASS** | Bản One-Pager (Word & PDF) trình bày đủ 3 khối: Pricing, GTM, Evidence Pack; toàn bộ các con số truy soát khớp 100% từng ô tương ứng trong Excel. |
| **10** | **Đã chạy ít nhất 2 prompt ở §4.7 và ghi lại accept/reject** | **✅ PASS** | Đã chạy 2 prompt: Cost/Job Stress Test (§4.7.1) và Channel Reality Check (§4.7.3); ghi lại đầy đủ phân tích và các quyết định Accept / Reject / Partial tại file `ai-support-log.md`. |

---

## 3. Bản đồ Số liệu Cốt lõi (Golden Metrics)

```
[ Cost/Job: $0.3859 ] ─── (3× Giá sàn: $1.1578) ─── [ Giá bán: $1.75 ] ─── [ Giá trần: $3.00 ]
         │                                                    │
   Chia cho 820 completed                              Gross Margin: 77.95%
 (v = $0.1395, HITL = $177/tháng)                    (An toàn: 60% ≤ GM ≤ 85%)
         │                                                    │
Breakeven Containment: 65.90% ◄────────────────────── Eval hiện tại: 82.00% (+16.1%)
```

```
[ Ngân sách CAC: $6,547.80 ] ◄────── Lệch 4.89 lần ──────► [ CAC Sales-Led: $32,000 ]
         │
         ▼
Lựa chọn kênh tối ưu: PARTNER-LED (VNPT HIS / FPT eHospital)
- Điểm nhúng: Nút 'Kích hoạt CareLoop' tại màn hình Duyệt Xuất Viện trên VNPT HIS.
- Chia sẻ doanh thu: 25% cho đối tác trên mỗi lượt bệnh nhân hoàn tất theo dõi.
```

---

## 4. Hướng dẫn Giám khảo / Người chấm Đánh giá Nhanh (2-minute Stranger Test)
1. **Bạn bán gì, cho ai, tính tiền theo đơn vị nào?**
   $\rightarrow$ Bán dịch vụ AI Agent theo dõi chăm sóc và sàng lọc biến chứng sau xuất viện cho các Bệnh viện tư nhân & Phòng khám đa khoa, tính tiền theo đơn vị **$1.75 / bệnh nhân hoàn tất chu kỳ 30 ngày (Completed Care Episode)**.
2. **Có lãi trên mỗi đơn vị không, con số nào chứng minh?**
   $\rightarrow$ **Có lãi rất lành mạnh**. Chi phí sản xuất **Cost/Job = $0.3859** (~10.034 ₫), giá bán **$1.75** (~45.500 ₫), tỷ suất lợi nhuận gộp **Gross Margin = 77.95%** (lãi $1.364 / bệnh nhân).
3. **Tiếp cận khách hàng qua đâu, vì sao là kênh đó?**
   $\rightarrow$ Tiếp cận qua kênh **Partner-Led nhúng vào phần mềm bệnh viện VNPT HIS** vì ngân sách CAC cho phép ($6,548) bị lệch gần 5 lần so với chi phí sales trực tiếp ($32,000), trong khi các bệnh viện đang dùng sẵn VNPT HIS mỗi ngày.
