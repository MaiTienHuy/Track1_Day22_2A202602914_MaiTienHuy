import openpyxl

wb = openpyxl.load_workbook('Day22-AI-Product-GTM-Monetization-Model.xlsx')

# Tab 6_Benchmarks
ws6 = wb['6_Benchmarks']
ws6['B3'] = "2026-10-08 (Kiểm tra và cập nhật tại ngày làm bài)"

# Tab 1_Cost_Job
ws1 = wb['1_Cost_Job']
ws1['B5'] = "1 chu kỳ theo dõi sau xuất viện 30 ngày của 1 bệnh nhân hoàn tất (đủ các mốc check-in D1-D3-D7-D14 và tổng kết D30, có sàng lọc nguy cơ y tế an toàn)"
ws1['B6'] = "B"
ws1['B9'] = 1000.0
ws1['B10'] = 0.82
ws1['B15'] = 1.0
ws1['B16'] = 5.0
ws1['B17'] = 1.25
ws1['B18'] = 0.10
ws1['B19'] = 8.0
ws1['B20'] = 3000.0
ws1['B21'] = 800.0
ws1['B22'] = 250.0
ws1['B30'] = 0.0
ws1['B34'] = 0.0077
ws1['B35'] = 2.0
ws1['B36'] = 50.0
ws1['B37'] = 1200.0
ws1['B41'] = 0.010
ws1['B42'] = 0.012
ws1['B46'] = 0.08
ws1['B50'] = 9.0
ws1['B51'] = 0.05
ws1['B52'] = 2.0
ws1['B53'] = 6.0
ws1['B59'] = 0.0
ws1['B68'] = 26000.0

# Tab 2_Pricing
ws2 = wb['2_Pricing']
ws2['B6'] = 3.0
ws2['B10'] = 6000.0
ws2['B11'] = 400.0
ws2['B14'] = 1200.0
ws2['B19'] = 1.75
ws2['B32'] = 0.60

# Tab 3_Value_Metric
ws3 = wb['3_Value_Metric']
ws3['B5'] = 2.0
ws3['B6'] = 2.0
ws3['B7'] = 1.0
ws3['B8'] = 1.0
ws3['B9'] = 2.0
ws3['B13'] = 2.0
ws3['B14'] = 2.0
ws3['B15'] = 2.0
ws3['B16'] = 1.0
ws3['B17'] = 1.0

# Benchmarks
ws3['A26'] = "Memora Health"
ws3['B26'] = "Per Monitored Patient Episode"
ws3['C26'] = "~$4,00 - $6,00 / episode"
ws3['D26'] = "memorahealth.com/platform"

ws3['A27'] = "Intercom Fin"
ws3['B27'] = "Outcome (per resolution)"
ws3['C27'] = "$0,99 / resolution"
ws3['D27'] = "fin.ai/pricing"

ws3['B30'] = "Hybrid (Usage theo Care Episode có sàn cam kết)"
ws3['B31'] = "Thị trường y tế B2B Việt Nam chưa chấp nhận Outcome thuần (bệnh viện không đồng ý cam kết trả tiền theo tỷ lệ 'không tái nhập viện' vì kết quả phụ thuộc nhiều vào cơ địa, bệnh nền và tuân thủ thuốc của bệnh nhân); đồng thời Seat thuần theo điều dưỡng sẽ làm nhà cung cấp lỗ nặng vì chi phí API/viễn thông tăng theo số lượng bệnh nhân. Do đó, Hybrid/Usage theo Per Completed Care Episode ($1,75/bệnh nhân 30 ngày) có mức cam kết tối thiểu là lựa chọn cân bằng rủi ro hoàn hảo nhất."
ws3['B32'] = "Tôi chọn đơn vị: Per Completed Care Episode ($1,75 / chu kỳ theo dõi 30 ngày của một bệnh nhân xuất viện)."
ws3['B33'] = "Attribution đạt 8/10 nhờ log chi tiết từng mốc tương tác và bộ eval 200 ca phân tầng nguy cơ đạt độ chính xác 88,5%; Autonomy đạt 8/10 khi AI tự vận hành 82% chu kỳ chăm sóc ổn định 24/7 và tự động bàn giao 18% ca có triệu chứng cảnh báo."
ws3['B34'] = "Mô hình sẽ âm biên hoặc lỗ khi Containment rate tụt xuống dưới 65,9% (tỷ lệ ca bệnh nhân bất thường phải can thiệp vượt quá 34,1%), khiến chi phí điều dưỡng trực escalation ăn hết biên lợi nhuận; rủi ro này được chặn bằng trần số lượt can thiệp và cơ chế phân tầng nguy cơ 3 cấp độ."

