print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("################")
import math
print("Giai phuong trinh ax^2+bx+c=0")
a=float(input("Nhap gia tri cua a la :"))
b=float(input("Nhap gia tri cua b la :"))
c=float(input("Nhap gia tri cua c la :"))

if(a==0):
    if(b==0):
        if(c==0):
            print(" Phuong trinh co vo so nghiem")
        else:
            print(" Phuong trinh vo nghiem")
    else:
        x= -c / b
        print(f"Phuong trinh co nghiem duy nhat: x = {x}")
else:
    delta= b**2-4*a*c
    if delta >0:
        x1 =(-b + math.sqrt(delta)) / (2*a)
        x2 =(-b - math.sqrt(delta)) / (2*a)
        print("Phuong trinh co hai nghiem phan biet")
        print(f"x1={x1}")
        print(f"x2={x2}")
    elif delta == 0:
        x=-b / (2*a)
        print(f" Phuong trinh co nghiep kep:x = {x}")
    else:
        print("Phuong trinh vo nghiem")
        
    
        
                
    
