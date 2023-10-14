import sys
import argparse
import subprocess
import typer
import pickle
import os
from typing_extensions import Annotated

from classes.account import *

accounts = []
app = typer.Typer()
PICKELFILE = "PersonalFinanceData.pkl"

"""    Statement
        Add statement
        Remove statement
        Print statement and transactions

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
        print("=========={accounts[placement-1].accountName}==========")
        print("============================")
        accounts[placement-1].print()
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

