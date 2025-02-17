-- 1: Tạo bảng NhanVien
CREATE TABLE NhanVien(
    MANV INT PRIMARY KEY,
    HoTeN VARCHAR(50),
    Tuoi INT,
    PhongBan VARCHAR(50)
);

-- 2: Chèn dữ liệu vào bảng NhanVien
INSERT INTO NhanVien(MANV, HoTeN, Tuoi, PhongBan)
VALUES 
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

-- 3: Hiển thị toàn bộ bảng NhanVien
SELECT * FROM NhanVien;
-- liệt kê những nhân viên trong tên có từ 'Nguyen'
select HoTen, Tuoi, PhongBan from NhanVien
where HoTen like 'Nguyen%'

-- 4: Lấy tên và tuổi nhân viên thuộc phòng ban IT
SELECT HoTeN, Tuoi 
FROM NhanVien 
WHERE PhongBan = 'IT';

-- 5: Lấy danh sách nhân viên có tuổi > 25
SELECT * FROM NhanVien 
WHERE Tuoi > 25;

-- 6: Tìm tuổi lớn nhất trong từng phòng ban
SELECT PhongBan, MAX(Tuoi) AS tuoi_max
FROM NhanVien
GROUP BY PhongBan;

-- 7: Cập nhật phòng ban của Le Van C từ IT thành Marketing (sửa lỗi)
UPDATE NhanVien 
SET PhongBan = 'Marketing'
WHERE MANV = 3;

SELECT PhongBan 
FROM NhanVien 
WHERE MANV = 3;

-- 8: Xóa nhân viên có MANV = 2 (sửa lỗi)
DELETE FROM NhanVien 
WHERE MANV = 2;


