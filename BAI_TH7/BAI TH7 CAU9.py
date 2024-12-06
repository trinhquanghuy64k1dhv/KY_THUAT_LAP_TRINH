print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
# Ham sao chep noi dung tu file nguon sang file dich
def copy_file_content(source_file, destination_file):
    try:
        with open(source_file, 'r', encoding='utf-8') as src:
            content = src.read()  # Doc toan bo noi dung tu file nguon
        with open(destination_file, 'w', encoding='utf-8') as dest:
            dest.write(content)  # Ghi noi dung vao file dich
        print(f"Noi dung da duoc sao chep tu '{source_file}' sang '{destination_file}'.")
    except FileNotFoundError:
        print(f"Khong tim thay file: {source_file}")
    except Exception as e:
        print(f"Loi xay ra: {e}")

# Goi ham voi file nguon va file dich
source = 'D:/a.txt'  # Thay bang duong dan file nguon
destination = 'D:/destination.txt'  # Thay bang duong dan file dich
copy_file_content(source, destination)
