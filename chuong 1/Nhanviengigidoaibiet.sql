CREATE table NhanVien (
    MaNV INT PRIMARY key,
    HoTen VARCHAR(50),
    Tuoi INT,
    PhongBan VARCHAR(50)
);
insert into NhanVien (MaNV, HoTen, Tuoi, PhongBan) VALUES
    (1, 'Nguyen Van A',30,'Ke Toan'),
    (2, 'Tran Thi B',25,' Nhan Su'),
    (3, 'Le Van C', 28, 'IT'),
    (4, 'Pham Thi D', 32,'Ke Toan'),
    (5, 'Vu Van E',26,'IT'),
    (6, 'Nguyen Thi F',29,'Marketing'),
    (7, 'Le Thi G',27,'Nhan Su'),
    (8, 'Hoang Van H',35,'Ke Toan'),
    (9, 'Pham Van I',33,'Marketing'),
    (10, 'Tran Van J',24,'IT'),
    (11,'Dang Thi K',31,'Nhan Su'),
    (12, 'Nguyen Van L', 28,'Ke Toan'),
    (13, 'Tran Thi M',26,'Marketing'),
    (14, 'Pham Van N',30,'Nhan Su'),
    (15,'Hoang Thi O',27,'IT');
SELECT * from NhanVien
SELECT HoTen,Tuoi from NhanVien
SELECT * from NhanVien where Tuoi>25
SELECT PhongBan, HoTen, Tuoi FROM NhanVien WHERE Tuoi IN (
    SELECT MAX(Tuoi)
    FROM NhanVien
    GROUP BY PhongBan
);
UPDATE NhanVien SET PhongBan = 'Marketing' WHERE HoTen = 'Le Van C';
SELECT * FROM NhanVien WHERE HoTen = 'Le Van C';
DELETE FROM NhanVien WHERE MaNV = 2; 
SELECT PhongBan, COUNT(*) AS SoLuongNhanVien FROM NhanVien GROUP BY PhongBan;