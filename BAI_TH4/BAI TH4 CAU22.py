print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
result = []
for num in range(1000, 3001):
    num_str = str(num)
    if all(int(digit) % 2 == 0 for digit in num_str):
        result.append(num_str)
print(','.join(result))
