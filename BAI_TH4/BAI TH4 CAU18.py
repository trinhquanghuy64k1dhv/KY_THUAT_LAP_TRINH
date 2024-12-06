print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
# Nhap so nguyen duong n
n = int(input("Nhap so n: "))

# Khoi tao danh sach đe luu cac so Fibonacci
fibonacci_list = []

# Khoi tao hai so đau tien cua day Fibonacci
a, b = 0, 1

# Tao day Fibonacci nho hon n
while a < n:
    fibonacci_list.append(a)
    a, b = b, a + b

# In danh sach cac so Fibonacci nho hon n
print(f"Cac so Fibonacci nho hon {n} la:")
print(fibonacci_list)
