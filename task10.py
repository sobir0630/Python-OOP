class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} hisobiga {amount} so'm pul qushildi hsiob {self.balance}")
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.balance} dan {amount} so'm ayrildi hisob {self.balance}")
            
        else:
            print(f"hisobda mablag' yetarli emas hisobda {self.balance} so'm mavjud")

balans = 50000
bank = BankAccount("Sobirjon", balans)

entry = int(input("nech pul kirtasiz ->> "))
bank.deposit(entry)        
 
entry2 = int(input(f"nech pul yechasiz hisobda {bank.balance} ->> ")) 
bank.withdraw(entry2)        




