print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
a, b = 1, 2
total = 0 # Bien de luu tong cac so fibonacci chia het cho 2
print(a,end=" ") # In so dau tien cua day Fibonacci(a=1),cach nhau bang dau cach
while (a <=4000000-1): #Vong lap chay den khi a nho hon hoac bang 4000000
    if a % 2 == 0: # Kiem tra neu a chia het cho 2
        total += a # cong gia tri cua a vao total
    a, b = b, a+b
    print(a,end=" ") # In ra tung dong va cach nhau mot khoang trang
print("\n sum of prine numbers term in fibonacci series: ",total)  #Tong cac so hang trong day fibonacci  
