print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
input_str = input("Nhap day so: ")
numbers = list(map(int, input_str.split(',')))
odd_numbers = [num for num in numbers if num % 2 != 0]
print(",".join(map(str, odd_numbers)))
