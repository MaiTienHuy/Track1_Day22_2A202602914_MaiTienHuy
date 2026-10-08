# AI Support Log — Day 22: Monetization & GTM Model

- **Học viên:** Mai Tiến Huy · **MHV:** 2A202602914
- **Lớp / Nhóm:** AI-IN-ACTION Track 1 · Nhóm DBH
- **Dự án:** CareLoop AI — AI Agent Hỗ trợ Chăm sóc Sau Xuất viện & Phòng Tái Nhập viện
- **Ngày thực hiện:** 08/10/2026
- **Công cụ AI sử dụng:** Claude 3.5 Sonnet / Codex (OpenAI)

---

## 1. Phần tôi đã làm (Human Driver & Chủ sở hữu mô hình)

Toàn bộ mô hình kinh tế, dữ liệu thị trường và quyết định định vị của CareLoop AI đều do tôi trực tiếp nghiên cứu, xây dựng và chịu trách nhiệm:

1. **Xác định bài toán & Định vị ngân sách (Trạm 1):**
   - Tôi tự định nghĩa Job cho CareLoop AI là *"1 chu kỳ theo dõi sau xuất viện 30 ngày của 1 bệnh nhân hoàn tất"* dựa trên các mốc theo dõi lâm sàng D1-D3-D7-D14-D30 đã xây dựng từ Day 20.
   - Tôi từ chối cách đóng gói "phần mềm y tế" (tránh ngân sách CNTT bệnh viện với thủ tục đấu thầu kéo dài 9–18 tháng); tôi quyết định định vị sản phẩm vào **Ngân sách Vận hành CSKH & Điều dưỡng ngoại viện** để cạnh tranh trực tiếp với chi phí thuê nhân sự trực tổng đài theo dõi.
   - Tôi tự viết định nghĩa hoàn tất job chặt chẽ (hoàn thành tối thiểu 4/5 mốc check-in hoặc bàn giao thành công cho điều dưỡng; không tính tiền nếu bệnh nhân từ chối ngay từ D1).

2. **Khảo sát giá API, thiết kế kiến trúc kỹ thuật & Lập bảng chi phí (Trạm 3):**
   - Tôi tự truy cập trang giá nhà cung cấp ngày 08/10/2026 để kiểm tra giá: Claude Haiku 4.5 ($1/$5 per 1M), Deepgram Nova-3 ($0.0077/phút), ElevenLabs Flash ($50/1M ký tự), cước SIP Trunk ($0.012/phút).
   - Tôi tự tính toán số lượt (8 turns) và phân bổ token input: 3.000 token system prompt/phác đồ y tế (tận dụng prompt caching giảm 44,9% chi phí) và 800 token dữ liệu động của bệnh nhân.
   - Tôi tự thiết lập cấu trúc 5 thành phần chi phí trong Excel và kiên quyết chọn **Biến thể B** của HITL (CareLoop AI chịu chi phí điều dưỡng trực escalation $9/giờ) vì hiểu rằng bệnh viện tư nhân chỉ ký hợp đồng khi có cam kết bao phủ ca trực.
   - Tôi tự thiết lập công thức mẫu số là **820 jobs hoàn thành** (loại bỏ 180 ca escalate không tự động) để bảo đảm chi phí Cost/Job phản ánh đúng thực tế vận hành.

3. **Chấm điểm Ma trận & Quyết định Value Metric (Trạm 2):**
   - Tôi tự chấm điểm thực tế sản phẩm: Attribution đạt 8/10, Autonomy đạt 8/10 dựa trên bộ log và kết quả eval 200 ca bệnh án mẫu.
   - Tôi tự tìm kiếm và đối chiếu 2 sản phẩm benchmark quốc tế cùng loại job: Memora Health ($4–$6/episode) và Intercom Fin ($0.99/resolution).
   - Tôi chủ động ghi đè (**Market Override**) gợi ý Outcome của model: Tôi quyết định chọn **Hybrid / Usage theo Per Completed Care Episode ($1.75/bệnh nhân 30 ngày)** vì hiểu sâu tâm lý bệnh viện B2B tại Việt Nam (không chấp nhận rủi ro Outcome thuần "không tái nhập viện" do phụ thuộc cơ địa bệnh nhân, trong khi Seat thuần sẽ làm tôi lỗ nặng chi phí viễn thông).

4. **Tính toán Affordability Test & Chốt kênh phân phối (Trạm 4):**
   - Tôi tự đưa ra các giả định kinh doanh B2B y tế tại Việt Nam: ARPU = $700/tháng (bệnh viện quy mô 400 ca xuất viện/tháng), quota AE = $100.000/năm.
   - Tôi tự tính ra ngân sách CAC tối đa là $6.547,80 và phát hiện độ lệch 4.89 lần so với CAC Sales-Led thực tế ($32.000 từ benchmark ICONIQ 2026).
   - Tôi tự chấm điểm Scorecard 3 kênh và quyết định chọn duy nhất kênh **Partner-Led**.
   - Tôi tự chọn 2 đối tác cụ thể: **VNPT Y tế (VNPT HIS)** và **FPT IS (eHospital)**, trực tiếp chuẩn bị đề xuất giá trị: bổ sung module Post-discharge CRM và chia sẻ 25% doanh thu cho đối tác.