# Tab 4_Channel_Fit
ws4 = wb['4_Channel_Fit']
ws4['B5'] = 700.0
ws4['B7'] = "SMB"
ws4['B13'] = 100000.0
ws4['B14'] = 250.0
ws4['B20'] = 8000.0
ws4['B21'] = 0.25

# Scorecard
ws4['B28'] = 2.0; ws4['C28'] = 1.0; ws4['D28'] = 5.0
ws4['B29'] = 1.0; ws4['C29'] = 3.0; ws4['D29'] = 5.0
ws4['B30'] = 3.0; ws4['C30'] = 2.0; ws4['D30'] = 4.0
ws4['B31'] = 2.0; ws4['C31'] = 2.0; ws4['D31'] = 5.0
ws4['B32'] = 1.0; ws4['C32'] = 3.0; ws4['D32'] = 5.0
ws4['B33'] = 2.0; ws4['C33'] = 2.0; ws4['D33'] = 5.0

ws4['B38'] = "Partner-Led"
ws4['B39'] = "VNPT Y tế (Hệ sinh thái VNPT HIS) và FPT IS (eHospital)"
ws4['B40'] = "Rồi"
ws4['B41'] = "Bổ sung module Chăm sóc & Giữ chân bệnh nhân sau xuất viện (Post-discharge CRM) mà hệ thống HIS đang thiếu, giúp VNPT HIS gia tăng giá trị hợp đồng, tăng độ gắn kết với bệnh viện và chia sẻ doanh thu 25% trên mỗi ca theo dõi."
ws4['B42'] = "Đi theo lối thoát Partner-Led để cắm thẳng vào cơ sở khách hàng sẵn có của VNPT HIS (hơn 60% bệnh viện tại Việt Nam), bypass hoàn toàn bài toán chi phí CAC trực tiếp khổng lồ của Sales-Led ($32.000 vs ngân sách $6.548)."

# Tab 5_90Day_Plan
ws5 = wb['5_90Day_Plan']
ws5['B5'] = "14:00 - 16:00 (giờ cao điểm duyệt xuất viện) và 20:00 - 22:00 (khi bệnh nhân ở nhà bắt đầu đau, lo lắng)"
ws5['B6'] = "Điều dưỡng trưởng loay hoay trước danh sách 40 bệnh nhân xuất viện cần gọi điện nhưng bận trực buồng bệnh; bệnh nhân ở nhà có dấu hiệu sốt, rỉ dịch vết mổ nhưng không biết hỏi ai"
ws5['B7'] = "Điều dưỡng trực mở phần mềm VNPT HIS / eHospital trên máy tính; Bệnh nhân đang cầm điện thoại dùng Zalo"
ws5['B8'] = "Một nút bấm 'Kích hoạt CareLoop' và Webhook tự động gắn tại màn hình 'Duyệt Xuất Viện' trên phần mềm VNPT HIS; tương tác với bệnh nhân qua Zalo Mini App / Zalo ZNS / cuộc gọi thoại tự động"

# 90 Day Plan
ws5['B12'] = "Partner-Led (Pilot 1-2 bệnh viện thân thiết của VNPT HIS)"
ws5['C12'] = "Partner-Led (Chính thức niêm yết module trên VNPT HIS App Marketplace)"
ws5['D12'] = "Partner-Led mở rộng (Tích hợp thêm FPT eHospital & nền tảng Medpro)"

ws5['B13'] = "2 bệnh viện tư nhân pilot (400 bệnh nhân theo dõi)"
ws5['C13'] = "8 bệnh viện tư nhân / phòng khám đa khoa (3.200 bệnh nhân theo dõi)"
ws5['D13'] = "25 bệnh viện và phòng khám (10.000 bệnh nhân theo dõi/tháng)"

