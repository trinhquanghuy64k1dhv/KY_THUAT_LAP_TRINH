print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
# Import module bubble_sort
from bubble_sort import bubbleSort

# Nhap danh sach cac phan tu tu ban phim
nlist = input("Nhap danh sach cac so (cach nhau bang dau phay): ")
nlist = list(map(int, nlist.split(',')))# Chuyen danh sach chuoi thanh danh sach so nguyen

# Goi ham bubbleSort va hien thi ket qua
sorted_list = bubbleSort(nlist)
print("Danh sach sau khi sap xep:", sorted_list)
