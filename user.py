
class User :
    def __init__(self,name):
        self.id = hash(name)
        self.wallet = 0

    def __str__(self):
        return self.id

    def addToWallet(self,amount):
        self.wallet += amount

    def removeToWallet(self,amount):
        self.wallet -= amount