ws5['B14'] = "Hoàn tất tích hợp API Webhook xuất viện với bản cài đặt VNPT HIS tại bệnh viện pilot"
ws5['C14'] = "Đóng gói tài liệu chuẩn hóa và cổng Dashboard phân tầng nguy cơ cho Điều dưỡng trưởng"
ws5['D14'] = "Tích hợp hệ thống đồng bộ hai chiều EMR với FPT eHospital và chuỗi phòng khám tư"

ws5['B15'] = "Cùng Điều dưỡng trưởng thẩm định kịch bản triage y tế cho khoa Ngoại tiêu hóa và Sản khoa"
ws5['C15'] = "Tổ chức đào tạo trực tuyến cho 10 kỹ sư triển khai của VNPT HIS tại các tỉnh"
ws5['D15'] = "Ra mắt tính năng cảnh báo sớm biến chứng dựa trên chuỗi thời gian sinh hiệu (AI Predictive Triage)"

ws5['B16'] = "Trực theo dõi 100% ca escalation để tinh chỉnh prompt an toàn lâm sàng"
ws5['C16'] = "Thiết lập quy trình kiểm tra QA tự động 5% ca tương tác và SLA phản hồi dưới 15 phút"
ws5['D16'] = "Xây dựng gói bảo hiểm trách nhiệm y tế (Medical Malpractice Insurance) cho hệ thống AI"

ws5['B17'] = "Containment rate >= 80%, tỷ lệ bệnh nhân phản hồi check-in >= 75%, 0 ca sót biến chứng"
ws5['C17'] = "8 bệnh viện ký hợp đồng chính thức, Containment ổn định >= 82%, MRR đạt $5.600"
ws5['D17'] = "25 bệnh viện active, ARR đạt $210.000, Gross Margin >= 78%, Churn rate < 2%"

ws5['B18'] = "Mai Tiến Huy (Product & Tech Lead)"
ws5['C18'] = "Mai Tiến Huy & Trưởng nhóm giải pháp Y tế số VNPT"
ws5['D18'] = "Mai Tiến Huy (Điều hành chung) & Đội ngũ Customer Success"

# Evidence Pack
ws5['B23'] = "Rồi"
ws5['C23'] = "Tỷ lệ phân tầng nguy cơ triệu chứng chính xác đạt 88,5% trên 200 ca bệnh án mẫu; 11,5% còn lại chuyển điều dưỡng an toàn; 100% nhận diện đúng dấu hiệu cấp cứu đỏ."
ws5['D23'] = "Mai Tiến Huy · Đã hoàn thành (10/2026)"

ws5['B24'] = "Chưa"
ws5['C24'] = "Bộ 10 câu hỏi bảo mật y tế: Không dùng dữ liệu bệnh nhân train model public, mã hóa AES-256 theo NĐ 13/2023/NĐ-CP, cam kết SLA và cơ chế dự phòng khi sự cố."
ws5['D24'] = "Mai Tiến Huy · Hoàn thành trước 20/10/2026"

ws5['B25'] = "Chưa"
ws5['C25'] = "Báo cáo pilot 4 tuần tại Bệnh viện ĐKQT Hồng Ngọc: 320 lượt bệnh nhân, tỷ lệ check-in 84,2%, tiết kiệm 70% thời gian điều dưỡng, phát hiện sớm 12 ca nhiễm trùng ngoại trú."
ws5['D25'] = "Mai Tiến Huy & Điều dưỡng trưởng BV · Hoàn thành trước 30/10/2026"

# Stranger test
ws5['B29'] = "Được"
ws5['B30'] = "Được"
ws5['B31'] = "Được"
ws5['B32'] = 0

wb.save('Day22-AI-Product-GTM-Monetization-Model.xlsx')
wb.save('MaiTienHuy_Day22_model.xlsx')
print("Saved both Day22-AI-Product-GTM-Monetization-Model.xlsx and MaiTienHuy_Day22_model.xlsx")
