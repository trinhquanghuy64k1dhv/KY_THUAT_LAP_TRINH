print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
# Đọc file và in đảo ngược kết quả
input_file = open('D:/a.txt', 'r')

for line in input_file:
    l = len(line)  # Độ dài của dòng
    s = ''  # Chuỗi đảo ngược
    while (l >= 1):
        s = s + line[l - 1]  # Lấy ký tự cuối thêm vào chuỗi đảo ngược
        l = l - 1  # Giảm L xuống
    print(s)  # In kết quả đảo ngược

input_file.close()
