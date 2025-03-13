create table Nhanvien(
	MaNV int primary key,
	HoTen Varchar(20),
	Tuoi int,
	PhongBan varchar(50)
);
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

SELECT * FROM NhanVien;



--câu 3
SELECT Tuoi,PhongBan
FROM NhanVien;


--câu 4 
SELECT HoTen, Tuoi 
FROM NhanVien
WHERE PhongBan = 'IT';

--câu 5
SELECT * FROM NhanVien
WHERE Tuoi > 25;

--câu6
Select PhongBan,Max(Tuoi) as Tuoi from Nhanvien
group by (PhongBan)

--câu 7 
update Nhanvien
set PhongBan= 'Marketing'
where HoTen= 'Le Van C';

--không có vấn đề gì khi chuyển đổi thông tin

SELECT * FROM NhanVien;

--câu 8 
delete from Nhanvien
Where MaNV = 2

SELECT * FROM NhanVien;

--Dem  so nhan vien moi phong
Select PhongBan,count(PhongBan) as SoNhanVien from Nhanvien
group by PhongBan
