
class Atm(object):
    #init=constructor,def=function,self=this
    def __init__(self,name,age,contact,address,amount):
        self.name=name
        self.age=age
        self.contact=contact
        self.address=address
        self.amount=1500

    def cashwithdrawl(self):
        self.amount=self.amount-500
        print("you have successfully withdrawed ",self.amount)
        
      
    def cashdeposit(self):
        self.amount=self.amount+500
        print(self.amount ," has been deposited in the bank successfully")
        

    def balanceinquiry(self):
        x=self.amount+500
        print("you balance",x)


abc=Atm("sparsh","14","01234567890","Mumbai","1000")
print("Name-Sparsh","Age-14","Contact-1234567890","City-mumbai")
print("your account balance  is ",abc.amount)
abc.cashwithdrawl()
abc.cashdeposit()
abc.balanceinquiry()