thang = float(input("nhập tháng (1->12):  "))
if thang in [ 1,3,5,7,8,10,12] :
    print("tháng đó có 31 ngày")
elif thang in [ 4,6,9,11] :
    print("tháng đó có 30 ngày")
elif thang == 2:
    nam = float(input("nhập năm:  "))
    # Kiểm tra năm nhuận
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        print("tháng 2 có 29 ngày")
    else:
        print("tháng 2 có 28 ngày")
else :
    print("nhập lại tháng từ 1-> 12")
