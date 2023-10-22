from classes.transaction import *

class category:

    def __init__(self, catgeorieName, transactions, withdraw, deposit):
        self.catgeorieName = catgeorieName
        self.transactions = transactions
        self.withdraw = withdraw 
        self.deposit = deposit
    
    def sumWithdraw(self):
        for transaction in self.transactions:
           if transaction.amount <= 0:
                self.totalWithdraw+= transaction.amount
    def sumDeposit(self):
        for transaction in self.transactions:
            if transaction.amount > 0:
                self.totalDeposit+= transaction.amount

    def removeTransaction(self, transaction):
         return 0 #TODO
    def addTransaction(self, transaction):
        self.transactions.append(transaction)