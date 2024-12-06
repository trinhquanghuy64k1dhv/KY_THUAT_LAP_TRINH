print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
import numpy as np

# Tao du lieu dau vao
data = np.array([
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.1),
    ('Pit', 5, 40.11)
  ],dtype=[('name', 'U10'), ('class', 'i4'), ('height', 'f4')])

# Sap xep mang theo 'class' truoc sau do 'height' tang dan
sorted_data = np.sort(data, order=['class', 'height'])

# In ket qua da sap xep
print("Ket qua sap xep")
print(sorted_data)
