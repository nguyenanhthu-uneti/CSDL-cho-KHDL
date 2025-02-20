-- 15-22174600050 -Từ Tất Duy -DHKL16A2HN - Chương 1
-- Xóa bảng "NhanVien" nếu tồn tại
DROP TABLE IF EXISTS NhanVien;

-- Tạo bảng "NhanVien"
CREATE TABLE NhanVien (
    MaNV INT PRIMARY KEY,
    HoTen VARCHAR(50),
    Tuoi INT,
    PhongBan VARCHAR(50)
);

-- Chèn các bản ghi nhân viên
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

-- Truy vấn tất cả thông tin từ bảng "NhanVien"
SELECT * FROM NhanVien;

-- Truy vấn tên và tuổi của các nhân viên trong phòng IT
SELECT HoTen, Tuoi FROM NhanVien WHERE PhongBan = 'IT';

-- Tìm các nhân viên lớn hơn 25 tuổi
SELECT * FROM NhanVien WHERE Tuoi > 25;

-- Xác định nhân viên lớn tuổi nhất trong mỗi phòng ban
SELECT PhongBan, HoTen, MAX(Tuoi) AS Tuoi
FROM NhanVien
GROUP BY PhongBan, HoTen
ORDER BY PhongBan;

-- Thay đổi thông tin phòng ban của nhân viên "Le Van C" sang "Marketing"
--Có nhiều nhân viên cùng tên "Le Van C", dẫn đến cập nhật nhầm dữ liệu.
--Nhập sai thông tin (ví dụ, viết thiếu dấu hoặc sai chính tả trong tên).
--Không có nhân viên nào tên "Le Van C", dẫn đến không có bản ghi nào được cập nhật.
--Cách giải quyết:

--Dùng MaNV (khóa chính) để xác định chính xác nhân viên cần cập nhật.
--Kiểm tra số bản ghi bị ảnh hưởng bằng SELECT trước khi UPDATE.
-- Xóa nhân viên có MaNV = 2
-- Kiểm tra thông tin nhân viên trước khi cập nhật
SELECT * FROM NhanVien WHERE HoTen = 'Le Van C';

-- Nếu có nhiều người cùng tên, xác định MaNV cụ thể, ví dụ MaNV = 3
UPDATE NhanVien 
SET PhongBan = 'Marketing' 
WHERE MaNV = 3; -- Chỉ cập nhật đúng nhân viên cần thiết


-- Hiển thị số lượng nhân viên trong mỗi phòng ban
SELECT PhongBan, COUNT(*) AS SoNhanVien
FROM NhanVien
GROUP BY PhongBan;

