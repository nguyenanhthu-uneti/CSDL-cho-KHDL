import sqlite3


# Kết nối đến database : 

conn = sqlite3.connect("NhanVien.db")

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS NhanVien")
conn.commit()

#1.Tạo bảng nhân viên : 

cursor.execute('''
            CREATE TABLE IF NOT EXISTS NhanVien(
                MaNV INTEGER PRIMARY KEY ,
                HoTen TEXT NOT NULL , 
                Tuoi INTEGER ,
                PhongBan TEXT NOT NULL 
        )
''')

#2.Chèn dữ liệu vào bảng : 

Data = [
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


cursor.executemany("INSERT INTO NhanVien (MaNV, HoTen, Tuoi, PhongBan) VALUES(?,?,?,?)",Data)

conn.commit()


#3. Lấy toàn bộ thông tin nhân viên :
cursor.execute("SELECT * FROM NhanVien ")
alls = cursor.fetchall()
print('\nToàn bộ thông tin của Nhân Viên :')
for nv in alls  : 
    print(nv)

#4. Truy vấn HoTen và Tuoi của nhân viên trong phòng IT : 

cursor.execute("SELECT HoTen, Tuoi FROM NhanVien WHERE PhongBan = 'IT'")
rows = cursor.fetchall()
print('\nHoTen và Tuoi của nhân viên trong phòng IT :')
for row in rows:
    print(row)

#5. Tìm nhân viên có độ tuổi lớn hơn 25
cursor.execute("SELECT * FROM NhanVien WHERE Tuoi > 25")
tuoi = cursor.fetchall()
print('\nNhân viên có độ tuổi lớn hơn 25 : ')
for tuois in tuoi :
    print(tuois)

#6. NNhân viên lớn tuổi nhất của các PhongBan : 
cursor.execute('''
    SELECT PhongBan, HoTen, Tuoi
    FROM NhanVien n
    WHERE Tuoi = (
        SELECT MAX(Tuoi) 
        FROM NhanVien 
        WHERE PhongBan = n.PhongBan
    )
''')

PB = cursor.fetchall()

print("\nNhân viên lớn tuổi nhất của các phòng ban:")
for pb in PB:
    print(f"- Phòng ban: {pb[0]}, Nhân viên: {pb[1]}, Tuổi: {pb[2]}")
#7.Chuyển đổi thông tin PhongBan của nhân viên “Le Van C” sang “Marketing” 
# (có vấn đề gặp phải khi thực hiện chuyển đổi thông tin hay không? Nếu có, vấn đề đó là gì và hãy đề xuất biện pháp giải quyết).
cursor.execute("UPDATE NhanVien SET PhongBan = 'Marketing' WHERE MaNV = 3")
conn.commit()
cursor.execute("SELECT * FROM NhanVien ")
alls = cursor.fetchall()
print('\nToàn bộ thông tin của Nhân Viên sau khi chuyển đổi thông tin :  :')
for all in alls  : 
    print(all)
# Vấn đề : Vấn đề về dữ liệu không tồn tại : 
# Nếu MaNV = 3 không tồn tại trong bảng NhanVien, câu lệnh UPDATE vẫn chạy nhưng không có hàng nào bị thay đổi.
# Giải Pháp : Kiểm tra xem nhân viên có tồn tại trước khi cập nhật
cursor.execute("SELECT * FROM NhanVien WHERE MaNV = 3")
if cursor.fetchone():
    cursor.execute("UPDATE NhanVien SET PhongBan = 'Marketing' WHERE MaNV = 3")
    conn.commit()
    print("Cập nhật thành công!")
else:
    print("Không tìm thấy nhân viên có MaNV = 3!")


#8. Xóa nhân viên có “MaSV = 2” rồi cho biết mỗi phòng ban có bao nhiêu người 
cursor.execute("DELETE FROM NhanVien WHERE MaNV = 2")
conn.commit()
cursor.execute("SELECT * FROM NhanVien ")
print("\nThông tin sau khi bị xóa :")
xoa = cursor.fetchall()
for xoas in xoa :
    print(xoas)
# cho biết mỗi phong ban có bao nhiêu người :

print("\nSố nhân viên mỗi phòng ban:")
cursor.execute("SELECT PhongBan, COUNT(*) FROM NhanVien GROUP BY PhongBan")
for dem in cursor.fetchall():
    print(dem)



#9. Trình bày các bước kết nối đến SQLite trong Python và thực thi các câu lệnh trên bằng Python:
# Import thư viện SQLite : import sqlite3 
# Kết nối đến cơ sở dữ liệu : sqlite3.connect("ten_database.db") . Nếu SQL chưa tồn tại sẽ tự cập nhập file mới
# Tạo con trỏ (cursor) để thực thi câu lệnh SQL :  cursor = conn.cursor() 
# Thực thi các câu lệnh SQL : SELECT , FROM , UPDATE , WHERE , GROUP BY ,...

