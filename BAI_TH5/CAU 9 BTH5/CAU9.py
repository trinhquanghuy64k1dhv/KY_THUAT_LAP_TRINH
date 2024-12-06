print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
#Nhap module nhi phan_search

from binary_search import binary_search

# Nhap danh sach va phan tu can tim
list_input = input("Nhap danh sach cac so (cach nhau bang dau phay): ")
list_input = list(map(int, list_input.split(',')))
list_input.sort()  # Đam bao danh sach đuoc sap xep đe su dung binary search

value = int(input("Nhap phan tu can tim: "))

# Goi ham binary_search va hien thi ket qua
result = binary_search(list_input, value)
print("Ket qua:", result)
