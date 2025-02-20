import sqlite3

# Kết nối đến SQLite (hoặc tạo file database nếu chưa tồn tại)
conn = sqlite3.connect("nhanvien.db")
cursor = conn.cursor()

# Xóa bảng nếu đã tồn tại
cursor.execute("DROP TABLE IF EXISTS NhanVien")

# Tạo bảng NhanVien
cursor.execute('''
    CREATE TABLE NhanVien (
        MaNV INTEGER PRIMARY KEY,
        HoTen TEXT,
        Tuoi INTEGER,
        PhongBan TEXT
    )
''')

# Chèn các bản ghi vào bảng
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
cursor.executemany("INSERT INTO NhanVien VALUES (?, ?, ?, ?)", nhan_vien_data)

# Truy vấn tất cả thông tin
cursor.execute("SELECT * FROM NhanVien")
print("\nDanh sách nhân viên:")
for row in cursor.fetchall():
    print(row)

# Truy vấn nhân viên phòng IT
cursor.execute("SELECT HoTen, Tuoi FROM NhanVien WHERE PhongBan = 'IT'")
print("\nNhân viên phòng IT:")
for row in cursor.fetchall():
    print(row)

# Tìm nhân viên có tuổi > 25
cursor.execute("SELECT * FROM NhanVien WHERE Tuoi > 25")
print("\nNhân viên trên 25 tuổi:")
for row in cursor.fetchall():
    print(row)

# Xác định nhân viên lớn tuổi nhất trong mỗi phòng ban
cursor.execute('''
    SELECT PhongBan, HoTen, Tuoi FROM NhanVien
    WHERE (PhongBan, Tuoi) IN (
        SELECT PhongBan, MAX(Tuoi) FROM NhanVien GROUP BY PhongBan
    )
''')
print("\nNhân viên lớn tuổi nhất mỗi phòng ban:")
for row in cursor.fetchall():
    print(row)

# Kiểm tra thông tin nhân viên trước khi cập nhật
cursor.execute("SELECT * FROM NhanVien WHERE HoTen = 'Le Van C'")
le_van_c = cursor.fetchall()
if le_van_c:
    cursor.execute("UPDATE NhanVien SET PhongBan = 'Marketing' WHERE MaNV = 3")
    print("\nCập nhật phòng ban cho nhân viên Le Van C thành công.")
else:
    print("\nKhông tìm thấy nhân viên Le Van C.")

# Xóa nhân viên có MaNV = 2
cursor.execute("DELETE FROM NhanVien WHERE MaNV = 2")
print("\nĐã xóa nhân viên có MaNV = 2.")

# Hiển thị số lượng nhân viên trong mỗi phòng ban
cursor.execute("SELECT PhongBan, COUNT(*) FROM NhanVien GROUP BY PhongBan")
print("\nSố nhân viên theo phòng ban:")
for row in cursor.fetchall():
    print(row)

# Lưu thay đổi và đóng kết nối
conn.commit()
conn.close()
