print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
# main.py
import search_utils

# Nhap so luong phan tu trong danh sach
n = int(input("Nhap so luong phan tu trong danh sach: "))

# Nhap cac phan tu cua danh sach
dlist = []
for i in range(n):
    value = int(input(f"Nhap phan tu thu {i+1}: "))
    dlist.append(value)

# Nhập phần tử cần tìm
item = int(input("Nhap phan tu can tim: "))

# Su dung ham tim kiem tuyen tinh
found, index = search_utils.Sequential_Search(dlist, item)

# Hien thi ket qua
if found:
    print(f"Phan tu {item} đuoc tim thay tai vi tri {index}.")
else:
    print(f"Phan tu {item} khong co trong danh sach.")
