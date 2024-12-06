print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
# Nhap chuoi cac so nhi phan tu ban phim
input_string = input("Nhap cac so nhi phan, cach nhau boi dau phay: ")

# Tach chuoi thanh danh sach cac so nhi phan
binary_numbers = input_string.split(",")

# In ra cac so nhi phan
print("Cac gia tri đuoc nhap:")
for binary in binary_numbers:
    print(binary)
