#bai 3
a = float(input("nhap canh a : "))
b = float(input("nhap canh b : "))
c = float(input("nhap canh c : "))
if a + b > c and b + c > a and a + c > b :
    if  a == b == c:
            print("là tam giác đều")
    elif a == b or b == c or c == a :
        if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2 :
            print("là tam giác vuông cân")
        else :
            print("là tam giác cân")
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2 :
        print("là tam giác vuông")
    else :
        print("là tam giác thường")
else:
    print(" không phải là tam giác")

        