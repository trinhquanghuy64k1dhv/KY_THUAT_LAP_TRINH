print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
# Ham ghi noi dung danh sach vao tep
def write_list_to_file(filename, data_list):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for item in data_list:
                file.write(f"{item}\n")  # Ghi tung phan tu cua danh sach vao tep
        print(f"Noi dung danh sach da duoc ghi vao file '{filename}'.")
    except Exception as e:
        print(f"Loi khi ghi vao file: {e}")

# Danh sach can ghi
my_list = ["Dong thu nhat", "Dong thu hai", "Dong thu ba"]

# Goi ham voi ten file va danh sach
filename = 'D:/output.txt'  # Thay doi duong dan neu can
write_list_to_file(filename, my_list)
