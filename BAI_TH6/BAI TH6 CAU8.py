print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
class Bank:
    Account_type = "Savings"
    location = "Guntur"

    def __init__(self, name, Account_Number, balance):
        self.name = name
        self.Account_Number = Account_Number
        self.balance = balance
        self.Account_type = Bank.Account_type
        self.location = Bank.location

    def __repr__(self):
        print("Welcome to the SBI ATM Machine")
        account_pin = int(input("Please enter your pin number: "))
        if account_pin == 123:
            self.Account()
        else:
            print("Pin Incorrect. Please try again")
            self.Error()
        return f"{self.name}, {self.Account_Number}"

    def Error(self):
        account_pin = int(input("Please enter your pin number: "))
        if account_pin == 123:
            self.Account()
        else:
            print("Pin Incorrect. Please try again")
            self.Error()

    def Account(self):
        print("Your Card Number is: XXXX XXXX XXXX 1337")
        print("Would you like to deposit/withdraw/Check Balance?")
        print("""
1) Balance
2) Withdraw
3) Deposit
4) Quit
""")
        option = int(input("Please enter your choice: "))
        if option == 1:
            self.Balance()
        elif option == 2:
            self.Withdraw()
        elif option == 3:
            self.Deposit()
        elif option == 4:
            print("Thank you for using the SBI ATM Machine!")
            exit()
        else:
            print("Invalid option. Please try again.")
            self.Account()

    def Balance(self):
        print("Balance:", self.balance)
        self.Account()

    def Withdraw(self):
        w = int(input("Please Enter Desired amount: "))
        if self.balance > 0 and self.balance >= w:
            self.balance -= w
            print("Your transaction is successful")
            print("Your Balance:", self.balance)
        else:
            print("Your transaction is cancelled due to insufficient balance.")
        self.Account()

    def Deposit(self):
        d = int(input("Please Enter Desired amount: "))
        self.balance += d
        print("Your transaction is successful")
        print("Balance:", self.balance)
        self.Account()


# Tao đoi tuong va chay chuong trinh
t1 = Bank('Mahesh', 1453210145, 5000)
print(t1)
