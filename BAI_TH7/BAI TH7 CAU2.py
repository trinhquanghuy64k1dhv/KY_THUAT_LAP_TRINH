print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
# Mo file de doc
k = open('D:/a.txt', 'r')
# Khoi tao bien dem
char, wc, lc = 0, 0, 0
# Doc tung dong trong file
for line in k:
    lc += 1  # Dem so dong
    char += len(line)  # Dem so ky tu trong dong
    wc += len(line.split())  # Dem so tu trong dong dua tren khoang trang
# Dong file sau khi doc
k.close()
# In ket qua
print("So ky tu la: %d" % char)
print("So tu la: %d" % wc)
print("So dong la: %d" % lc)
