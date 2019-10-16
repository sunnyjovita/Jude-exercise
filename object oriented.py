# make a balance account
class Account:
    # make the title with capital letter
    __balance = 0

    # double underscore to make the balance is private
    def __init__(self, balance):
        self.__balance = balance

    #     make an object (balance)
    def getBalance(self):
        return self.__balance

    def deposit(self, amt):
        if amt > 0:
            self.__balance = self.__balance + amt
            return True
        else:
            return False


# myAccount = Account(5000)
# myAccount.__balance = 100000
# # can not print 100000 because we use double underscore to make it private
#  make 2 accounts
myAccount = Account(5000)
myAccount2 = Account(100000)
if (myAccount.deposit(10000)):
    print("Account balance is >>", myAccount.getBalance())
else:
    print("hahahahaahaha")


# print("Account2 balance is >>", myAccount2.getBalance())
# withdraw the account
class Account:
    # make the title with capital letter
    __balance = 0

    # double underscore to make the balance is private
    def __init__(self, balance):
        self.__balance = balance

    def getBalance(self):
        return self.__balance

    def withdraw(self, amt):
        if amt <= 0:
            return False
        else:
            self.__balance -= amt
            return True


# myAccount = Account(5000)
# myAccount.__balance = 100000
# # can not print 100000 because we use double underscore to make it private
#  make 2 accounts
myAccount = Account(5000)
myAccount2 = Account(100000)
if (myAccount.withdraw(1000)):
    print("Account balance is >>", myAccount.getBalance())
else:
    print("hahahahaahaha")


# make the customer account
class Customer:
    __fname = ""
    __lname = ""
    __account = Account(50000)

    def __init__(self, fname, lname):
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


myFc = Customer("Mia", "Ozawa")

print(myFc.getAccount().getBalance())
# make a bank account
class Bank:
    __bankname = ""
    __customers = []
    __numberofcustomers = 0

    def __init__(self, bankname):
        self.__bankname = bankname

    def addCustomer(self,firstname,lastname):
        # firstname = input("Enter your firstname :")
        # lastname = input("Enter your lastname :")
        self.__customers.append(Customer(firstname, lastname))
        self.__numberofcustomers += 1

    def getnumberofcustomer(self):
        return self.__numberofcustomers

    def getCustomer(self,index):
        return self.__customers[index]

newbank = Bank('sunny')
newbank.addCustomer('jeco','danka')
print(newbank.getCustomer(0).getfirstname())
