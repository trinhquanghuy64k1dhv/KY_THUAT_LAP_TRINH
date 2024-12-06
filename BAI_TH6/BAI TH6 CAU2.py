print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
class Hinhchunhat:
    # Ham khoi tao voi tham so chieu dai va chieu rong
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    # Phuong thuc tinh dien tich
    def dientich(self):
        return self.dai * self.rong

# Khoi tao doi tuong Hinhchunhat voi chieu dai 5 va chieu rong 3
hinh_chunhat = Hinhchunhat(5, 3)

# In dien tich hinh chu nhat
print(hinh_chunhat.dientich())

