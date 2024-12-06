print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
ds_tu= input('Nhap day cac tu :').split()
# Tim do dai cua tu dai nhat
do_dai_max= max(len(tu) for tu in ds_tu)

#In ra cac tu co do dai bang do dai lon nhat
tu_dai_nhat= [tu for tu in ds_tu if len(tu) ==do_dai_max]
# In ra ket qua
print('Tu dai nhat:', ', '.join(tu_dai_nhat))
