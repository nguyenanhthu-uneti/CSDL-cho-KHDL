import sqlite3

# Kết nối đến cơ sở dữ liệu (tạo mới nếu chưa tồn tại)
conn = sqlite3.connect('nhanvien.db')

# Tạo con trỏ để thực hiện các thao tác
cursor = conn.cursor()

# 1. Xóa bảng nếu đã tồn tại (tránh lỗi trùng lặp)
cursor.execute('DROP TABLE IF EXISTS NhanVien')

# 2. Tạo bảng NhanVien
cursor.execute('''
    CREATE TABLE NhanVien (
        MaNV INTEGER PRIMARY KEY,
        HoTen TEXT,
        Tuoi INTEGER,
        PhongBan TEXT
    )
''')

# 3. Dữ liệu cần thêm
nhan_vien = [
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

# 4. Chèn dữ liệu với INSERT OR REPLACE để tránh trùng lặp
cursor.executemany('''
    INSERT OR REPLACE INTO NhanVien (MaNV, HoTen, Tuoi, PhongBan) 
    VALUES (?, ?, ?, ?)
''', nhan_vien)

# Lưu thay đổi
conn.commit()

# 5. Truy vấn và in ra toàn bộ dữ liệu trong bảng NhanVien
cursor.execute('SELECT * FROM NhanVien')
rows = cursor.fetchall()

print("Toàn bộ thông tin nhân viên:")
for row in rows:
    print(row)

# 6. Truy vấn HoTen và Tuoi của nhân viên trong phòng IT
cursor.execute('SELECT HoTen, Tuoi FROM NhanVien WHERE PhongBan = ?', ('IT',))
rows = cursor.fetchall()

print("\nNhân viên phòng IT:")
for row in rows:
    print(row)

# 7. Tìm nhân viên có độ tuổi lớn hơn 25
cursor.execute('SELECT * FROM NhanVien WHERE Tuoi > 25')
rows = cursor.fetchall()

print("\nNhân viên có độ tuổi lớn hơn 25:")
for row in rows:
    print(row)

# 8. Nhân viên lớn tuổi nhất của mỗi PhongBan
cursor.execute('''
    SELECT PhongBan, HoTen, MAX(Tuoi) AS Tuoi 
    FROM NhanVien 
    GROUP BY PhongBan
''')
rows = cursor.fetchall()

print("\nNhân viên lớn tuổi nhất trong mỗi phòng ban:")
for row in rows:
    print(row)

# 9. Chuyển đổi PhongBan của Le Van C sang Marketing
cursor.execute('''
    UPDATE NhanVien 
    SET PhongBan = ? 
    WHERE HoTen = ?
''', ('Marketing', 'Le Van C'))
conn.commit()

# 10. Xóa nhân viên có MaNV = 2
cursor.execute('DELETE FROM NhanVien WHERE MaNV = ?', (2,))
conn.commit()

# Đếm số lượng nhân viên trong mỗi phòng ban
cursor.execute('''
    SELECT PhongBan, COUNT(*) AS SoLuong 
    FROM NhanVien 
    GROUP BY PhongBan
''')
rows = cursor.fetchall()

print("\nSố lượng nhân viên trong mỗi phòng ban sau khi xóa MaNV=2:")
for row in rows:
    print(row)

# Đóng con trỏ và kết nối
cursor.close()
conn.close() 