5. **Thiết kế Pain Moment, Điểm nhúng & Kế hoạch 90 ngày (Trạm 5 & 6):**
   - Tôi tự phác họa Pain Moment thực tế từ quan sát tại bệnh viện: 14h–16h (giờ cao điểm ký giấy xuất viện) và 20h–22h (khi bệnh nhân ở nhà lo lắng); điều dưỡng đang dùng VNPT HIS, bệnh nhân dùng Zalo.
   - Tôi tự xác định điểm nhúng: Webhook kích hoạt CareLoop ngay trên màn hình "Duyệt xuất viện" của VNPT HIS.
   - Tôi tự lập Kế hoạch 90 ngày với 3 giai đoạn rõ ràng: Tháng 1 học (2 BV pilot, 400 ca), Tháng 2–3 đòn bẩy (8 BV, 3.200 ca), Tháng 4+ mở rộng (25 BV, 10.000 ca/tháng).
   - Tôi tự soạn thảo nội dung 3 tài sản Evidence Pack (kết quả Eval 88,5% accuracy, bộ 10 câu hỏi bảo mật y tế NĐ 13/2023, báo cáo pilot tại BVĐKQT Hồng Ngọc).

---

## 2. Phần AI đã hỗ trợ (Challenger & Phản biện độc lập)

Tôi chỉ sử dụng AI như một công cụ phản biện khách quan, đóng vai trò **CFO khắt khe và Kỹ sư hạ tầng hoài nghi** để tìm lỗ hổng trong các giả định tôi đã lập:

1. **Thực thi Prompt 4.7.1 — Cost/Job Stress Test:**
   - Tôi đưa toàn bộ bảng giả định chi phí do tôi tính vào prompt để AI rà soát lỗi số học và các chi phí bị bỏ sót.
   - AI kiểm tra tính toán prompt caching, cảnh báo biến động giá API (Deepgram), tính toán lại phương trình Breakeven Containment và chỉ ra biến rủi ro lớn nhất ("The One Number That Kills Me").
2. **Thực thi Prompt 4.7.3 — Channel Reality Check:**
   - Tôi đưa các con số ARPU, ACV, quota và ngân sách CAC của tôi vào để AI kiểm tra tính khả thi toán học của Sales-Led.
   - AI đối chiếu ngân sách CAC của tôi với benchmark chi phí bán hàng doanh nghiệp của ICONIQ 2026 và đưa ra câu hỏi phản biện mạnh nhất về động lực của đối tác Partner-Led.

---

## 3. Phần tôi đánh giá & ra quyết định (Accept / Reject / Partial)

Trước các ý kiến phản biện của AI, tôi trực tiếp cân nhắc và đưa ra quyết định cuối cùng dựa trên thực tế thị trường y tế Việt Nam:

| Vấn đề AI phản biện | Phân tích của tôi | Quyết định của tôi | Hành động điều chỉnh trong Model & One-Pager |
|---|---|:---:|---|
| **Mẫu số Cost/Job** | AI xác nhận việc chia cho 820 jobs hoàn thành thay vì 1.000 job thử làm Cost/Job tăng từ $0.3165 lên $0.3859 (+21,9%). | **ACCEPT** | Giữ vững mẫu số 820 completed jobs trong công thức Excel để bảo đảm tính trung thực của COGS. |
| **Giá API biến động** | AI cảnh báo Deepgram có giá khuyến mại $0.0048/phút nhưng giá list là $0.0077/phút. | **ACCEPT** | Sử dụng giá List $0.0077/phút trong model để đảm bảo mô hình tài chính không bị gãy khi hết đợt khuyến mại. |
| **Độ trễ & Batch API** | AI gợi ý dùng Batch API để giảm 50% chi phí token LLM. | **REJECT** | Bác bỏ vì CareLoop AI tương tác chăm sóc bệnh nhân cần phản hồi tức thì (< 3 giây), không thể dùng Batch API chạy theo lô (trễ tới 24h). |
| **Chi phí lưu trữ y tế** | AI đề xuất nâng phí infra lên $0.05/job do yêu cầu audit log y tế. | **PARTIAL** | Tôi chấp nhận nâng từ $0.005 lên $0.010/job cho DB/logging nội địa (Viettel Cloud/AWS Singapore), nhưng không tăng tới $0.05 vì kiến trúc dữ liệu của MVP chỉ lưu tóm tắt triệu chứng. |
| **Kênh Sales-Led** | AI chỉ ra ngân sách CAC $6.548 bị lệch 4.89 lần so với CAC thực tế $32.000 $\rightarrow$ Bất khả thi. | **ACCEPT** | Chốt 100% nguồn lực 90 ngày đầu vào Partner-Led; loại bỏ hoàn toàn ý định tuyển Sales Rep đi gõ cửa từng bệnh viện. |
| **Đề xuất kênh PLG** | AI gợi ý đổi sang PLG giá rẻ $50/tháng cho các phòng khám tư tự đăng ký để dễ tăng trưởng. | **REJECT** | Bác bỏ vì đặc thù y tế tại Việt Nam: các phòng khám không bao giờ tự đưa dữ liệu bệnh nhân lên một website lạ nếu không có xác thực pháp lý và tích hợp trực tiếp vào phần mềm quản lý phòng khám có sẵn. |
| **Kiểm chứng Partner** | AI đưa ra phép thử: Nếu sau 14 ngày đối tác VNPT không cấp tài liệu API thì kế hoạch bị sập. | **ACCEPT** | Đưa mốc kết nối API pilot trong 14 ngày đầu vào Kế hoạch Tháng 1 của 90-day plan và chuẩn bị phương án dự phòng làm việc song song với FPT IS. |

---

## 4. Kết luận về tính tự chủ của bài làm

- **Tỷ lệ đóng góp:** **85% Học viên** (Nghiên cứu thị trường, xây dựng phác đồ, thiết lập toàn bộ công thức Excel, ra quyết định định giá, liên hệ đối tác) / **15% AI** (Phản biện độc lập theo prompt mẫu và kiểm tra số học).
- Mọi con số trong bảng tính và văn bản One-Pager đều phản ánh đúng bản chất vận hành thực tế của dự án CareLoop AI do tôi phát triển.
