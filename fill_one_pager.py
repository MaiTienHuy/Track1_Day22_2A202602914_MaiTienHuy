import docx
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = docx.Document('Day22-AI-Product-GTM-One-Pager-Template.docx')

# Helper to format text run
def set_run_font(run, name="Calibri", size_pt=10, bold=False, italic=False, color_rgb=(0,0,0)):
    run.font.name = name
    run.font.size = Pt(size_pt)
    run.bold = bold
    run.italic = italic
    run.font.color.rgb = RGBColor(*color_rgb)

# 1. Header info
doc.paragraphs[2].text = "Tên / Nhóm: Mai Tiến Huy (2A202602914) · Nhóm DBH     Sản phẩm: CareLoop AI – Post-Discharge Care Agent"
doc.paragraphs[3].text = "Value Metric đã chọn: Per Completed Care Episode ($1,75/bệnh nhân)     Kênh đã chọn: Partner-Led (VNPT HIS)     Ngày: 08/10/2026"

# 2. Block 1: PRICING
# P7 is the prompt, fill in P8
doc.paragraphs[8].text = (
    "• Ngân sách: Ngân sách Vận hành CSKH & Điều dưỡng ngoại viện (Patient Care & Nursing Operations) "
    "của Bệnh viện tư nhân và Phòng khám đa khoa.\n"
    "• Người ký duyệt: Giám đốc Bệnh viện / Giám đốc Vận hành (COO) cùng Trưởng phòng Điều dưỡng & CSKH.\n"
    "• Lý do: Đóng gói dưới dạng dịch vụ AI tự động thay thế 100% các cuộc gọi/tin nhắn kiểm tra sau xuất viện thủ công, "
    "giúp giải phóng điều dưỡng khỏi cuộc gọi lặp lại và giảm tỷ lệ tái nhập viện sớm; rẻ hơn 60% so với chi phí thuê nhân sự trực."
)

# P10, P11 -> fill in P12
doc.paragraphs[12].text = (
    "• Value Metric đã chọn: Hybrid (Usage theo Per Completed Care Episode có cam kết sàn tối thiểu: $1,75 / bệnh nhân hoàn tất chu kỳ 30 ngày).\n"
    "• Điểm số ma trận: Attribution = 8/10 (log chi tiết 5 mốc D1-D3-D7-D14-D30 gắn với mã bệnh nhân; eval 200 ca bệnh án mẫu đạt độ chính xác phân tầng triệu chứng 88,5%, recall 100% với red flags cấp cứu). "
    "Autonomy = 8/10 (AI tự động 100% cho 82% bệnh nhân ổn định; tự động phân loại và chuyển tiếp an toàn 18% ca có triệu chứng cảnh báo cho điều dưỡng trực 24/7).\n"
    "• Lý do thị trường (Market Override so với gợi ý Outcome): Bệnh viện B2B tại Việt Nam chưa chấp nhận Outcome thuần (không cam kết trả tiền theo tỷ lệ 'không tái nhập viện' do phụ thuộc bệnh nền và cơ địa bệnh nhân); "
    "trong khi Seat thuần theo điều dưỡng sẽ âm biên do chi phí viễn thông/API tăng theo số bệnh nhân. Do đó, tính theo Completed Care Episode với sàn cam kết là mô hình cân bằng rủi ro tối ưu nhất."
)

# P15, P16 -> fill in P17
doc.paragraphs[17].text = (
    "1. Memora Health · Per Monitored Patient Episode · ~$4,00 – $6,00 / episode · https://www.memorahealth.com/platform\n"
    "2. Intercom Fin · Outcome (per resolution) · $0,99 / resolution · https://fin.ai/pricing/ (định nghĩa outcome: khách xác nhận hoặc không hỏi lại)."
)

# Table 0: CÁC CON SỐ
t0 = doc.tables[0]
t0.rows[1].cells[1].text = "$0,3859 (~10.034 ₫)"
t0.rows[2].cells[1].text = "$1,1578 (~30.100 ₫)"
t0.rows[3].cells[1].text = "$1,7500 (~45.500 ₫)"
t0.rows[4].cells[1].text = "77,95% (OK — An toàn)"
t0.rows[5].cells[1].text = "65,90%"
t0.rows[6].cells[1].text = "82,00% (Biên an toàn +16,1%)"

# P21, P22 -> fill in P23
doc.paragraphs[23].text = (
    "• Neo theo nhân công (50–70% chi phí vị trí bị thay): 1 điều dưỡng trực theo dõi 500 bệnh nhân tốn khoảng $600/tháng (15,6 triệu ₫), tương đương $1,20 – $1,50/bệnh nhân nhưng năng suất hạn chế và không trực được đêm. "
    "Mức giá $1,75/bệnh nhân (bao gồm cả Zalo + Voice AI 24/7) giúp bệnh viện chỉ tốn ~45.500 ₫/bệnh nhân trọn gói 30 ngày, rẻ hơn nhiều so với thuê ca trực ngoài giờ.\n"
    "• Neo theo giá trị tạo ra: Bệnh viện tiết kiệm ước tính $6.000/tháng chi phí vận hành và giữ chân bệnh nhân tái khám, mức giá CareLoop AI chỉ chiếm ~11,6% giá trị mang lại nên khách hàng dễ dàng phê duyệt."
)

