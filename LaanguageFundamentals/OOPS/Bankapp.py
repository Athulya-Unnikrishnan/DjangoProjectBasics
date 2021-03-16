from datetime import *
class Bank:
    bank="SBI"#static variable so that memory is alocated one time only when each object is called
    #class variable or static variable can be called using classname.variable

    def create_account(self,acc_no,cust_name,Total_amount):
        self.acc_no=acc_no
        self.cust_name=cust_name
        self.Total_amount=Total_amount

    def deposit(self,amount):
        self.Total_amount+=amount
        print("Bank Name is",Bank.bank,"Account Number:",self.acc_no,"credited with amount",amount,"on",datetime.today())
        print("Your available balance is",self.Total_amount)

    def withdraw(self,amount):
        if(amount>self.Total_amount):
            print("Transaction failed")
        else:
            self.Total_amount-=amount
            print("Account Number :",self.acc_no,"debited with amount",amount)
            print("Transaction successfull")

    def balance(self):
        print("Your available balance is", self.Total_amount)

ban=Bank()
ban.create_account(123456,"Athulya Unnikrishnan",1000)
ban.deposit(1000)
ban.withdraw(500)
#ban.balance()
