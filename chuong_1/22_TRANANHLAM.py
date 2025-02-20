import sqlite3

# Bước 1: Kết nối đến cơ sở dữ liệu
conn = sqlite3.connect('nhanvien.db')
cursor = conn.cursor()

# 1. Lấy toàn bộ thông tin của nhân viên
cursor.execute("SELECT * FROM NhanVien")
all_data = cursor.fetchall()
print("Toàn bộ thông tin nhân viên:")
for row in all_data:
    print(row)

# 2. Truy vấn HoTen và Tuoi của các nhân viên trong phòng IT
cursor.execute("SELECT HoTen, Tuoi FROM NhanVien WHERE PhongBan = 'IT'")
it_employees = cursor.fetchall()
print("\nNhân viên trong phòng IT:")
for row in it_employees:
    print(row)

# 3. Tìm nhân viên có độ tuổi lớn hơn 25
cursor.execute("SELECT * FROM NhanVien WHERE Tuoi > 25")
older_than_25 = cursor.fetchall()
print("\nNhân viên có độ tuổi lớn hơn 25:")
for row in older_than_25:
    print(row)

# 4. Nhân viên lớn tuổi nhất của các phòng ban
cursor.execute("SELECT PhongBan, MAX(Tuoi) AS TuoiMax FROM NhanVien GROUP BY PhongBan")
oldest_in_departments = cursor.fetchall()
print("\nNhân viên lớn tuổi nhất của các phòng ban:")
for row in oldest_in_departments:
    print(row)

# 5. Cập nhật phòng ban của nhân viên 'Le Van C' sang 'Marketing'
cursor.execute("UPDATE NhanVien SET PhongBan = 'Marketing' WHERE HoTen = 'Le Van C'")
conn.commit()  # Lưu thay đổi

# Kiểm tra lại
cursor.execute("SELECT * FROM NhanVien WHERE HoTen = 'Le Van C'")
updated_employee = cursor.fetchall()
print("\nThông tin nhân viên 'Le Van C' sau khi cập nhật:")
for row in updated_employee:
    print(row)

# 6. Xóa nhân viên có MaNV = 2 và đếm số lượng nhân viên theo phòng ban
cursor.execute("DELETE FROM NhanVien WHERE MaNV = 2")
conn.commit()  # Lưu thay đổi

cursor.execute("SELECT PhongBan, COUNT(*) AS SoLuongNhanVien FROM NhanVien GROUP BY PhongBan")
employee_count = cursor.fetchall()
print("\nSố lượng nhân viên theo phòng ban:")
for row in employee_count:
    print(row)

# Đóng kết nối
conn.close()
