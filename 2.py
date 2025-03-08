#bai 2
x = float(input("nhap x:"))
y = float(input("Nhap y:"))
a = float(input("nhap a:"))
b = float(input("nhap b:"))
r = float(input("nhap r:"))
khoang_cach = ((x-a)**2 + (y-b)**2)**(1/2)
if khoang_cach <= r**2:
    print("True-diem M(x,y) nam trong hoac tren duong tron ")
else:
    print("False-diem M(x,y) nam ngoai duong tron")
print(khoang_cach)