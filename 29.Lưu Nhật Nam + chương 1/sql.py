import sqlite3
conn = sqlite3.connect("nhanvien.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS NhanVien (
        MaNV INTEGER PRIMARY KEY,
        HoTen TEXT,
        Tuoi INTEGER,
        PhongBan TEXT
    )
''')
conn.commit()

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
    (10, 'Tran Van J', 24, 'IT')
]
cursor.execute("DELETE FROM NhanVien")  # Xóa toàn bộ dữ liệu cũ
conn.commit()

cursor.executemany("INSERT INTO NhanVien VALUES (?, ?, ?, ?)", nhan_vien_data)
conn.commit()
##3
print("câu 3:")
cursor.execute("SELECT * FROM NhanVien")
for row in cursor.fetchall():
    print(row)
##4
print("câu 4:")
cursor.execute("SELECT HoTen, Tuoi FROM NhanVien WHERE PhongBan = 'IT'")
for row in cursor.fetchall():
    print(row)
##5
print("câu 5:")
cursor.execute("SELECT * FROM NhanVien WHERE Tuoi > 25")
for row in cursor.fetchall():
    print(row)
##6
print("câu 6:")
cursor.execute('''
    SELECT PhongBan, HoTen, Tuoi 
    FROM NhanVien 
    WHERE (PhongBan, Tuoi) IN (
        SELECT PhongBan, MAX(Tuoi) 
        FROM NhanVien 
        GROUP BY PhongBan
    )
''')
for row in cursor.fetchall():
    print(row)
##7
print("câu 7 :")
cursor.execute("SELECT * FROM NhanVien WHERE HoTen = 'Le Van C'")
results = cursor.fetchall()

if len(results) == 1:
    cursor.execute("UPDATE NhanVien SET PhongBan = 'Marketing' WHERE HoTen = 'Le Van C'")
    conn.commit()
    print("Cập nhật thành công!")
elif len(results) > 1:
    print("Có nhiều nhân viên tên 'Le Van C', vui lòng chọn MaNV chính xác!")
else:
    print("Không tìm thấy nhân viên 'Le Van C'!")


##8
cursor.execute("DELETE FROM NhanVien WHERE MaNV = 2")
conn.commit()

print("câu 8:")
cursor.execute("SELECT PhongBan, COUNT(*) FROM NhanVien GROUP BY PhongBan")
for row in cursor.fetchall():
    print(row)
