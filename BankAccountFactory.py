from CheckingAccount import CheckingAccount
from SavingAccount import SavingAccount
from BankAccount import BankAccount


class BankAccountFactory:

    def __init__(self) -> None:
        pass

    def makeAccount(self, accountType:str, name:str, amount:float):
        if(accountType == 'SAVING'):
            return SavingAccount(name, amount)
            
        elif(accountType == 'CHECKING'):
            return CheckingAccount(name, amount)
        
        else:
            return False