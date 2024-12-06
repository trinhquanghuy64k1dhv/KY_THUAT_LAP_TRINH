print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
import math
def benefit(t, n, k):
    """
    Ham benefit tinh so tien nhan đuoc sau k thang voi lai suat t% moi thang va số vốn ban đầu n.
    Tham so:
    t (float): Lai suat hang thang duoi dang phan tram.
    n (float): So von ban đau.
    k (int): So thang gui tiet kiem.
    Tra ve:
    float: So tien cuoi cung sau k thang.
    """
    A = n * (1 + t / 100) ** k
    return A
def main():
    try:
        t_input = input("Nhap lai suat tiet kiem hang thang (%): ")
        t = float(t_input)
        if t < 0:
            print("Lai suat phai lon hon hoac bang 0.")
            return
        n_input = input("Nhap so von ban đau (n): ")
        n = float(n_input)
        if n < 0:
            print("So von ban đau phai lon hon hoac bang 0.")
            return
        k_input = input("Nhap so thang gui tiet kiem (k): ")
        if not k_input.isdigit():
            print("So thang gui phai la mot so nguyen khong am.")
            return
        k = int(k_input)
        if k < 0:
            print("So thang gui phai lon hon hoac bang 0.")
            return
        final_amount = benefit(t, n, k)
        print(f"So tien nhan đuoc sau {k} thang la: {final_amount:.2f}")
    except ValueError:
        print("Gia tri nhap vao khong hop le. Vui long nhap so thuc cho lai suat và số vốn, và số nguyên cho số tháng gửi.")
if __name__ == "__main__":
    main()
