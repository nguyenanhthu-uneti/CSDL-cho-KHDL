x = float(input("nhap x :"))
y = float(input("nhap y :"))
a = float(input("nhap a :"))
b = float(input("nhap b :"))
r = float(input("nhap r :"))
MI = ((x-a)**2+(y-b)**2)**1/2
if MI <= r :
    print(True)
else:
    print(False)
