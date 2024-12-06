print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
def binary_search(arr, value):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == value:
            return True
        elif arr[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return False
