print("Sinh vien Trinh Quang Huy")
print(" MSSV:235752021610016")
print("###################")
"Chuong trinh tao mot may tinh don gian co the cong, tru, nhan va chia "
#Ham cong 2 so
def add (x,y):
    return x+y
#Ham tru 2 so
def subtract(x,y):
    return x-y
#Ham nhan 2 so
def multipli(x,y):
    return x*y
#Ham chia 2 so
def divide(x,y):
    return x/y
print("Chon thao tac")
print("1.Add")
print("2.Subtract")
print("3.Multipli")
print("4.Divide")

#Lay y kien dong gop tu nguoi dung
choise=input("Enter choise (1/2/3/4):")
num1=int(input("Enter first number"))
num2=int(input("Enter second number:"))

if choise=='1':
    print(num1,"+",num2,"=", add(num1, num2))
elif choise=='2':
    print(num1,"-",num2,"=", subtract(num1, num2))
elif choise=='3':
    print(num1,"*",num2,"=", multipli(num1,num2))
elif choise=='4':
    print(num1,"/",num2,"=", divide(numl, num2))
else:
    print("Invalid input")
