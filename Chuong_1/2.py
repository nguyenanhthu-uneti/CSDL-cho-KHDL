#Câu1 và Câu 2 
import sqlite3

# Kết nối đến database (hoặc tạo mới nếu chưa tồn tại)
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Xóa bảng NhanVien nếu đã tồn tại
cursor.execute("DROP TABLE IF EXISTS NhanVien")

# Tạo bảng NhanVien mới
cursor.execute("""
CREATE TABLE IF NOT EXISTS NhanVien (
    MaNV INT PRIMARY KEY,
    HoTen VARCHAR(50),
    Tuoi INT,
    PhongBan VARCHAR(50)
);
""")

# Dữ liệu cần chèn vào bảng
nhan_vien_data = [
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
]

# Chèn dữ liệu vào bảng
cursor.executemany("INSERT INTO NhanVien (MaNV, HoTen, Tuoi, PhongBan) VALUES (?, ?, ?, ?)", nhan_vien_data)

# Lưu thay đổi
conn.commit()

# Hiển thị tất cả dữ liệu trong bảng NhanVien
cursor.execute("SELECT * FROM NhanVien")
nhanviens = cursor.fetchall()

# Hiển thị kết quả
print("\nDanh sách nhân viên:")
for nhanvien in nhanviens:
    print(f"Mã NV: {nhanvien[0]}, Họ tên: {nhanvien[1]}, Tuổi: {nhanvien[2]}, Phòng ban: {nhanvien[3]}")

# Đóng kết nối
conn.close()

# Câu 3 Lấy toàn bộ thông tin của nhân viên trong bảng NhanVien 
import sqlite3

# Kết nối đến database (hoặc tạo mới nếu chưa tồn tại)
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Lấy toàn bộ thông tin của nhân viên trong bảng NhanVien
cursor.execute("SELECT * FROM NhanVien")
nhanviens = cursor.fetchall()

# Hiển thị kết quả
print("\nDanh sách toàn bộ nhân viên:")
for nhanvien in nhanviens:
    print(f"Mã NV: {nhanvien[0]}, Họ tên: {nhanvien[1]}, Tuổi: {nhanvien[2]}, Phòng ban: {nhanvien[3]}")

# Đóng kết nối
conn.close()

#Câu 4 Truy vấn Hoten và Tuoi của các nhân viên trong phòng IT
import sqlite3

# Kết nối đến database (hoặc tạo mới nếu chưa tồn tại)
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Truy vấn Họ tên và Tuổi của các nhân viên trong phòng IT
cursor.execute("SELECT HoTen, Tuoi FROM NhanVien WHERE PhongBan = 'IT'")
nhanviens_it = cursor.fetchall()

# Hiển thị kết quả
print("\nDanh sách nhân viên phòng IT:")
for nhanvien in nhanviens_it:
    print(f"Họ tên: {nhanvien[0]}, Tuổi: {nhanvien[1]}")

# Đóng kết nối
conn.close()

#Câu5 Tìm nhân viên có độ tuổi lớn hơn 25 
import sqlite3

# Kết nối đến database (hoặc tạo mới nếu chưa tồn tại)
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Truy vấn các nhân viên có độ tuổi lớn hơn 25
cursor.execute("SELECT * FROM NhanVien WHERE Tuoi > 25")
nhanviens = cursor.fetchall()

# Hiển thị kết quả
print("\nDanh sách nhân viên có độ tuổi lớn hơn 25:")
for nhanvien in nhanviens:
    print(f"Mã NV: {nhanvien[0]}, Họ tên: {nhanvien[1]}, Tuổi: {nhanvien[2]}, Phòng ban: {nhanvien[3]}")

# Đóng kết nối
conn.close()

#Câu6 Cho biết nhân viên  lớn tuổi nhất của các PhongBan 
import sqlite3

# Kết nối đến database (hoặc tạo mới nếu chưa tồn tại)
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Truy vấn nhân viên lớn tuổi nhất trong từng phòng ban
cursor.execute("""
SELECT NhanVien.PhongBan, NhanVien.HoTen, NhanVien.Tuoi
FROM NhanVien
INNER JOIN (
    SELECT PhongBan, MAX(Tuoi) AS MaxTuoi
    FROM NhanVien
    GROUP BY PhongBan
) AS MaxAge ON NhanVien.PhongBan = MaxAge.PhongBan AND NhanVien.Tuoi = MaxAge.MaxTuoi;
""")
nhanviens_luatoi_nhat = cursor.fetchall()

# Hiển thị kết quả
print("\nNhân viên lớn tuổi nhất của các phòng ban:")
for nhanvien in nhanviens_luatoi_nhat:
    print(f"Phòng ban: {nhanvien[0]}, Họ tên: {nhanvien[1]}, Tuổi: {nhanvien[2]}")

# Đóng kết nối
conn.close()

#Câu7 
import sqlite3

# Kết nối đến database (hoặc tạo mới nếu chưa tồn tại)
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Cập nhật phòng ban của nhân viên "Le Van C" từ "IT" sang "Marketing"
cursor.execute("""
UPDATE NhanVien
SET PhongBan = 'Marketing'
WHERE HoTen = 'Le Van C' AND PhongBan = 'IT';
""")

# Lưu thay đổi
conn.commit()

# Hiển thị thông tin đã cập nhật
cursor.execute("SELECT * FROM NhanVien WHERE HoTen = 'Le Van C'")
nhanvien = cursor.fetchone()

print("\nThông tin đã cập nhật:")
print(f"Mã NV: {nhanvien[0]}, Họ tên: {nhanvien[1]}, Tuổi: {nhanvien[2]}, Phòng ban: {nhanvien[3]}")

# Đóng kết nối
conn.close()

#Câu 8 : xoá nhân viên có "MaSV = 2" rồi cho biết mỗi phòng ban có bao nhiêu người
import sqlite3

# Kết nối đến database (hoặc tạo mới nếu chưa tồn tại)
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Xóa nhân viên có MaNV = 2
cursor.execute("DELETE FROM NhanVien WHERE MaNV = 2")

# Lưu thay đổi
conn.commit()

# Đếm số lượng nhân viên theo phòng ban
cursor.execute("SELECT PhongBan, COUNT(*) AS SoLuongNhanVien FROM NhanVien GROUP BY PhongBan")
result = cursor.fetchall()

# Hiển thị kết quả
print("\nSố lượng nhân viên theo mỗi phòng ban:")
for row in result:
    print(f"Phòng ban: {row[0]}, Số lượng nhân viên: {row[1]}")

# Đóng kết nối
conn.close()
# Câu 9 
#Bước 1: Import thư viện SQLite
#Bước 2: Kết nối đến cơ sở dữ liệu
#Bước 3: Tạo bảng
#Bước 4: Chèn dữ liệu vào bảng
#Bước 5: Truy vấn dữ liệu
#Bước 6: Cập nhật dữ liệu
#Bước 7: Xóa dữ liệu
#Bước 8: Thống kê số nhân viên theo phòng ban
#Bước 9: Đóng kết nối