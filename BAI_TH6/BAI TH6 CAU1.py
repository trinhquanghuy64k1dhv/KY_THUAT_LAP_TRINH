print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
class Circle(object):
    # Khoi tao voi tham so ban kinh r
    def __init__(self, r):
        self.radius = r

    # Phuong thuc tinh dien tich
    def area(self):
        return self.radius ** 2 * 3.14

# Khoi tao doi tuong Circle voi ban kinh 2
aCircle = Circle(2)

# In dien tich hinh tron
print(aCircle.area())
