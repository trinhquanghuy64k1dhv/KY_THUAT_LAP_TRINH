print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
class StringManipulator:
    def __init__(self):
        self.text = ""

    def get_String(self):
        # Nhap chuoi tu nguoi dung
        self.text = input("Nhap mot chuoi: ")

    def print_String(self):
        # In chuoi bang chu in hoa
        print(self.text.upper())

# Tao doi tuong cua lop StringManipulator
string_manipulator = StringManipulator()

# Chap nhan chuoi tu nguoi dung
string_manipulator.get_String()

# In chuoi da nhap bang chu in hoa
string_manipulator.print_String()
