DROP TABLE NhanVien;

CREATE TABLE NhanVien (
    MaNV INT PRIMARY KEY,
    HoTen VARCHAR(50),
    Tuoi INT,
    PhongBan VARCHAR(50)
);
INSERT INTO NhanVien (MaNV, HoTen, Tuoi, PhongBan)
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

#3.Lấy toàn bộ thông tin của nhân viên trong bảng NhanVien
SELECT * FROM NhanVien;

#4.Truy vấn HoTen và Tuoi của các nhân viên trong phòng IT
SELECT HoTen, Tuoi 
FROM NhanVien 
WHERE PhongBan = 'IT';

#5.Tìm nhân viên có độ tuổi lớn hơn 25
SELECT * 
FROM NhanVien 
WHERE Tuoi > 25;

#6.Cho biết nhân viên lớn tuổi nhất của mỗi PhongBan
SELECT PhongBan, HoTen, Tuoi
FROM NhanVien
WHERE Tuoi IN (
    SELECT MAX(Tuoi)
    FROM NhanVien
    GROUP BY PhongBan
);

#7.Chuyển đổi thông tin PhongBan của nhân viên Le Van C từ IT sang Marketing
SELECT * FROM NhanVien WHERE HoTen = 'Le Van C';
UPDATE NhanVien
SET PhongBan = 'Marketing'
WHERE MaNV = 3;


DELETE FROM NhanVien 
WHERE MaNV = 2;

SELECT PhongBan, COUNT(*) AS SoLuongNhanVien
FROM NhanVien
GROUP BY PhongBan;
---Không gặp vấn đề trong việc chuyển đổi thông tin 

#8.Xoá nhân viên có "MaSV=2" rồi cho biết mõi phong ban có bao nhiêu người
DELETE FROM NhanVien 
WHERE MaNV = 2;

SELECT PhongBan, COUNT(*) AS SoLuongNhanVien
FROM NhanVien
GROUP BY PhongBan;
DELETE FROM NhanVien 
WHERE MaNV = 2;
SELECT PhongBan, COUNT(*) AS SoLuongNhanVien
FROM NhanVien
GROUP BY PhongBan;

#9.Các bước kết nối sqllite trong python:
import sqlite3

# b1. Kết nối đến database
conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()

# b2. Tạo bảng
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY, 
                    name TEXT, age INTEGER, grade TEXT)''')

# b3. Chèn dữ liệu
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", 
               ("Nguyễn Văn A", 20, "A"))
conn.commit()

# b4. Truy vấn dữ liệu
cursor.execute("SELECT * FROM students")
print(cursor.fetchall())

# b5. Cập nhật dữ liệu
cursor.execute("UPDATE students SET grade = ? WHERE name = ?", ("B+", "Nguyễn Văn A"))
conn.commit()

# b6. Xóa dữ liệu
cursor.execute("DELETE FROM students WHERE name = ?", ("Nguyễn Văn A",))
conn.commit()
# b7. Đóng kết nối
conn.close()
