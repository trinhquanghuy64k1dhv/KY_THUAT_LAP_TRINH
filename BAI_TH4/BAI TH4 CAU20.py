print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
# Nhap so n
n = int(input("Nhap so n: "))

# Tao danh sach đe luu tru cac dong cua tam giac Pascal
pascals_triangle = []

# Tao tam giac Pascal
for i in range(n):
    # Tao dong moi
    row = [1] * (i + 1)  # Moi dong bat đau voi cac 1
    for j in range(1, i):
        # Tinh gia tri o vi tri j
        row[j] = pascals_triangle[i - 1][j - 1] + pascals_triangle[i - 1][j]
    pascals_triangle.append(row)

# In tam giac Pascal
for row in pascals_triangle:
    print(" ".join(map(str, row)))
