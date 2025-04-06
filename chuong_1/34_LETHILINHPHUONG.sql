---Lê Thị Linh Phương 22174600010
---1. Tạo bảng NhanVien
CREATE TABLE NhanVien (
    MaNV INT PRIMARY KEY,
    HoTen VARCHAR(50),
    Tuoi INT,
    PhongBan VARCHAR(50)
);

---2. Chèn các bảng ghi vào bảng NhanVien
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

---3. Lấy toàn bộ thông tin của nhân viên trong bảng NhanVien 
SELECT * FROM NhanVien;

---4. Truy vấn HoTen và Tuoi của các nhân viên trong phòng IT 
SELECT HoTen, Tuoi FROM NhanVien WHERE PhongBan = 'IT';

---5. Tìm nhân viên có độ tuổi lớn hơn 25 
SELECT * FROM NhanVien WHERE Tuoi > 25;

---6. Cho biết nhân viên lớn tuổi nhất của các phòng ban 
SELECT PhongBan, HoTen, Tuoi
FROM NhanVien
WHERE Tuoi IN (
    SELECT MAX(Tuoi)
    FROM NhanVien
    GROUP BY PhongBan
);

---7. Chuyển đổi thông tin Phongban của nhân viên "Le Van C" sang "Marketing"
UPDATE NhanVien 
SET PhongBan = 'Marketing' 
WHERE HoTen = 'Le Van C';

--Kiểm tra 
SELECT * 
FROM NhanVien
WHERE HoTen = 'Le Van C';

---8. Xóa nhân viên có "MaSV = 2" rồi cho biết mỗi phòng ban có bao nhiêu người 
DELETE FROM NhanVien WHERE MaNV = 2;
--Đếm số nhân viên sau khi xóa 
SELECT PhongBan, COUNT(*) AS SoLuongNhanVien
FROM NhanVien
GROUP BY PhongBan;

---9. Các bước kết nối đến SQLite trong Python

import sqlite3
--1. Kết nối đến database
conn = sqlite3.connect("nhanvien.db")
cursor = conn.cursor()
--2. Tạo bảng nếu chưa có
cursor.execute("""
CREATE TABLE IF NOT EXISTS NhanVien (
    MaNV INT PRIMARY KEY,
    HoTen VARCHAR(50),
    Tuoi INT,
    PhongBan VARCHAR(50)
)
""")
conn.commit()

--3. Chèn dữ liệu vào bảng
cursor.execute("INSERT INTO NhanVien VALUES (1, 'Nguyen Van A', 30, 'Ke Toan')")
conn.commit()

--4. Truy vấn dữ liệu
cursor.execute("SELECT * FROM NhanVien")
rows = cursor.fetchall()
for row in rows:
    print(row)

--5. Đóng kết nối
conn.close()