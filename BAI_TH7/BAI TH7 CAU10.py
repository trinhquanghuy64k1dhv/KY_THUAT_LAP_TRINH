print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
# Ham tim tu dai nhat trong file
def find_longest_words(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            words = file.read().split()  # Doc noi dung va tach thanh cac tu
        max_length = len(max(words, key=len))  # Do dai tu dai nhat
        # Tim cac tu dai nhat
        longest_words = [word for word in words if len(word) == max_length]
        return longest_words
    except FileNotFoundError:
        print(f"Khong tim thay file: {filename}")
        return []
    except Exception as e:
        print(f"Loi xay ra: {e}")
        return []

# Goi ham voi file can tim
filename = 'D:/a.txt'  # Thay bang duong dan file cua ban
longest_words = find_longest_words(filename)

# In ket qua
if longest_words:
    print(f"Cac tu dai nhat trong file '{filename}' la: {', '.join(longest_words)}")
else:
    print("Khong tim thay tu nao hoac file rong.")
