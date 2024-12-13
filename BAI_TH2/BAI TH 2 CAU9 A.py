print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
# Nhap mot chuoi 
str = input ("Enter a String:")
dict ={} # Khoi tao mot dictionary rong
for n in str: # Lap qua tung ki tu trong chuoi
    keys = dict.keys() # Kiem tra xem ki tu da ton tai trong dictionary chua
    if n in keys:
        dict[n] += 1 # Neu co, tang gia trin len 1
    else:
        dict[n] = 1 # Neu chua, gan gia tri bang 1
print (dict)        
