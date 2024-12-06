print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
class StringReverser:
    def __init__(self, text):
        self.text = text

    def reverse_words(self):
        # Tach chuoi thanh cac tu
        words = self.text.split()
        
        # Dao nguoc thu tu cac tu trong danh sach
        reversed_words = words[::-1]
        
        # Noi cac tu da dao nguoc lai thanh chuoi
        result = " ".join(reversed_words)
        
        return result

# Du lieu vao
input_text = "hello .py"
reverser = StringReverser(input_text)

# Ket qua
print(reverser.reverse_words())  
