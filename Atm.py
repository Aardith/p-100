class Atm(object):
    def __init__(self,cardnumber, pinnumber):
        self.cardnumber = cardnumber
        self.pinnumber = pinnumber
        self.balance = 100000
        
    def canshwithdrawel(self, amount):
        self.balance-=amount
        print(amount, "Has Been Debited")

    def balanceenquiry(self):
        print(self.balance)

    def change_pin(self, newpin):
        self.pinnumber = newpin
        print("Your Pin Has Been Changed")

aardith = Atm(903826406, 8785)
aardith.balanceenquiry()
aardith.canshwithdrawel(5000)
aardith.balanceenquiry()
aardith.change_pin(3875)
print(aardith.pinnumber)              
             
                 