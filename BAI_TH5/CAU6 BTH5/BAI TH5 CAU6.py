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

# Su dung module de sap xep va tim phan tu lon nhat va nho nhat
sorted_lst = my_module.sort_list(lst)
max_value = my_module.find_max(lst)
min_value = sorted_lst[0]  # Phan tu nho nhat la phan tu dau tien sau khi sap xep

# Tim vi tri cua phan tu lon nhat va nho nhat
max_index = lst.index(max_value) + 1  # Chuyen sang chi so tu 1
min_index = lst.index(min_value) + 1  # Chuyen sang chi so tu 1

# Ket qua
print("Danh sach da sap xep:", sorted_lst)
print("Phan tu lon nhat:", max_value, ", Vi tri:", max_index)
print("Phan tu nho nhat:", min_value, ", Vi tri:", min_index)
