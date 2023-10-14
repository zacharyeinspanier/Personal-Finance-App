from classes.transaction import *
from classes.category import *
import random
import time

class statement:

    def __init__(self, statementName, totalWithdraw = 0, totalDeposit = 0, balance = 0, order=0,  transactions = []):
        self.statementName = statementName # string
        self.transactions = transactions # array
        self.totalWithdraw = float(totalWithdraw) # /float
        self.totalDeposit = float(totalDeposit) # float
        self.balance = float(balance) # float
        self.order = order


    def sumWithdraw(self):
        for transaction in self.transactions:
            if transaction.amount <= 0:
                self.totalWithdraw += transaction.amount 

    def sumDeposit(self):
        for transaction in self.transactions:
            if transaction.amount  > 0:
                self.totalDeposit+= transaction.amount 
                
    def sumBalance(self):
        self.balance = float(self.totalWithdraw + self.totalDeposit)

    def addTransaction(self, transaction):
        transaction.order = (len(self.transactions) + 1)
        self.transactions.append(transaction)

    def removeTransaction(self, order = 0, description = ""): 
        if order == 0 and description == "":
            return False
        
        transactionIndex = self.getTransactionIndex(order, description)

        if transactionIndex == -1:
            return False
        
        transactionStartOrder = self.transactions[transactionIndex].order
    
        self.transactions.pop(transactionIndex)

        for i in range(transactionIndex, len(self.transactions)):
            self.transactions[i].order = transactionStartOrder
            transactionStartOrder += 1

        return True
    def getTransactionIndex(self, order = 0, description = ""):
        if order > 0 and order <= len(self.transactions):
            return (order-1)

        elif description != "":
            #search or Decription, Note Descriptions are not unique
            for index, transaction in enumerate(self.transactions):
                if transaction.description == description:
                    return index
        
        return -1
    def print(self):
        for transaction in self.transactions:
            print("#", transaction.order, " Description", transaction.description, " Ammout: ", transaction.amount, "\n")


    def createTransActions(self, transactions):
        for currTransaction in transactions:
            newTransaction = transaction()
            newTransaction.parseDictionary(currTransaction)
            self.addTransaction(newTransaction)
        self.sumWithdraw()
        self.sumDeposit()
        self.sumBalance()
        return 0

    def changeStatementName(self, newName):
        self.statementName = newName
        
    def delete(self):
        while len(self.transactions) > 0:
            deleteTrans = self.transactions.pop()
            del deleteTrans
        
