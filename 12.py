nameInput = input("Ur id bro")
depositInput = int(input("how much dolla u wanna keep: $"))
amountInput = int(input("How much do u wanna put:"))
cashoutInput = int(input("How much do u wanna take out:"))
class Bank:
    def __init__(self,name,deposit):
        self.name = name
        self.__deposit = deposit

    def InsertMoney(self,amount):
        self.__deposit += amount
        if amount > 0:
            print(f"""We gotchu bro
                  Money u put:${amount}
                  What you got now:${self.__deposit}""")
        else:
            print("Not possible kid")  

    def withdraw(self,cashout):
        if 0 < cashout < self.__deposit:
            print("Here u go kid.")
        else:
            print("U dont have it.")

BankAccount = Bank(nameInput,depositInput)

BankAccount.InsertMoney(amountInput)
BankAccount.withdraw(cashoutInput)