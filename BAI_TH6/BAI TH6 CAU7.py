print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius  # Khoi tao ban kinh

    def area(self):
        # Tinh dien tich hinh tron
        return math.pi * self.radius ** 2

    def circumference(self):
        # Tinh chu vi hinh tron
        return 2 * math.pi * self.radius

# Tao doi tuong cua lop Circle
circle = Circle(7)

# In dien tich va chu vi
print(f"Dien tich hinh tron: {circle.area()}")
print(f"Chu vi hinh tron: {circle.circumference()}")
