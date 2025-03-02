#bài 1:
n = int(input("nhập năm cần biết: "))
if n % 4 ==0 and n % 100 != 0:
    print(f"{n} là năm nhuận")
elif n % 400 == 0:
    print(f"{n} là năm nhuận")
else:
    print(f"{n} không là năm nhuận")


#bài 2:
import math
x = float(input("nhập tọa độ x của điểm M: "))
y = float(input("nhập tọa độ y của điểm M: "))
a = float(input("nhập tọa độ a của điểm I: "))
b = float(input("nhập tọa độ b của điểm I: "))
R = float(input("nhập bán kính R của đường tròn: "))
d = math.sqrt((x-a)**2+(y-b)**2)
if d <= R:
    print("True")
else:
    print("False")

#bài 3:
a = int(input("nhập độ dài cạnh a: "))
b = int(input("nhập độ dài cạnh b: "))
c = int(input("nhập độ dài cạnh c: "))
if a>0 and b>0 and c>0:
    if a**2 + b**2 == c**2:
        print("đây là tam giác vuông")
    elif a==b!=c or a==c!=b or b==c!=a:
        print("đây là tam giác cân")
    elif a**2 + b**2 == c**2 and a==b!=c or a==c!=b or b==c!=a:
        print("đây là tam giác vuông cân")
    elif a==b==c:
        print("đây là tam giác đều")
    elif a+b>c or a+c>b or b+c>a:
        print("đây là tam giác thường")
    else:
        print("đây không là tam giác")
else:
    print("đây không là tam giác")


#bài 4:
a = float(input("nhập a: "))
b = float(input("nhập b: "))
c = float(input("nhập c: "))
if a>=b and a>=c:
    print(f"{a} là số lớn nhất")
elif b>=a and b>=c:
    print(f"{b} là số lớn nhất")
else:
    print(f"{c} là số lớn nhất")

#bài5:
kitu = str(input("nhập kí tự: "))
if kitu == "u" or kitu == "e" or kitu== "o" or kitu == "a" or kitu =="i":
    print("đây là nguyên âm")
else:
    print("đây là phụ âm")

#bài6:
print("rạp chiếu phim ABC")
print("MENU")
print("1.phim tình cảm")
print("2.phim kinh dị")
print("3.phim hoạt hình")
print("4.phim hành động")
print("5.phim trinh thám")
print("6.phim siêu anh hùng")
luachon = int(input("vui lòng nhập số thứ tự lựa chọn của bạn: "))
if luachon == 1 :
    print("bạn đã chọn phim tình cảm")
elif luachon == 2:
    print("bạn đã chọn phim kinh dị")
elif luachon == 3:
    print("bạn đã chọn phim hoạt hình")
elif luachon == 4:
    print("bạn đã chọn phim hành động")
elif luachon == 5: 
    print("bạn đã chọn phim trinnh thám")
elif luachon == 6:
    print("bạn đã chọn phim siêu anh hùng")
else:
    print("lựa chọn không hợp lệ.vui lòng lựa chọn lại")



#bài8:
n = input("nhập điểm cần phân loại: ").upper()
if n == "A":
    print("đây là sinh viên loại xuất sắc")
elif n == "B":
    print("đây là sinh viên loại giỏi")
elif n == "C":
    print("đây là sinh viên loại khá")
elif n == "D":
    print("đây là sinh viên loại trung bình")
elif n == "E":
    print("đây là sinh viên lọai yếu")
elif n == "F":
    print("đây là sinh viên loại kém")
else:
    print("không hợp lệ. vui lòng nhập lại")


#bài9:
luong =float(input("nhập lương của bạn: "))
if luong < 7000000 :
    thue = 0.1
    luong_rong = luong - luong*thue
    print(f"thuế thu nhập là:{luong*thue}, lương ròng là:{luong_rong}")
elif luong >=7000000 and luong <15000000:
    thue = 0.2
    luong_rong = luong - luong*thue
    print(f"thuế thu nhập là:{luong*thue}, lương ròng là:{luong_rong}")
else: 
    thue = 0.3
    luong_rong = luong - luong*thue
    print(f"thuế thu nhập là:{luong*thue}, lương ròng là:{luong_rong}")


#bài 10:
thang = int(input("nhập vào tháng bạn muốn biết:"))
if thang == 1 :
    print("tháng 1 có 31 ngày")
elif thang == 2 :
    nam = int(input("vui lòng nhập năm:"))
    if nam % 4 == 0 and nam % 100 != 0:
        print(f"{nam} là năm nhuận.Tháng 2 có 29 ngày")
    elif nam % 400 == 0:
        print(f"{nam} là năm nhuận.Tháng 2 có 29 ngày")
    else:
        print(f"{nam} là năm không nhuận.Tháng 2 có 28 ngày")
elif thang == 3:
    print(f"tháng {thang} có 31 ngày")
elif thang == 4:
    print(f"tháng {thang} có 30 ngày")
elif thang == 5:
    print(f"tháng {thang} có 31 ngày")
elif thang == 6:
    print(f"tháng {thang} có 30 ngày")
elif thang == 7:
    print(f"tháng {thang} có 31 ngày")
elif thang == 8:
    print(f"tháng {thang} có 31 ngày")
elif thang ==9 :
    print(f"tháng {thang} có 30 ngày")
elif thang == 10 :
    print(f"tháng {thang} có 31 ngày")
elif thang == 11:
    print(f"tháng {thang} có 30 ngày")
elif thang == 12 :
    print(f"tháng {thang} có 31 ngày")
else:
    print("không hợp lệ. vui lòng nhập lại")


#bài 11 :
n = int(input("Nhập số nguyên có ba chữ số: "))
if 100 <= n <= 999:
    hang_tram = ["", "Một trăm", "Hai trăm", "Ba trăm", "Bốn trăm", "Năm trăm", 
                 "Sáu trăm", "Bảy trăm", "Tám trăm", "Chín trăm"]
    
    hang_chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", 
                 "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
    
    hang_don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

    tram = n // 100
    chuc = (n % 100) // 10
    don_vi = n % 10

    ket_qua = hang_tram[tram]

    if chuc == 0:
        if don_vi != 0:
            ket_qua += " lẻ " + hang_don_vi[don_vi]
    elif chuc == 1:
        if don_vi == 0:
            ket_qua += " mười"
        elif don_vi == 5:
            ket_qua += " mười lăm"
        else:
            ket_qua += " mười " + hang_don_vi[don_vi]
    else:
        ket_qua += " " + hang_chuc[chuc]
        if don_vi != 0:
            if don_vi == 1:
                ket_qua += " mốt"
            elif don_vi == 5:
                ket_qua += " lăm"
            else:
                ket_qua += " " + hang_don_vi[don_vi]
    print("Cách đọc:", ket_qua.strip())

else:
    print("Vui lòng nhập một số nguyên có đúng ba chữ số!")





#bài 12:
tnct = int(input("nhập thâm niên công tác: "))
if tnct >= 60:
    heso = 3.99
    luong = heso * 1350000
    print(f"lương của nhân viên là: {luong}")
elif tnct >= 36 and tnct < 60:
    heso = 3.66
    luong = heso * 1350000
    print(f"lương của nhân viên là: {luong}")
elif tnct >= 12 and tnct < 36:
    heso = 3.33
    luong = heso * 1350000
    print(f"lương của nhân viên là: {luong}")
else:
    heso = 2.34
    luong = heso *1350000
    print(f"lương của nhân viên là: {luong}")

#huyen
#1818
