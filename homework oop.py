class Account:
    __balance = 0
    def __init__(self, balance):
        self.__balance = balance
    def getBalance(self):
        return self.__balance
    def deposit(self, amt):
        if amt > 0:
            self.__balance = self.__balance + amt
            return True
        else:
            return False
    def withdraw(self, amt):
        if amt <= 0:
            return False
        else:
            self.__balance -= amt
            return True
class Customer:
    __fname = ""
    __lname = ""
    __account = Account(0)

    def __init__(self,fname,lname):
        self.__fname = fname
        self.__lname = lname
    def getfirstname(self):
        return self.__fname
    def getlastname(self):
        return self.__lname
    def getAccount(self):
        return self.__account
    def setAccount(self, acct):
        self.account = acct
class Bank:
    __bankname = ""
    __customers = []
    __numberofcustomers = 0
    def __init__(self, bankname):
        self.__bankname = bankname
    def addCustomer(self,firstname,lastname):
        self.__customers.append(Customer(firstname, lastname))
        self.__numberofcustomers += 1
    def deleteCustomer(self, index):
        self.__customers.pop(index)
    def getnumberofcustomer(self):
        return self.__numberofcustomers
    def getCustomer(self,index):
        return self.__customers[index]
def intro():
    print("**********************")
    print("\tBANK  MANDIRI")
    print("**********************")
intro()
newbank = Bank('sunny')
while True:
    print("\tMAIN MENU")
    print("1. NEW ACCOUNT ")
    print("2. DEPOSIT AMOUNT")
    print("3. WITHDRAW AMOUNT")
    print("4. BALANCE ENQUIRY")
    print("5. ALL ACCOUNT MEMBER")
    print("6. CLOSE AN ACCOUNT")
    print("7. EXIT")
    print("Select Your Option (1-7) ")
    ui = input()
    if ui == '1':
        firstname = input("First name: ")
        lastname = input("Last name: ")
        newbank.addCustomer(firstname, lastname)
    elif ui == '2':
        for i in range(newbank.getnumberofcustomer()):
            print(str(i+1) + ". " + str(newbank.getCustomer(i).getfirstname()) + " " +str(newbank.getCustomer(i).getlastname()))
        select = input("Which number of account u want to deposit :")
        amount = input("number of amount :")
        newbank.getCustomer(int(select)-1).getAccount().deposit(int(amount))
        print("Your balance is ", newbank.getCustomer(int(select)-1).getAccount().getBalance())
    elif ui == '3':
        for i in range(newbank.getnumberofcustomer()):
            print(str(i+1) + ". " + str(newbank.getCustomer(i).getfirstname()) + " " +str(newbank.getCustomer(i).getlastname()))
        select = input("Which number of account u want to withdraw: ")
        amount = input("number of amount :")
        newbank.getCustomer(int(select)-1).getAccount().withdraw(int(amount))
        print("Your balance is ", newbank.getCustomer(int(select)-1).getAccount().getBalance())
    elif ui == '4':
        for i in range(newbank.getnumberofcustomer()):
            print(str(i+1) + ". " + str(newbank.getCustomer(i).getfirstname()) + " " +str(newbank.getCustomer(i).getlastname()))
        select = input("Which number of account u want to check balance: ")
        print("Your balance is ", newbank.getCustomer(int(select) - 1).getAccount().getBalance())
    elif ui == '5':
        for i in range(newbank.getnumberofcustomer()):
            print(str(i + 1) + ". " + str(newbank.getCustomer(i).getfirstname()) + " " + str(newbank.getCustomer(i).getlastname()))
    elif ui == '6':
        for i in range(newbank.getnumberofcustomer()):
            print(str(i+1) + ". " + str(newbank.getCustomer(i).getfirstname()) + " " +str(newbank.getCustomer(i).getlastname()))
        select = input("Which number of account u want to close account: ")
        newbank.deleteCustomer(int(select)-1)
    elif ui == '7':
        print("Thank you for using our bank")
        break