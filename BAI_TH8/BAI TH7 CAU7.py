print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
# Mo file de dem so dong
def count_lines_in_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()  # Doc tat ca cac dong trong file
            return len(lines)  # Tra ve so dong
    except FileNotFoundError:
        print(f"Khong tim thay file: {filename}")
        return 0

# Goi ham voi ten file can dem
filename = 'D:/a.txt'  # Thay doi duong dan file neu can
line_count = count_lines_in_file(filename)

# In ket qua
print(f"So dong trong file '{filename}' la: {line_count}")
