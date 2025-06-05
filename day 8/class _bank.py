#bank account
from abc import ABC,abstractmethod

class BankAccount(ABC):
   #  def __init__(self,name,money):
   #   self.name=name
   #   self.money=money
     #self._balance=0
    @abstractmethod
    def get_balance(self):
            pass
    @abstractmethod
    def withdraw(self,money):
            pass
    @abstractmethod
    def deposit(self):
            pass
class SavingAccount(BankAccount):
    __balance=0
    def get_balance(self):
   #   print("balance ",self.__balance)
     return self.__balance
    def withdraw(self,money):
       if self.__balance>=money:
        self.__balance-=money
        print("money withdrawed",money)
        print("remaining balance",self.__balance)
       else:
          print("insufficient balance")
    
    def deposit(self,money):
       self.__balance+=money
       print("money added",money)
       print("money addded sucessfuly",self.__balance)
class CurrentAccount(BankAccount):
   __balance=0
   withdrawlimit=0
   

   def get_balance(self):
      # print("balance", self.__balance)
      return self.__balance 
   def withdraw(self,money):
      if self.__balance>money:
         self.__balance-=money
         print("ammount withdrawed",money)
         print(self.__balance)
      else:
         print("insufficient balnce")
   def deposit(self,money):
      self.__balance+=money
      print("amount added",money)
      print("total amount:",self.__balance)
class Bank:
 def __init__(self,name,money,acc_type="savings"):
      self.name=name
      self.money=money
      if acc_type=="savings":
        self.account=SavingAccount()
      if acc_type=="current":
         self.account=CurrentAccount()
          
   
class Manager:
   def customer_info(self,x:Bank):
      print(f"name:{x.name}")
      if(type(x.account)==SavingAccount):
          print("Saving Account")
      else:
          print("current Account")
      
      print(x.account.get_balance())
          
      

s=Bank("sai",100,"savings")
s.account.deposit(100)
s.account.get_balance()
c=Manager()
c.customer_info(s)
d=Bank("ram",100,"current")
d.account.deposit(100)
d.account.get_balance()
c.customer_info(d)
#class customer_info:
# sa=CurrentAccount("sai",10000)
# sa.deposite(100)
# sa.withdraw(2000)
# sa.get_balance()
# b=Bank("sai",100,"current")
