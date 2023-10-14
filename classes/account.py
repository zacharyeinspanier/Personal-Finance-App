from classes.statement import *
import array as arr 

class account:

    def __init__(self, accountName, order=0, statements = []):
        self.accountName = accountName
        self.statements = statements
        self.order = order

    def addStatement(self, statement):
        # check for dups
        if self.getStatementIndex(name = statement.statementName) == -1:
            statement.order = (len(self.statements) + 1)
            self.statements.append(statement)
            return True
        else:
            return False
    
    def removeStatement(self, order = 0, name = ""):
        if order == 0 and name == "":
            return False
        
        statementIndex = self.getStatementIndex(order, name)

        if statementIndex == -1:
            return False

        startOrder = self.statements[statementIndex].order
        # remove the item
        self.statements.pop(statementIndex)

        # change the order of the remaining items
        for i in range(statementIndex, len(self.statements)):
            self.statements[i].order = startOrder
            startOrder += 1

        return True

    def getStatementIndex(self, order = -1, name = ""):
        if order > 0 and order <= len(self.statements):
            return (order - 1)
        elif name != "":
            # serch for statment name
            for index, statement in enumerate(self.statements):
                if statement.statementName == name:
                    return index
        return -1

    def createStatement(self, transactions, name = "default"):
        newStatement = statement(name)
        newStatement.createTransActions(transactions)
        newStatement.sumBalance()
        self.addStatement(newStatement)
        
    def delete(self):
        while len(self.statements) > 0:
            deleteStmnt = self.statements.pop()
            deleteStmnt.delete()
            del deleteStmnt
    def print(self):
        for statement in self.statements:
            print("#", statement.order, " ", statement.statementName, "\n")
