print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
def bubbleSort(nlist):
    n = len(nlist)  # So luong phan tu trong danh sach
    for i in range(n - 1):  # Lap qua tung phan tu tru phan tu cuoi cung
        swapped = False  # Bien swapped dung de kiem tra neu co su trao doi
        for j in range(n - 1 - i):  # Lap qua cac phan tu chua duoc sap xep
            if nlist[j] > nlist[j + 1]:  # Neu phan tu hien tai lon hon phan tu ke tiep
                # Hoan doi hai phan tu
                nlist[j], nlist[j + 1] = nlist[j + 1], nlist[j]
                swapped = True  # Danh dau rang co trao doi xay ra
        # Neu khong co su trao doi nao trong vong lap danh sach da duoc sap xep
        if not swapped:
            break
    return nlist  # Tra ve danh sach da sap xep
