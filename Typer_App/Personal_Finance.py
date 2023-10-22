import sys
import argparse
import subprocess
import typer
import pickle
import os
from typing_extensions import Annotated

from .classes.account import *
from Scripts.StatementReader import StatementReader

accounts = []
app = typer.Typer(rich_markup_mode="rich")
PICKELFILE = "Pickel_Files\PersonalFinanceData.pkl"

"""    Statement
        Remove statement

"""
@app.command()
def CreateNewAccount(name: Annotated[str, typer.Argument(help="The name of the account")]):
    """
    This function adds a new account to the accounts list

    Prams:
        name: a string representing the name of the new account
    """
    if len(accounts) == 0:
        placement = 1
    else:
        placement = len(accounts) + 1

    newAccount = account(name, order = placement)
    accounts.append(newAccount)
    MemoryUpdate()
    return True

@app.command()
def DeletetAccount(placement: Annotated[int, typer.Argument(help="The account placement number.")]):
    """
    This function deletes an account from the accounts list, then updates the order for each account

    Prams:
        Placement: an integer representing the index of the account in the accounts list
    """
    if len(accounts) == 0:
        print("There ware no accounts to remove.")
        return False
    elif placement > len(accounts) or placement < 1:
        print("This is not a valid account to remove.")
        return False
    else:
        accounts[placement-1].delete()
        accounts.pop(placement-1)
        for i in range(placement-1, len(accounts)):
            accounts[i].order = i+1
        MemoryUpdate()
    return True

@app.command()
def PrintAccountContent(placement: Annotated[int, typer.Argument(help="The account placement number.")]):
    """
    This function prints out the contents of a specific account.

    Prams:
        Placement: an integer representing the index of the account in the accounts list
    """
    if len(accounts) == 0:
        print("There ware no accounts to print.")
        return False
    elif placement > len(accounts) or placement < 1:
        print("This is not a valid account to print.")
        return False
    else:
        print("============================")
        print("======",accounts[placement-1].accountName,"========")
        
        print("============================")
        for statement in  accounts[placement-1].statements:
            print("======",statement.statementName,"========")
            print("====== Total Deposit",statement.totalDeposit,"========")
            print("====== Totla Withdraw",statement.totalWithdraw,"========")
            print("====== Total Balance",statement.balance,"========")
            statement.print()
        
    return True

@app.command()
def PrintAccountList():
    """
    This function prints out each account name and order
    """
    if len(accounts) == 0:
        print("There are not accounts to print.")
    else:
        for account in accounts:
            print("# ", account.order," ", account.accountName)

@app.command()
def AddNewStatement(
    statementname: Annotated[str, typer.Argument(help="A name for the statement")] = "",
    pathtostatement: Annotated[str, typer.Argument(help="A file path to the statement")] = "", 
    accountplacement: Annotated[int, typer.Argument(help="The account placement number.")]= 0):
    """
    This function turns a .csv bank statement into a statement with a list of transactions. 
    This statement is attached to the account provided in prams

    Prams:
        statementname: string name for new statement
        pathtostatement: the string path to the statement file
        accountplacement: integer of the account to attach the statement to
    """

    if statementname == "" or pathtostatement == "" or accountplacement == 0:
        print("Arguments are not valid")
    elif not os.path.isfile(pathtostatement):
        print("This file does not exit in the os directory ", pathtostatement)
    else:
        newStatement = StatementReader(pathtostatement)
        accounts[accountplacement-1].createStatement(newStatement, name = statementname)
        MemoryUpdate()

@app.command()
def RemoveStatement(accountplacement: Annotated[int, typer.Argument(help="The account placement number.")]= 0,
    statementplacement: Annotated[int, typer.Argument(help="The statement placement number.")]= 0,
    statementname: Annotated[str, typer.Argument(help="A name for the statement")] = "" 
    ):
    """
    This function removes a statement from an account.

    Prams:
        accountplacement: integer representing the account to select
        statementplacement: integer representing the statement to remove
        statementname: string representing the name of the statement
    """

    if len(accounts) == 0:
        print("There are not accounts created")
    elif accountplacement > len(accounts) or accountplacement < 1:
        print("Placement provided is not valid")
    else:
        if statementplacement < 1 and statementname == "":
            print("The statment placement and name do not match a statement")
            return
        elif statementname == "" and (statementplacement > len(accounts[accountplacement-1].statements) or statementplacement < 1):
            print("Statement name and placement do not match a statement")
        else:
            res = accounts[accountplacement-1].removeStatement(order = statementplacement, name = statementname)
            if res:
                print("statement removed from account: ", accounts[accountplacement-1].accountName)
            else:
                print("failed to remove statement")
            MemoryUpdate()

@app.command()
def DeleteMemory():
    """
    This function deletes the contents of a memory file
    If the file does not exist or is empty -> return
    """
    if not os.path.isfile(PICKELFILE):
        print("Memory File has not been created.")
        return
    elif os.path.getsize(PICKELFILE) <= 0:
        print("Memory file is empty")
        return 
    else:
        with open(PICKELFILE, "r+") as picf:
            picf.truncate(0)
        return

@app.callback()
def LoadData():
    """
    This function loads data from the memory file to the list accounts
    If the file does not exist or is empty -> return 
    """
    global accounts
    dataFromLoad = []
    if not os.path.isfile(PICKELFILE):
        print("No memory file to load")
        return
    elif os.path.getsize(PICKELFILE) <= 0:
        print("Memory file is empty")
        return 
    else:
        with open(PICKELFILE, "rb") as picf:
            dataFromLoad = pickle.load(picf)
        print("Memory is loaded")
        accounts = dataFromLoad
    return 
 
def SaveData():
    """
    This function handles a memory save.
    It will create the memory file if it des not exist
    Then it will write the list account to the memory
    """
    if not os.path.isfile(PICKELFILE):
        f = open(PICKELFILE, "x")
        f.close()
        print("Memory file created")
    with open(PICKELFILE, "wb") as picf:
        pickle.dump(accounts, picf)
    print("Memory is saved")

def MemoryUpdate():
    """
    This function handels a memory update. 
    Memory file is cleared then data is written to the file
    """
    DeleteMemory()
    SaveData()

if __name__ == "__main__": 
    app()

