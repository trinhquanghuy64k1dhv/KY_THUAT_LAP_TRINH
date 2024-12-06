print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
import my_module

# Nhap so luong phan tu cua danh sach
n = int(input("Nhap so luong phan tu cua danh sach: "))

# Nhap gia tri cho danh sach
lst = []
for i in range(n):
    value = float(input(f"Nhap phan tu thu {i + 1}: "))
    lst.append(value)

# Su dung module đe sap xep và tim phan tu lon nhat
sorted_lst = my_module.sort_list(lst)
max_value = my_module.find_max(lst)

# Kết quả
print("Danh sach đa sap xep:", sorted_lst)
print("Phan tu lon nhat:", max_value)
