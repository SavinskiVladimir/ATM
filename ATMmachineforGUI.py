from account import *
from json import *

class ATMmachine:
    def __init__(self):
        self.__users = []
        self.__amount = 0
        self.__active_user = None

    def synchronize(self, filename, type):
        if type == OperationType.GET:
            with open(filename, "r") as f:
                data = load(f)
            self.__amount = data[0]["amount"]
            for item in data:
                if "amount" not in item.keys():
                    self.__users.append(Account(item["name"], item["pin"], item["balance"], item["number"], item["history"]))
            return True
        elif type == OperationType.PUT:
            data = [{"amount" : self.__amount}]
            for user in self.__users:
                data.append(user.to_dict())
            with open(filename, "w") as f:
                dump(data, f)
            return True
        return False

    def addAccount(self, username, pincode):
        new_account = Account(username, pincode)
        for account in self.__users:
            if (account.getName() == new_account.getName() and account.getPin() == new_account.getPin()):
                return False

        new_account.setNumber(hash(new_account))
        self.__users.append(new_account)
        return True

    def authorize(self, surname, name, pincode):
        for account in self.__users:
            if (account.getName() == name + " " + surname and account.getPin() == pincode):
                self.__active_user = account
                return (True, account.getName().split(" ")[0])

        return (False, "")

    def getMoney(self, amount):
        if (self.__amount < amount):
            return (False, "Сумма не доступна для снятия")
        else:
            if self.__active_user.getMoney(amount):
                self.__amount -= amount
                return (True, "Заберите деньги")
            else:
                return (False, "Недостаточно средств")

    def putMoney(self, amount):
        self.__amount += amount
        self.__active_user.putMoney(amount)

    def getOperations(self):
        return self.__active_user.getOperations()

    def getBalance(self):
        return self.__active_user.getBalance()

    def increaseAmount(self, amount):
        self.__amount += amount

    def getAmount(self):
        return "Сумма средств в банкомате: " + str(self.__amount)

    def decreaseAmount(self, amount):
        if self.__amount < amount:
            return (False, "Недостаточно средств")
        else:
            self.__amount -= amount
            return (True, "Заберите средства")

    def deAuthorize(self):
        result = "До свидания, " + self.__active_user.getName().split()[0]
        self.__active_user = None
        return result