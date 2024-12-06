print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
from itertools import islice
def file_read_from_head(fname, nlines):
    with open(fname) as f:
        for line in islice(f, nlines):
            print(line) 
file_read_from_head('test.txt', 2)