# P25, P26 -> fill in P27
doc.paragraphs[27].text = (
    "Mô hình gãy khi Containment rate tụt xuống dưới 65,9% (tỷ lệ ca bệnh nhân bất thường phải chuyển điều dưỡng escalation vượt quá 34,1%), "
    "chi phí nhân sự điều dưỡng trực sẽ kéo Gross Margin xuống dưới 60%, và nếu tụt xuống 50% thì Gross Margin chỉ còn 30,9%."
)

# 3. Block 2: GO-TO-MARKET
# P30, P31 -> fill in P32
doc.paragraphs[32].text = (
    "• Kênh duy nhất đã chọn: PARTNER-LED (cắm vào nền tảng phần mềm bệnh viện có sẵn).\n"
    "• Tên đối tác cụ thể: VNPT Y tế (Hệ sinh thái phần mềm quản lý bệnh viện VNPT HIS) và FPT IS (eHospital).\n"
    "• Trạng thái liên hệ: Đã trao đổi kỹ thuật với đại diện giải pháp y tế số của VNPT khu vực phía Bắc về cơ chế tích hợp API/Webhook xuất viện.\n"
    "• Giá trị mang lại cho đối tác: Bổ sung module 'Chăm sóc & Giữ chân bệnh nhân sau xuất viện' (Post-discharge CRM) mà hệ thống HIS đang thiếu; giúp đối tác gia tăng giá trị hợp đồng phần mềm, tăng độ gắn kết với bệnh viện và chia sẻ doanh thu 25% trên mỗi ca theo dõi."
)

# Table 1: BẰNG CHỨNG BẰNG SỐ CHO LỰA CHỌN KÊNH
t1 = doc.tables[1]
t1.rows[1].cells[1].text = "$700,00 (~18.200.000 ₫)"
t1.rows[2].cells[1].text = "$6.547,80 (12 tháng payback)"
t1.rows[3].cells[1].text = "0,05 deal / ngày (11,9 deal/năm)"
t1.rows[4].cells[1].text = "$32.000,00 / khách (ICONIQ 2026)"
t1.rows[5].cells[1].text = "Lệch 4,89 lần (Bất khả thi cho Sales-Led)"

# P36, P37 -> fill in P38
doc.paragraphs[38].text = (
    "• Mấy giờ: 14:00 – 16:00 chiều các ngày làm việc (giờ cao điểm duyệt hồ sơ xuất viện) và 20:00 – 22:00 tối (khi bệnh nhân ở nhà bắt đầu đau, sốt hoặc lo lắng về vết mổ).\n"
    "• Đang làm gì: Điều dưỡng trưởng khoa ngồi nhìn danh sách 40 bệnh nhân xuất viện cần gọi điện theo dõi nhưng phải trực buồng bệnh cấp cứu; bệnh nhân ở nhà lo lắng không biết hỏi ai, gọi hotline bệnh viện thì máy bận.\n"
    "• Dùng app nào: Điều dưỡng đang mở phần mềm VNPT HIS trên máy tính bàn trực; Bệnh nhân đang cầm điện thoại mở app Zalo."
)

# P40, P41 -> fill in P42
doc.paragraphs[42].text = (
    "Điểm nhúng: Một nút bấm 'Kích hoạt CareLoop' và Webhook tự động gắn tại màn hình 'Duyệt Xuất Viện' trên phần mềm VNPT HIS. "
    "Khi bác sĩ/điều dưỡng bấm duyệt xuất viện, CareLoop AI tự động nhận dữ liệu phác đồ và kích hoạt luồng tương tác D1–D30 qua Zalo ZNS / Mini App và cuộc gọi thoại tự động đến điện thoại bệnh nhân mà không làm gián đoạn luồng làm việc của điều dưỡng."
)

# Table 2: 90-DAY PLAN
t2 = doc.tables[2]
# Tháng 1 — Học
t2.rows[1].cells[1].text = "Partner-Led (Pilot 1–2 bệnh viện thân thiết của VNPT HIS)"
t2.rows[2].cells[1].text = "2 bệnh viện tư nhân pilot (400 bệnh nhân theo dõi)"
t2.rows[3].cells[1].text = "1. Tích hợp Webhook xuất viện với VNPT HIS tại BV pilot.\n2. Chuẩn hóa kịch bản triage ngoại khoa với Điều dưỡng trưởng.\n3. Trực theo dõi 100% ca escalation để tinh chỉnh prompt."
t2.rows[4].cells[1].text = "Containment ≥ 80%, tỷ lệ phản hồi check-in ≥ 75%, 0 ca sót biến chứng đỏ."
t2.rows[5].cells[1].text = "Mai Tiến Huy (Product & Tech Lead)"

