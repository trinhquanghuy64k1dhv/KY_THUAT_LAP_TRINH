print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
import sys
import os

def file_read_from_tail(fname, lines):
    if not os.path.exists(fname):
        print(f"File '{fname}' khong ton tai!")
        return

    bufsize = 8192
    fsize = os.stat(fname).st_size
    iter = 0
    data = []

    with open(fname, 'r') as f:
        while True:
            iter += 1
            f.seek(max(fsize - bufsize * iter, 0))
            data.extend(f.readlines())
            if len(data) >= lines or f.tell() == 0:
                print(''.join(data[-lines:]))
                break

# Đuong dan đay đu hoac kiem tra tep
file_read_from_tail('test.txt', 1)
