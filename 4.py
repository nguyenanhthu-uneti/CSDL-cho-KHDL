#bai 4
x = float(input("nhập số x:"))
y = float(input("nhập số y:"))
z = float(input("nhập số z:"))
if x >= y and x >= z :
    so_lon_nhat = x
elif y >= x and y >= z  :
    so_lon_nhat = y
else:
    so_lon_nhat = z
print("số lớn nhất trong ba số là : ", so_lon_nhat)