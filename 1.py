n = float(input("nhap so nam:"))

if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
    print(f"{n} là năm nhuận.")
else:
    print(f"{n} không phải là năm nhuận.")
