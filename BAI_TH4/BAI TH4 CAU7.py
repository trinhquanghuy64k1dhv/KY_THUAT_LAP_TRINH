print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
chuoi= input('Nhap chuoi:')
# Loai bo tat ca cac chu so khoi chuoi
chuoi_moi = ''.join([ch for ch in chuoi if not ch.isdigit()])
# In ra chuoi moi
print(' In ra chuoi moi khi bo so:', chuoi_moi)

