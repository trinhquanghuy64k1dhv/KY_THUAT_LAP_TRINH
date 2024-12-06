"BEGIN"
print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
j=[]
for i in range (2000,3201) :
    if  (i%7==0) and (i%5!=0):
        j .append (str(i))
print (','.join(j))
'end'
