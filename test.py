from classes.account import *
from classes.category import *
from classes.statement import *
from classes.transaction import *

def main(): 

   
    if testTransaction():
        print("=========Test Transaction Create Pass=========")
    else:
        print("=========Test Transaction Create Failed=========")

    if testStatement():
        print("=========Test Statement Add Pass=========")
    else:
        print("=========Test Statement Add Failed=========")

    if testStatementTransaction():
        print("=========Test Statement Remove Pass=========")
    else:
        print("=========Test Statement Remove Failed=========")

    if testAccount():
        print("=========Test Account Add Pass=========")
    else:
        print("=========Test Account Add Failed=========")

    if testAccountStatement():
        print("=========Test Account Remove Pass=========")
    else:
        print("=========Test Account Remove Failed=========")
    
    
    
def testTransaction():
    res = False

    transactionOne = transaction("01/07/2023", "01:05:23", 700, "deposit", "This is a test")
    if (transactionOne.date =="01/07/2023" and 
    transactionOne.time == "01:05:23" and 
    transactionOne.amount == 700 and 
    transactionOne.type == "deposit" and 
    transactionOne.description == "This is a test" ):
        res = True
    else:
        res = False
        return res
        

    transactionTwo = transaction("01/07/2023", "01:05:23", 900, "deposit", "This is a test")
    if (transactionTwo.date =="01/07/2023" and 
    transactionTwo.time == "01:05:23" and 
    transactionTwo.amount == 900 and 
    transactionTwo.type == "deposit" and 
    transactionTwo.description == "This is a test" ):
        res = True
    else:
        res = False
        return res
        
    return res

def testCategory():
    return True
def testAccount():
    res = True

    accountOne = account("accountOne", 0, [])
    if accountOne.accountName != "accountOne":
        return False
    transactionOne = transaction("01/07/2023", "01:05:23", 700, "deposit", "This is a test")
    transactionTwo = transaction("01/08/2023", "01:05:23", 900, "deposit", "This is a test")
    transactionThree = transaction("01/09/2023", "01:05:23", -50, "withdraw", "This is a test")
    transactionFour = transaction("01/10/2023", "01:05:23", -100, "withdraw", "This is a test")
    transactionFive = transaction("01/11/2023", "01:05:23", 200, "deposit", "This is a test")
    statementOne = statement("statement One", 0,0,0,0)
    statementOne.addTransaction(transactionOne)
    statementOne.addTransaction(transactionTwo)
    accountOne.addStatement(statementOne)
    accountOne.statements[0].addTransaction(transactionThree)
    accountOne.statements[0].addTransaction(transactionFour)
    accountOne.statements[0].addTransaction(transactionFive)
    accountOne.statements[0].sumDeposit()

    if accountOne.statements[0].totalDeposit != 1800:
        return False

    accountOne.statements[0].sumWithdraw()

    if accountOne.statements[0].totalWithdraw != -150:
        return False

    accountOne.statements[0].sumBalance()

    if accountOne.statements[0].balance != 1650:
        return False


    return res

def testAccountStatement():
    accountOne = account("accountOne",0, [])
    statementOne = statement("April-May 2023 Statement", 0,0,0,order = 0, transactions = [])
    statementTwo = statement("May-June 2023 Statement", 0,0,0,order = 0, transactions = [])
    statementThree = statement("June-July 2023 Statement", 0,0,0,order = 0, transactions = [])
    statementFour = statement("July-August 2023 Statement", 0,0,0,order = 0, transactions = [])
    statementFive = statement("August-September 2023 Statement", 0,0,0,order = 0, transactions = [])
    accountOne.addStatement(statementOne)
    accountOne.addStatement(statementTwo)
    accountOne.addStatement(statementThree)
    accountOne.addStatement(statementFour)
    accountOne.addStatement(statementFive)

    if len(accountOne.statements) != 5:
        return False
    
    accountOne.removeStatement(3)

    if len(accountOne.statements) != 4:
        return False

    accountOne.removeStatement(name="April-May 2023 Statement")

    if len(accountOne.statements) != 3:
        return False
    return True


def testStatement():
    res = True

    transactionOne = transaction("01/07/2023", "01:05:23", 700, "deposit", "This is a test")
    transactionTwo = transaction("01/08/2023", "01:05:23", 900, "deposit", "This is a test")
    transactionThree = transaction("01/09/2023", "01:05:23", -50, "withdraw", "This is a test")
    transactionFour = transaction("01/10/2023", "01:05:23", -100, "withdraw", "This is a test")
    transactionFive = transaction("01/11/2023", "01:05:23", 200, "deposit", "This is a test")
    statementOne = statement("statement One", 0,0,0, order = 0, transactions = [])

    if statementOne.statementName != "statement One":
        return False

    statementOne.addTransaction(transactionOne)
    statementOne.addTransaction(transactionTwo)
    statementOne.addTransaction(transactionThree)
    statementOne.addTransaction(transactionFour)
    statementOne.addTransaction(transactionFive)
    statementOne.sumDeposit()

    if statementOne.totalDeposit != 1800:
       return False

    statementOne.sumWithdraw()

    if statementOne.totalWithdraw != -150:
       return False

    statementOne.sumBalance()

    if statementOne.balance != 1650:
       return False
    
    return res

def testStatementTransaction():
    res = True

    transactionOne = transaction("01/07/2023", "01:05:23", 700, "deposit", "This is a test One")
    transactionTwo = transaction("01/08/2023", "01:05:23", 900, "deposit", "This is a test Two")
    transactionThree = transaction("01/09/2023", "01:05:23", -50, "withdraw", "This is a test Three")
    transactionFour = transaction("01/10/2023", "01:05:23", -100, "withdraw", "This is a test Four")
    transactionFive = transaction("01/11/2023", "01:05:23", 200, "deposit", "This is a test Five")
    statementOne = statement("statement One", 0,0,0, order = 0, transactions = [])

    if statementOne.statementName != "statement One":
        return False

    statementOne.addTransaction(transactionOne)
    statementOne.addTransaction(transactionTwo)
    statementOne.addTransaction(transactionThree)
    statementOne.addTransaction(transactionFour)
    statementOne.addTransaction(transactionFive)

    if len(statementOne.transactions) != 5:
        return False
    
    statementOne.removeTransaction(order = 2)
    
    if len(statementOne.transactions) != 4:
        return False
    
    statementOne.removeTransaction(description= "This is a test Four")

    if len(statementOne.transactions) != 3:
        return False

    
    return res

if __name__ == "__main__":
    main()