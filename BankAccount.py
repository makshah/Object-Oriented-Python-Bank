class BankAccount:
    __name, __balance = None, None
    __type = None


    def __init__(self, name: str, amount: float):
        self.__name = name
        self.__balance = amount

    def getName(self) -> str:
        return self.__name

    def setName(self, name: str) -> bool:
        if(name.isalpha()):
            self.__name = name
            return True
        else:
            return False

    def getBalance(self) -> float:
        return self.__balance
    
    def makeDeposit(self, amount: float) -> bool:
        if(amount > 0):
            self.__balance += amount
            return True
        else:
            return False
    
    def makeWithdraw(self, amount: float) -> bool:
        if(amount > self.__balance):
            return False
        else:
            self.__balance -= amount
            return True

    def getAccountType(self) -> str:
        return self.__type

    
    def setAccountType(self, accountType : str):
        self.__type = accountType
        
    
    def getInterest(self) -> float:
        pass
