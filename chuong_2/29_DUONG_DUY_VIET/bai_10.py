
thang = int(input("Nhập tên tháng : "))
if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
    print("Tháng này có 31 ngày.")
elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
    print("Tháng này có 30 ngày.")
elif thang == 2:
    nam = int(input("Nhập năm : "))
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        print("Tháng 2 có 29 ngày (năm nhuận).")
    else:
        print("Tháng 2 có 28 ngày.")
else:
    print("Tên tháng không hợp lệ.")
