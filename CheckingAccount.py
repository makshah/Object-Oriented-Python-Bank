import BankAccount

class CheckingAccount(BankAccount.BankAccount):
    __interestRate = 5

    def __init__(self, name:str, amount:float) -> None:
        super().__init__(name, amount)
        super().setAccountType('Checking Account')
    
    def getInterest(self) -> float:
        __balance = self.getBalance()
        __interestRate = 5
        return (__balance * (__interestRate/100))