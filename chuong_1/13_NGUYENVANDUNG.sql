---BTVN_CHƯƠNG 1 CÂU 1-8---


---1. Tạo bảng NhanVien
CREATE TABLE NhanVien (
    MaNV INT PRIMARY KEY,
    HoTen VARCHAR(50),
    Tuoi INT,
    PhongBan VARCHAR(50)
);

---2. Chèn các bản ghi vào bảng NhanVien
INSERT INTO NhanVien (MaNV, HoTen, Tuoi, PhongBan) VALUES
(1, 'Nguyen Van A', 30, 'Ke Toan'),
(2, 'Tran Thi B', 25, 'Nhan Su'),
(3, 'Le Van C', 28, 'IT'),
(4, 'Pham Thi D', 32, 'Ke Toan'),
(5, 'Vu Van E', 26, 'IT'),
(6, 'Nguyen Thi F', 29, 'Marketing'),
(7, 'Le Thi G', 27, 'Nhan Su'),
(8, 'Hoang Van H', 35, 'Ke Toan'),
(9, 'Pham Van I', 33, 'Marketing'),
(10, 'Tran Van J', 24, 'IT'),
(11, 'Dang Thi K', 31, 'Nhan Su'),
(12, 'Nguyen Van L', 28, 'Ke Toan'),
(13, 'Tran Thi M', 26, 'Marketing'),
(14, 'Pham Van N', 30, 'Nhan Su'),
(15, 'Hoang Thi O', 27, 'IT');

---3.Lấy toàn bộ thông tin của nhân viên trong bảng NhanVien
SELECT * FROM NhanVien;

---Lấy tất cả các thông tin của các nhân viên trong bảng NhanVien mà HoTen có chứa từ "Nguyen" (không phân biệt vị trí trong chuỗi)
SELECT * FROM NhanVien
WHERE HoTen LIKE '%Nguyen%';

---4. Truy vấn HoTen và Tuoi của nhân viên trong phòng IT
SELECT HoTen, Tuoi 
FROM NhanVien
WHERE PhongBan = 'IT';

---5. Tìm nhân viên có độ tuổi lớn hơn 25
SELECT * 
FROM NhanVien
WHERE Tuoi > 25;

---6. Cho biết nhân viên lớn tuổi nhất của các PhongBan
SELECT PhongBan, HoTen, Tuoi
FROM NhanVien
WHERE Tuoi IN (
    SELECT MAX(Tuoi)
    FROM NhanVien
    GROUP BY PhongBan
);

---7. Chuyển đổi thông tin PhongBan của nhân viên "Le Van C" sang "Marketing"
UPDATE NhanVien
SET PhongBan = 'Marketing'
WHERE HoTen = 'Le Van C';
---Kiểm tra
SELECT * 
FROM NhanVien
WHERE HoTen = 'Le Van C';
---Kiểm tra tính duy nhất của dữ liệu
UPDATE NhanVien
SET PhongBan = 'Marketing'
WHERE MaNV = 3;

---PHẦN CÂU HỎI BƯỚC 7: Sau khi kiểm tra tính duy nhất của dữ liệu, ta thấy mỗi nhân viên trong bảng có một mã nhân viên (MaNV) duy nhất để dễ dàng xác định bản ghi cần cập nhật
---Như vậy, không có vấn đề gặp phải khi thực hiện chuyển đổi thông tin Bước 7

---Giả sử có vấn đề chuyển đổi thông tin, ta có thể có các giải pháp là:
---Giải pháp 1: Kiểm tra tính duy nhất của dữ liệu thay vì sử dụng HoTen thì dùng MaNV tránh sự trùng lặp vì mỗi NV chỉ có 1 mã
UPDATE NhanVien
SET PhongBan = 'Marketing'
WHERE MaNV = 3;
---Giải pháp 2: Kiểm tra dữ liệu trước khi cập nhật
SELECT * 
FROM NhanVien
WHERE HoTen = 'Le Van C';
---Giải pháp 3: Xác nhận tính chính xác sau khi cập nhật

---8. Xóa nhân viên có maNV = '2' và cho biết PhongBan có boa nhiêu người
DELETE FROM NhanVien
WHERE MaNV = 2;
---Dem so nhan vien sau khi xoa
SELECT PhongBan, COUNT(*) AS SoLuongNhanVien
FROM NhanVien
GROUP BY PhongBan;