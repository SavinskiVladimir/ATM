from enum import Enum
from datetime import datetime

class OperationType(Enum):
    PUT = 1
    GET = 2

class NumericException(Exception) :
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class Account:
    def __init__(self, *args):
        if len(args) == 2:
            self.__name = args[0]
            self.__pincode = args[1]
            self.__history = []
            self.__balance = 0
            self.__number = 0

        else:
            self.__name = args[0]
            self.__pincode = args[1]
            self.__balance = args[2]
            self.__number = args[3]
            self.__history = args[4]

    def __repr__(self):
        return f"name = {self.__name}"

    def to_dict(self):
        return {
            "name" : self.__name,
            "pin" : self.__pincode,
            "balance" : self.__balance,
            "number" : self.__number,
            "history" : self.__history
        }

    def getBalance(self):
        return "Ваш баланс: " + str(self.__balance)

    def __logOperation(self, type, amount):
        now = datetime.now()

        if type == OperationType.PUT:
            self.__history.append(tuple(["пополнение", amount, now.strftime('%Y-%m-%d %H:%M:%S')]))
        else:
            self.__history.append(tuple(["снятие", amount, now.strftime('%Y-%m-%d %H:%M:%S')]))

    def putMoney(self, amount):
        self.__balance += amount
        self.__logOperation(OperationType.PUT, amount)

    def getMoney(self, amount):
        if (self.__balance < amount):
            return False
        else:
            self.__balance -= amount
            self.__logOperation(OperationType.GET, amount)
        return True

    def getOperations(self):
        result = "История операций\n"
        for operation in self.__history:
            result += "- " + str(operation[0]) + " " + str(operation[1]) + " " + str(operation[2]) + "\n"
        return result

    def setNumber(self, number):
        self.__number = number

    def getNumber(self):
        return self.__number

    def getName(self):
        return self.__name

    def getPin(self):
        return self.__pincode



