from classes.statement import *

class account:

    def __init__(self, accountName, statements):
        self.accountName = accountName
        self.statements = statements

    def addStatement(self, statement):
        self.statements.append(statement)
    
    def removeStatement(self):
        return 0 #TODO
