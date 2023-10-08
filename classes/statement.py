from classes.transaction import *
from classes.category import *
import random

class statement:

    def __init__(self, statementName, transactions, totalWithdraw, totalDeposit, balance):
        self.statementName = statementName # string
        self.transactions = transactions # array
        self.totalWithdraw = float(totalWithdraw) # /float
        self.totalDeposit = float(totalDeposit) # float
        self.balance = float(balance) # float


    def sumWithdraw(self):
        for transaction in self.transactions:
            if transaction.amount <= 0:
                self.totalWithdraw += transaction.amount 

    def sumDeposit(self):
        for transaction in self.transactions:
            if transaction.amount  > 0:
                self.totalDeposit+= transaction.amount 
                
    def sumBalance(self):
        self.balance = self.totalWithdraw + self.totalDeposit

    def addTransaction(self, transaction):
       self.transactions.append(transaction)

    def addCategory(self, name):
        # create category
        newCategory = category(name, {}, 0, 0)
        self.categories.append(newCategory)

    def searchCategory(self, catName):
        for i in range(self.categories):
            if self.categories[i].name == catName:
                return i
        return -1

    def serachTransaction(self, transDescription):
        for i in range(self.transactions):
            if self.transactions[i].description == transDescription:
                return i
        return -1
   
    def removeTransaction(self, ):  
        return 0 #TODO
    def removeCategory(self, hashId):
        return 0 #TODO
    
    def addTransactionToCategory(self, ):
        return 0 #TODO

    def removeTransactionFromCategory(self):
        return 0 #TODO


# So I need a reliable way to search for transactions and catgeories
# I will need a way to identify the transaction before I call search()
# Categories:
    # Search by name
    # Requires brute force algortihm
    # no dups allowed
#Transactions: 
    # Identify them by date and time
    # Create a sorted list
    # better search time