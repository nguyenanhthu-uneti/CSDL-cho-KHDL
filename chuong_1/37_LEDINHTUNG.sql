-- Lê Đình Tùng - 22174600004

create database Ex
use Ex -- sử dụng csdl Ex

-- 1. Tạo bảng
create table NhanVien(
	MaNV int primary key,
	HoTen varchar(50),
	Tuoi int,
	PhongBan varchar(50))

-- 2. Chèn các bản ghi vào bảng
insert into NhanVien(MaNV, HoTen, Tuoi, PhongBan)
values
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
	(15, 'Hoang Thi O', 27, 'IT')

-- 3. Lấy toàn bộ thông tin của nhân viên trong bảng nhân viên
select * from NhanVien

-- 4. truy vấn Ho Ten và Tuoi của các nhan vien trong phong IT
select HoTen, Tuoi from NhanVien
where (PhongBan = 'IT')

-- 5. Tìm nhân viên có độ tuổi > 25
select * From NhanVien
where (Tuoi >25)

-- 6. Cho biết nhân viên lớn tuổi nhất các phòng ban
select PhongBan, HoTen, Tuoi from NhanVien
where Tuoi in (
	select max(Tuoi) from NhanVien group by PhongBan)
		
-- liệt kê những nhân viên trong tên có từ 'Nguyen'
select HoTen, Tuoi, PhongBan from NhanVien
where HoTen like 'Nguyen%'

---7. Chuyen doi thong tin PhongBan cua nhan vien &quot;Le Van C&quot; sang &quot;Marketing&quot;
UPDATE NhanVien
SET PhongBan = 'Marketing'
WHERE HoTen = 'Le Van C';
--- kiem tra
SELECT * FROM NhanVien
WHERE HoTen = 'Le Van C';

update NhanVien set PhongBan = 'Marketing'
where HoTen = 'Le Van C' and PhongBan = 'IT'

-- 8. Xóa nhân viên có 'MaNV = 2' rồi cho biết mỗi phòng ban có bao nhiêu người
delete from NhanVien
where MaNV = 2;
-- đếm số nhân viên sau khi xóa
select PhongBan, count(*) as SoLuongNhanVien
from NhanVien
group by PhongBan;






drop table NhanVien