print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")

# Nhap so nguyen duong n
n = int(input("Nhap so n: "))
print(f"Cac so nguyen duong nho hon {n} co tong cac uoc lon hon chinh no la:")

# Ham tinh tong cac uoc cua mot so
def sum_of_divisors(x):
    total = 0
    for i in range(1, x):
        if x % i == 0:
            total += i
    return total

# Duyet qua cac so tu 1 đen n-1
for number in range(1, n):
    if sum_of_divisors(number) > number:
        print(number)
