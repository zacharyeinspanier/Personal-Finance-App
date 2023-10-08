from classes.account import *
from classes.category import *
from classes.statement import *
from classes.transaction import *

def main(): 

   
    if testTransaction():
        print("=========Test Transaction Pass=========")
    else:
        print("=========Test Transaction Failed=========")

    if testStatement():
        print("=========Test Statement Pass=========")
    else:
        print("=========Test Statement Failed=========")

    if testAccount():
        print("=========Test Account Pass=========")
    else:
        print("=========Test Account Failed=========")
    
    
    
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

    accountOne = account("accountOne", [])
    if accountOne.accountName != "accountOne":
        return False
    transactionOne = transaction("01/07/2023", "01:05:23", 700, "deposit", "This is a test")
    transactionTwo = transaction("01/08/2023", "01:05:23", 900, "deposit", "This is a test")
    transactionThree = transaction("01/09/2023", "01:05:23", -50, "withdraw", "This is a test")
    transactionFour = transaction("01/10/2023", "01:05:23", -100, "withdraw", "This is a test")
    transactionFive = transaction("01/11/2023", "01:05:23", 200, "deposit", "This is a test")
    statementOne = statement("statement One", [], 0,0,0)
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
def testStatement():
    res = True

    transactionOne = transaction("01/07/2023", "01:05:23", 700, "deposit", "This is a test")
    transactionTwo = transaction("01/08/2023", "01:05:23", 900, "deposit", "This is a test")
    transactionThree = transaction("01/09/2023", "01:05:23", -50, "withdraw", "This is a test")
    transactionFour = transaction("01/10/2023", "01:05:23", -100, "withdraw", "This is a test")
    transactionFive = transaction("01/11/2023", "01:05:23", 200, "deposit", "This is a test")
    statementOne = statement("statement One", [], 0,0,0)

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


if __name__ == "__main__":
    main()