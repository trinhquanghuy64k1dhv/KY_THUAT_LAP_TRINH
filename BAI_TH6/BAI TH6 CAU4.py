print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
def roman_to_integer(roman):
    # Bang anh xa tu La Ma sang so nguyen
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    for i in range(len(roman)):
        # Lay gia tri cua ky tu hien tai va ky tu tiep theo (neu co)
        current_value = roman_map[roman[i]]
        
        # Kiem tra xem co phai can tru khong
        if i + 1 < len(roman) and current_value < roman_map[roman[i + 1]]:
            total -= current_value  # Neu ky tu tiep theo lon hon, tru gia tri nay
        else:
            total += current_value  # Neu khong, cong gia tri nay vao tong

    return total

# Vi du su dung
print(roman_to_integer("IX"))  
print(roman_to_integer("MCMXCIV"))
