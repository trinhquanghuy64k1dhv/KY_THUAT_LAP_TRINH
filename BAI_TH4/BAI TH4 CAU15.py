print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
# Nhap chuoi tu ban phim
input_string = input("Nhap cac tu tieng Anh, cach nhau boi dau cach: ")

# Tach chuoi thanh cac tu
words = input_string.split()

# Sap  xep cac tu theo thu tu tu dien
sorted_words = sorted(words)

# In ra cac tu da sap xep
print("Cac tu theo thu tu tu đien:")
for word in sorted_words:
    print(word)
