from BankAccount import BankAccount

class SavingAccount(BankAccount):
    
    def __init__(self, name:str, amount:float) -> None:
        super().__init__(name, amount)
        super().setAccountType('Saving Account')
        
    def getInterest(self) -> float:
        __balance = self.getBalance()
        __interestRate = 10
        return (__balance * (__interestRate/100))

    