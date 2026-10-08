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


## 2. Bản đồ Số liệu Cốt lõi (Golden Metrics)

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

## 3. Hướng dẫn Giám khảo / Người chấm Đánh giá Nhanh (2-minute Stranger Test)
1. **Bạn bán gì, cho ai, tính tiền theo đơn vị nào?**
   $\rightarrow$ Bán dịch vụ AI Agent theo dõi chăm sóc và sàng lọc biến chứng sau xuất viện cho các Bệnh viện tư nhân & Phòng khám đa khoa, tính tiền theo đơn vị **$1.75 / bệnh nhân hoàn tất chu kỳ 30 ngày (Completed Care Episode)**.
2. **Có lãi trên mỗi đơn vị không, con số nào chứng minh?**
   $\rightarrow$ **Có lãi rất lành mạnh**. Chi phí sản xuất **Cost/Job = $0.3859** (~10.034 ₫), giá bán **$1.75** (~45.500 ₫), tỷ suất lợi nhuận gộp **Gross Margin = 77.95%** (lãi $1.364 / bệnh nhân).
3. **Tiếp cận khách hàng qua đâu, vì sao là kênh đó?**
   $\rightarrow$ Tiếp cận qua kênh **Partner-Led nhúng vào phần mềm bệnh viện VNPT HIS** vì ngân sách CAC cho phép ($6,548) bị lệch gần 5 lần so với chi phí sales trực tiếp ($32,000), trong khi các bệnh viện đang dùng sẵn VNPT HIS mỗi ngày.
