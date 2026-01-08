class Atm:

    def __init__(self):      #Constructor

        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        while True:
            user_input = input("""
                      Hello how would you like to proceed?
                      1. Enter 1 to create the pin.
                      2. Enter 2 to deposit.
                      3. Enter 3 to withdraw.
                      4. Enter 4 to check the balance.
                      5. Enter 5 to exit. """)

            if user_input == '1':
                self.create_pin()
            elif user_input == '2':
                self.deposit()
            elif user_input == '3':
                self.withdraw()
            elif user_input == '4':
                self.check_balance()
            elif user_input == '5':
                print("Thank you using the ATM")
                break
            else:
               print("Invalid choice")


    def create_pin(self):
        self.pin = input("Create the Pin First: ")
        print("Pin Set Successfully!")

    def deposit(self):
        temp = input("Enter Your pin")
        if temp == self.pin:
            Amt = int(input("Enter the amount to be deposited: "))
            self.balance += Amt
            print(f" {Amt} Amount deposited successfullly")
        else:
            print("Incorrect pin")

    def withdraw(self):
        temp = input("Enter Your pin")
        if temp == self.pin:
            Amt = int(input("Enter the amount to be Withdraw: "))
            if Amt > self.balance:
                print("Insufficient balance!")
            else:
                self.balance -= Amt
                print(f" {Amt} Amount withdrawed successfullly")
        else:
            print("Incorrect pin")

    def check_balance(self):
        temp = input("Enter Your pin")
        if temp == self.pin:
            print(f"Your Balance: {self.balance}")
        else:
            print("Incorrect pin.")



atm = Atm()