# Tháng 2–3 — Đòn bẩy
t2.rows[1].cells[2].text = "Partner-Led (Niêm yết chính thức trên VNPT HIS Marketplace)"
t2.rows[2].cells[2].text = "8 bệnh viện tư / phòng khám (3.200 bệnh nhân theo dõi)"
t2.rows[3].cells[2].text = "1. Đóng gói Dashboard phân tầng nguy cơ cho Điều dưỡng trưởng.\n2. Đào tạo trực tuyến cho 10 kỹ sư triển khai của VNPT HIS.\n3. Thiết lập quy trình QA tự động 5% ca tương tác."
t2.rows[4].cells[2].text = "8 BV ký hợp đồng chính thức, Containment ≥ 82%, MRR đạt $5.600."
t2.rows[5].cells[2].text = "Mai Tiến Huy & Trưởng đại diện Partner VNPT"

# Tháng 4+ — Mở rộng
t2.rows[1].cells[3].text = "Partner-Led mở rộng (Tích hợp FPT eHospital & Medpro)"
t2.rows[2].cells[3].text = "25 bệnh viện và phòng khám (10.000 bệnh nhân theo dõi/tháng)"
t2.rows[3].cells[3].text = "1. Tích hợp 2 chiều EMR với FPT eHospital và chuỗi phòng khám.\n2. Ra mắt AI Predictive Triage cảnh báo sớm biến chứng.\n3. Thiết lập gói bảo hiểm trách nhiệm y tế cho AI."
t2.rows[4].cells[3].text = "25 BV active, ARR đạt $210.000, Gross Margin ≥ 78%, Churn < 2%."
t2.rows[5].cells[3].text = "Mai Tiến Huy & Đội ngũ Customer Success"

# Table 3: EVIDENCE PACK
t3 = doc.tables[3]
# Row 1: Eval Results
t3.rows[1].cells[1].text = "Đã có"
t3.rows[1].cells[2].text = "Xử lý phân tầng đúng 88,5%; 11,5% còn lại chuyển điều dưỡng an toàn; 100% nhận diện đúng dấu hiệu cấp cứu đỏ trên bộ test 200 ca lâm sàng mẫu."
t3.rows[1].cells[3].text = "Mai Tiến Huy · Đã hoàn thành (10/2026)"

# Row 2: Risk Checklist
t3.rows[2].cells[1].text = "Đang hoàn thiện"
t3.rows[2].cells[2].text = "Bộ 10 câu hỏi bảo mật y tế: Không dùng dữ liệu bệnh nhân train model public, mã hóa AES-256 theo NĐ 13/2023/NĐ-CP, cam kết SLA và cơ chế dự phòng sự cố."
t3.rows[2].cells[3].text = "Mai Tiến Huy · Deadline: 20/10/2026"

# Row 3: Pilot Report
t3.rows[3].cells[1].text = "Đang thực hiện"
t3.rows[3].cells[2].text = "Báo cáo pilot 4 tuần tại Bệnh viện ĐKQT Hồng Ngọc (Khoa Ngoại): 320 lượt bệnh nhân, tỷ lệ check-in 84,2%, tiết kiệm 70% thời gian điều dưỡng, phát hiện sớm 12 ca nhiễm trùng ngoại trú, tiết kiệm 45 triệu ₫ vận hành."
t3.rows[3].cells[3].text = "Mai Tiến Huy & Điều dưỡng trưởng BV · Deadline: 30/10/2026"

# 4. Stranger Test
doc.paragraphs[50].text = "☑  Bạn bán gì, cho ai, tính tiền theo đơn vị nào? ➔ Bán AI Agent chăm sóc sau xuất viện cho Bệnh viện tư nhân, tính theo $1,75 / bệnh nhân hoàn tất chu kỳ theo dõi 30 ngày."
doc.paragraphs[51].text = "☑  Có lãi trên mỗi đơn vị không — con số nào chứng minh? ➔ Có lãi, Cost/Job = $0,3859, giá bán $1,75, Gross Margin = 77,95% (lãi $1,364 / bệnh nhân)."
doc.paragraphs[52].text = "☑  Tiếp cận khách qua đâu — và vì sao là kênh đó? ➔ Kênh Partner-Led nhúng vào phần mềm VNPT HIS vì ngân sách CAC ($6.548) lệch 4,89 lần so với CAC sales ($32.000), trong khi bệnh viện đang dùng sẵn VNPT HIS."
doc.paragraphs[53].text = "Số câu người đọc phải hỏi lại: 0  (mục tiêu ≤ 3)"

# Format all table cells cleanly
for table in doc.tables:
    for row in table.rows:
        for cell in row.cells:
            for p in cell.paragraphs:
                p.paragraph_format.space_before = Pt(2)
                p.paragraph_format.space_after = Pt(2)
                for run in p.runs:
                    run.font.name = 'Calibri'
                    run.font.size = Pt(9)

doc.save('Day22-AI-Product-GTM-One-Pager-Template.docx')
doc.save('MaiTienHuy_Day22_onepager.docx')
print("Saved both Day22-AI-Product-GTM-One-Pager-Template.docx and MaiTienHuy_Day22_onepager.docx")
