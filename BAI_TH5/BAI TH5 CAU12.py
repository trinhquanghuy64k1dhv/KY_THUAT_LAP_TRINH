print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
import numpy as np

# Du lieu dau vao
student_id = [1023, 5202, 6230, 1671, 1682, 5241, 4532]
student_height = [40.0, 42.0, 45.0, 41.0, 38.0, 40.0, 42.0]

# Su dung lexsort de sap xep theo chieu cao tang dan
indices = np.lexsort((student_height,))

# In ket qua chi so
print("Chi so:")
print(indices)

# In ket qua du lieu da sap xep
print("Du lieu sap xep:")
for i in indices:
    print(student_id[i], student_height[i])
