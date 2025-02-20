import sqlite3

# Kết nối đến SQLite (tạo database nếu chưa có)
conn = sqlite3.connect("nhanvien.db")
cursor = conn.cursor()

# 1. Tạo bảng NhanVien
cursor.execute("""
CREATE TABLE IF NOT EXISTS NhanVien (
    MaNV INTEGER PRIMARY KEY,
    HoTen TEXT,
    Tuoi INTEGER,
    PhongBan TEXT
)
""")

# 2. Chèn dữ liệu vào bảng
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
conn.commit()

# 3. Lấy toàn bộ thông tin nhân viên
cursor.execute("SELECT * FROM NhanVien")
print("Danh sách nhân viên:", cursor.fetchall())

# 4. Truy vấn HoTen và Tuoi của nhân viên phòng IT
cursor.execute("SELECT HoTen, Tuoi FROM NhanVien WHERE PhongBan = 'IT'")
print("Nhân viên phòng IT:", cursor.fetchall())

# 5. Tìm nhân viên có độ tuổi lớn hơn 25
cursor.execute("SELECT * FROM NhanVien WHERE Tuoi > 25")
print("Nhân viên trên 25 tuổi:", cursor.fetchall())

# 6. Nhân viên lớn tuổi nhất của mỗi phòng ban
cursor.execute("""
    SELECT n1.PhongBan, n1.HoTen, n1.Tuoi
    FROM NhanVien n1
    JOIN (
        SELECT PhongBan, MAX(Tuoi) AS MaxTuoi FROM NhanVien GROUP BY PhongBan
    ) n2
    ON n1.PhongBan = n2.PhongBan AND n1.Tuoi = n2.MaxTuoi
""")
print("Nhân viên lớn tuổi nhất mỗi phòng ban:", cursor.fetchall())

# 7. Cập nhật phòng ban của "Le Van C" sang "Marketing"
cursor.execute("UPDATE NhanVien SET PhongBan = 'Marketing' WHERE MaNV = 3")
conn.commit()
print("Cập nhật phòng ban cho Le Van C thành công!")

# 8. Xóa nhân viên có MaNV = 2
cursor.execute("DELETE FROM NhanVien WHERE MaNV = 2")
conn.commit()
print("Đã xóa nhân viên có MaNV = 2")

# Đếm số lượng nhân viên theo từng phòng ban
cursor.execute("SELECT PhongBan, COUNT(*) FROM NhanVien GROUP BY PhongBan")
print("Số nhân viên mỗi phòng ban:", cursor.fetchall())

# Đóng kết nối
conn.close()
