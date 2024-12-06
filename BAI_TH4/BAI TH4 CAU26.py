print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
transactions = []
while True:
    transaction = input("Nhap giao dich (hoac nhap 'stop' đe ket thuc): ")
    if transaction.lower() == 'stop':
        break
    transactions.append(transaction)
balance = 0
for transaction in transactions:
    type, amount = transaction.split()
    amount = int(amount)
    if type == 'D':
        balance += amount
    elif type == 'W':
        balance -= amount
print("So du tai khoan:", balance)
