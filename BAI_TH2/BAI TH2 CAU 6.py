"BEGIN"
print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
j=[] # Khoi tao ds rong de luu gia tri
for i in range (2000,3201) : #Lap qua cac so tu 2000 den 3201
    if  (i%7==0) and (i%5!=0): # ktra chia het cho 7 nhung ko chia het cho 5
        j .append (str(i)) # Them so vao ds duoi dang chuoi
print (','.join(j)) # In cac so, ngan cach bang dau phay
'end'
