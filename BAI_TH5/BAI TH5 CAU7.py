print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
import numpy as np
data_type = [('name', 'S15'), ('class', int), ('height', float)]

# Tao mot mang cau truc
students = np.array(students_details, dtype=data_type)
print("Original array:")
print(students)
print("Sort by height")
print(np.sort(students, order='height'))