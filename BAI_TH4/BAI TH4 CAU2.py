print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
S= input('Nhap chuoi:')

for ch in S:
    #Bo qua space va tab
    if ch not in [' ', '\t']:
        print(ch)
