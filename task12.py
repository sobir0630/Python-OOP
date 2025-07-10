import sys

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
            
    def show_balance(self):
        print(f"hisob {self.balance}")
        
        
def main():
    balans = 50000
    bank = BankAccount("Sobirjon", balans)
    
    
    while True:
        print("""

_____ MENU _____

1. Pul qo'shish (Deposit)
2. Pul yechish (Withdraw)
3. Balansni ko'rish (Show balance)
4. Chiqish (Exit)

""")
        choise = input("Menuni tanlnag: ")
        
        
        if not choise.isdigit():
            print("iltimos faqat raqam kritng!!!")
            continue

        choise = int(choise)



        if choise == 1:
            entry = input("nech pul kirtasiz ->> ")
            if entry.isdigit():
                bank.deposit(int(entry)) 
            else:
                print("faqat raqam kritng!!!")
            
             
        elif choise == 2:       
            entry2 = input(f"nech pul yechasiz hisobda {bank.balance} ->> ")
            if entry.isdigit():
                bank.withdraw(int(entry2)) 
            else:
                print("faqat raqam kritng!!!") 
            
            
        elif choise == 3:
            bank.show_balance()
            
            
        elif choise == 4:
            print("dasturdan chiqdingiz")
            sys.exit()
            
            
        else:
            print("notug'ri tanlov faqat 1 dan 4gacha raqam kritng!!!")
                    
if __name__ =="__main__":
    main()
                
                
    

            
            

      




