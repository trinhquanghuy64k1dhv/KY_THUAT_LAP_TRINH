print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
class Nguoi(object):
    # Phuong thuc getGender mac dinh tra ve "Unknown"
    def getGender(self):
        return "Unknown"

class Nam(Nguoi):
    # Phuong thuc getGender cua lop con Nam tra ve "Nam"
    def getGender(self):
        return "Nam"

class Nu(Nguoi):
    # Phuong thuc getGender cua lop con Nu tra ve "Nu"
    def getGender(self):
        return "Nu"

# Khoi tao doi tuong Nam va Nu
aNam = Nam()
aNu = Nu()

# In gioi tinh cua doi tuong aNam va aNu
print(aNam.getGender())  # In "Nam"
print(aNu.getGender())   # In "Nu"
