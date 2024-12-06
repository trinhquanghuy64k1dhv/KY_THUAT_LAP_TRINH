print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
import math
def Tinh(R):
    """
    Hàm Tinh tinh chu vi va dien tich hinh tron voi ban kinh R.
    Tham so:
    R (float): Ban kinh cua hinh tron.
    Tra ve:
    tuple: (chu_vi, dien_tich) neu R hop le.
    In thong bao loi neu R khong hop le.
    """
    if not isinstance(R, (int, float)):
        print("Gia tri ban kinh phai la so.")
        return
    if R <= 0:
        print("Gia tri ban kinh phai lon hon 0.")
        return
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * (R ** 2)
    return chu_vi, dien_tich
def main():
    try:
        R_input = input("Nhap ban kanh hinh tron: ")
        R = float(R_input)
        result = Tinh(R)
        if result:
            chu_vi, dien_tich = result
        print(f"Chu vi hinh tron: {chu_vi:.2f}")
        print(f"Dien tich hinh tron: {dien_tich:.2f}")
    except ValueError:
        print("Gia tri nhap vao khong hop le. Vui long nhap mot so thuc.")
if __name__ == "__main__":
    main()
