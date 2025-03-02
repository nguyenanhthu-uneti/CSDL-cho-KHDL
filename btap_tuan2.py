#Bai1
n = int(input("Nhap vao nam: "))
if n % 4 == 0 and n % 100 != 0:
    print("la nam nhuan")
elif n % 400 == 0:
    print("la nam nhuan")
else:
    print("khong la nam nhuan")


#Bai2
x = float(input("Nhập x: "))
y = float(input("Nhập y: "))
a = float(input("Nhập tọa độ tâm a: "))
b = float(input("Nhập tọa độ tâm b: "))
R = float(input("Nhập bán kính R: "))

if ((x - a)**2 + (y - b)**2) <= R**2:
    print(True)
else:
    print(False)




#Bai3
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Tam giác đều")
    elif a == b or a == c or b == c:
        print("Tam giác cân")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Tam giác vuông")
    else:
        print("Tam giác thường")
else:
    print("Không phải tam giác")


#Bai4
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))

print("Số lớn nhất là:", max(a, b, c))

#Bai5
a = input("Nhập ký tự: ")

if a.isalpha():
    if a in "ueoaiUEOAI":
        print("Ký tự là nguyên âm")
    else:
        print("Ký tự là phụ âm")
else:
    print("Không phải chữ cái")


#Bai6
print("Menu phim rạp ABC:")
print("1. Phim hành động")
print("2. Phim tình cảm")
print("3. Phim hoạt hình")
print("4. Phim kinh dị")

choice = int(input("Nhập lựa chọn: "))
if choice == 1:
    print("Bạn đã chọn phim hành động")
elif choice == 2:
    print("Bạn đã chọn phim tình cảm")
elif choice == 3:
    print("Bạn đã chọn phim hoạt hình")
elif choice == 4:
    print("Bạn đã chọn phim kinh dị")
else:
    print("Lựa chọn không hợp lệ")


#Bai8
diem = input("Nhập điểm của sinh viên (A-F): ")

if diem == "A":
    print("Sinh viên xuất sắc")
elif diem == "B":
    print("Sinh viên loại giỏi")
elif diem == "C":
    print("Sinh viên loại khá")
elif diem == "D":
    print("Sinh viên loại trung bình")
elif diem == "E":
    print("Sinh viên loại yếu")
elif diem == "F":
    print("Sinh viên xếp loại kém")
else:
    print("Điểm không hợp lệ")

#Bai9
luong = float(input("Nhập lương: "))
if luong > 15:
    tax = luong * 0.3
elif 7 <= luong <= 15:
    tax = luong * 0.2
else:
    tax = luong * 0.1

net_luong = luong - tax
print(f"Thuế thu nhập: {tax} triệu")
print(f"Lương thực nhận: {net_luong} triệu")

#Bai10
thang = int(input("Nhập tháng: "))

if thang in [1, 3, 5, 7, 8, 10, 12]:
    print("Tháng có 31 ngày")
elif thang in [4, 6, 9, 11]:
    print("Tháng có 30 ngày")
elif thang == 2:
    print("Tháng có 28 hoặc 29 ngày")
else:
    print("Tháng không hợp lệ")


#Bai11
so = int(input("Nhập số nguyên có 3 chữ số: "))
chu = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
if 100 <= so <= 999:
    hang_tram = so // 100
    hang_chuc = (so % 100) // 10
    hang_dv = so % 10

    print(f"{chu[hang_tram]} trăm", end=" ")
    if hang_chuc == 0 and hang_dv != 0:
        print("lẻ", chu[hang_dv])
    elif hang_chuc == 1:
        print("mười", chu[hang_dv])
    else:
        print(chu[hang_chuc], "mươi", chu[hang_dv])
else:
    print("Số không hợp lệ")

#Bai12
thamnien = int(input("Nhập thâm niên công tác (tháng): "))
luong_cb = 1350000

if thamnien < 12:
    heso = 2.34
elif thamnien <= 36:
    heso = 3.00
elif thamnien <= 60:
    heso = 3.66
else:
    heso = 3.99

luong = heso * luong_cb
print(f"Lương nhân viên: {luong} đồng")