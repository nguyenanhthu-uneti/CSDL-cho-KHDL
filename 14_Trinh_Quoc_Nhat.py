#Bai3   x=3,fx=0.32
x = float(input( "nhap vao x: "))
fx = ((-x+(x**2+4)**(1/2) ))/((x**4+1)**(1/7))
print(f" gia tri la {fx:.2f}")


#Bai4   a=20,c=293.15
a = float(input("nhap vao nhiet do C: "))
k = a + 273.15
print(f"nhiet do k la: {k}")



#Bai6  a=1,b=2,c=3, pt vo nghiem
import math
a = float(input("Nhap a: "))
b = float(input( "Nhap b: "))
c = float(input("Nhap c: "))
denta= b**2-4*a*c 
if a !=0:
    if denta >0:
        print("phuong trinh co hai nghiem phan biet")
        ("x1" , (-b-math.sqrt (denta)/2*a))
        ("x2", (-b+math.sqrt (denta) /2*a)) 
        print(f"x1={X1:.2f}")
        print(f"x2={x2:.2f}")
    elif denta ==0:
        print("phuong trinh co nghien kep")
    elif denta <0:
        print("phuong trinh vo nghiem")
elif a == 0:
    print("pt co nghiem x", -b/c)
    
    
    
#Bai7 h=3,v=7.67
h = float (input("nhap vao do cao: "))
v=(2*9.8*h)**(1/2)
print(f"van toc la: {v:.2f}")
    
    
#Bai9 x=5,f=1.59
import math
x = float (input ("nhap x: "))
f = math. log(x,4)+math. log(2,x)
print(f" ket qua {f:.2f}")

    
    
 #Bai10 x=12,y=2,f=-0.03
import math
x = float(input( "nhap x: "))
y = float (input ("nhap y: "))
f = math. sin(x)/ (((2*x+y)/math.cos (x) )-(x**y)/(x-y))
print (f" ket qua {f:.2f}")
   
