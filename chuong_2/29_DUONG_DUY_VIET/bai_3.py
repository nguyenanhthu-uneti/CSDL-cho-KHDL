a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

if a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("a, b, c là ba cạnh của tam giác đều")
    elif a == b or b == c or a == c:
        if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
            print("a, b, c là ba cạnh của tam giác vuông cân")
        else:
            print("a, b, c là ba cạnh của tam giác cân")
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
        print("a, b, c là ba cạnh của tam giác vuông")
    else:
        print("a, b, c là ba cạnh của tam giác thường")
else:
    print("a, b, c không phải ba cạnh của tam giác")

