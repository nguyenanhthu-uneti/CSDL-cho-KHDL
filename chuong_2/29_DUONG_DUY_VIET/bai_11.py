tram = int(input("nhap hang tram: "))
chuc = int(input("nhap hang chuc: "))
donvi = int(input("nhap hang don vi: "))
if tram!=0 and chuc!=0 and donvi!=0:
    print(f"{tram} tram {chuc} muoi {donvi}")
elif tram!=0 and chuc==0 and donvi!=0:
    print(f"{tram} tram linh {donvi}")
elif tram!=0 and chuc==0 and donvi==0:
    print(f"{tram} tram ")
elif tram!=0 and chuc==1 and donvi!=0:
    print(f"{tram} tram muoi {donvi}")
elif tram!=0 and chuc==1 and donvi==0:
    print(f"{tram} tram muoi")
elif tram!=0 and chuc!=0 and donvi==0:
    print(f"{tram} tram {chuc} muoi")

elif tram==0 and chuc!=0 and donvi!=0:
    print(f"{chuc} muoi {donvi}")
elif tram!=0 and chuc==0 and donvi!=0:
    print(f"{donvi}")
elif tram==0 and chuc==1 and donvi!=0:
    print(f"muoi {donvi}")
elif tram==0 and chuc==1 and donvi==0:
    print(f"muoi")
elif tram==0 and chuc==0 and donvi==0:
    print(f"khong")





