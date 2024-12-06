print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
def file_read(fname):
    from itertools import islice
    with open(fname, "w") as myfile:
        myfile.write("Python Exercises\n")
        myfile.write("Java Exercises\n")
    txt = open(fname)
    print(txt.read())
file_read('abc.txt')
