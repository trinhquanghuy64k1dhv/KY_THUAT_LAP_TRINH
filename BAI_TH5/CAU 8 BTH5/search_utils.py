print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
# search_utils.py
def Sequential_Search(dlist, item):
    """
    Tim kiem phan tu trong danh sach bang giai thuat tim kiem tuyen tinh.
    Tra ve (True, index) neu tim thay phan tu, (False, -1) neu khong tim thay.
    """
    for index, value in enumerate(dlist):
        if value == item:
            return True, index
    return False, -1
