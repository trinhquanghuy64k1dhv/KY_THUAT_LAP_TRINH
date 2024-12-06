print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
input_file=open('D:/a.txt','r')
for line in input_file:
    l=len(line)
    s=' '
    while(l>=1):
        s=s+line[1-1]
        l=l-1
    print(s)
input_file.close()
