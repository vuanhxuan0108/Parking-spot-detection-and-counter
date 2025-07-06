# 🚗 Parking Spot Detection and Counter

Dự án giúp **phát hiện và đếm số lượng chỗ đậu xe trống** trong video giám sát bãi đỗ xe. Ứng dụng sử dụng **OpenCV** để xử lý video và **Machine Learning** để phân loại chỗ trống / có xe.

---

## 📌 Mục tiêu đề tài

- Xác định các vùng đỗ xe trên video bằng ảnh mask thủ công
- Dự đoán từng vị trí có xe hay trống dựa trên ảnh cắt từ video
- Đếm số lượng chỗ trống và hiển thị: `Chỗ trống / Tổng số chỗ`

---

## 📁 Cấu trúc thư mục

```
.
├── data/                    # Chứa video .mp4 input
├── mask/                    # Chứa các ảnh mask định nghĩa vùng đỗ xe
├── model/                   # Mô hình đã huấn luyện (model.p)
├── clf-data/                # Ảnh cắt từ các slot đỗ xe để huấn luyện
├── crop_cars.py             # Script để cắt ảnh từ video theo mask
├── train_model.py           # Huấn luyện mô hình phân loại slot
├── main.py                  # Phát hiện chỗ trống và hiển thị kết quả
├── utils.py                 # Các hàm hỗ trợ
├── requirements.txt         # Thư viện cần cài
└── README.md
```

---

## 🚀 Cách sử dụng

### 1. Cài đặt thư viện

```bash
pip install -r requirements.txt
```

---

### 2. Cắt ảnh các vị trí đỗ xe từ video để huấn luyện

```bash
python crop_cars.py
```

Kết quả: ảnh `.jpg` được lưu trong `clf-data/` tương ứng với từng chỗ đậu xe.

---

### 3. Huấn luyện mô hình phân loại có xe / trống

```bash
python train_model.py
```

Sau khi huấn luyện, model sẽ được lưu ở `model/model.p`.

---

### 4. Chạy chương trình chính để phát hiện chỗ trống

```bash
python main.py
```

- Hiển thị video và trạng thái từng chỗ: **trống (xanh lá)** hoặc **có xe (đỏ)**
- Hiển thị số lượng chỗ trống / tổng số ngay trên khung hình

---

## 🧠 Mô hình Machine Learning

- **Thuật toán**: SVM (Scikit-learn)
- **Dữ liệu huấn luyện**: Ảnh kích thước 15x15 RGB từ từng slot
- **Nhãn**: 
  - `0` = Trống
  - `1` = Có xe

---

## 🎥 Đầu vào

- Video: `data/parking_1920_1080.mp4`
- Mask ảnh định vị slot: `mask/mask_1920_1080.png`

> Các video `.mp4` có dung lượng lớn nên nên dùng **Git LFS** hoặc upload riêng.

---

## 📊 Kết quả đầu ra

- Video realtime với trạng thái các chỗ đậu
- Số lượng chỗ trống / tổng số được cập nhật mỗi frame

---

## 📷 Demo (giả sử)

```
Chỗ trống: 53 / 85
```

---

## 📝 Tác giả

- **Vũ Anh Xuân – 2025**  
- Dự án thực hiện trong khuôn khổ học phần hoặc đồ án chuyên ngành.

---

## 📄 License

MIT License