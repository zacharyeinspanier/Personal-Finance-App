from classes.transaction import transaction


class treeNode:

    def __init__(
        self, 
        name: str,
        withdraw: int, 
        deposit: int, 
        balance: int,
        type: str,
        children = {},
        parent = None
    ):
        self.name = name
        self.children = children
        self.withdraw = withdraw
        self.deposit = deposit
        self.balance = balance
        self.parent = parent
        self.type = type

    def sumWithdraw(self):
        for node in self.children.keys():
            if self.children[node].withdraw <= 0:
                self.withdraw += self.children[node].withdraw

    def sumDeposit(self):
        for node in self.children.keys():
            if self.children[node].deposit  > 0:
                self.deposit += self.children[node].deposit
                
    def sumBalance(self):
        self.balance = float(self.withdraw + self.deposit)

    def add(self, node):
        # key would be name
        if node.name not in self.children:
            self.children[node.name] = node
            return True
        else: 
            return False
        

    def remove(self, key): 
        if key in self.children:
            del self.children[key]
            return True

        return False

 




"""
   def getTransactionIndex(self, order = 0, description = ""):
        if order > 0 and order <= len(self.transactions):
            return (order-1)

        elif description != "":
            #search or Decription, Note Descriptions are not unique
            for index, transaction in enumerate(self.transactions):
                if transaction.description == description:
                    return index
        
        return -1
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
        
    def print(self):
        for transaction in self.transactions:
            print("#", transaction.order, " Description", transaction.description, " Ammout: ", transaction.amount, "\n")

"""


    

