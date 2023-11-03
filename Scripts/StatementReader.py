import csv
import PyPDF2
import sys
import os
from collections import namedtuple


def StatementReader(PathToFile):
    """
    This function takes a .csv file and parsces it into a dictionary

    PathToFile(str): path to .csv file
    """

    fileName = PathToFile

    if fileName.endswith(".csv"):
        statement = parseCVS(fileName)
    else:
        sys.exit("This is not a .csv or .pdf file")
    
    statement = castAmount(statement)
    return statement


def castAmount(statement = []):
    """
    This function find the ammount key in a dictionary and casts it to a float

    statement: dictionary with key and values
    """

    for transaction in statement:
        if "Amount" in transaction:
            amount = float(transaction["Amount"])
            transaction["Amount"] = amount
    return statement


def parseCVS(fileName):
    """
    This function Takes a csv file and parces it into a list of dictionarys
    
    fileName(str): path to .csv file
    """

    statement = []
    # open and reading csv
    try:
        with open(fileName, 'r') as file:
            header = []
            # remove spaces
            for key in next(file).split(","):
                header.append(key.strip())
            # create dictoaries using stripped header
            reader = csv.DictReader(file, fieldnames=header)

            for row in reader:
                statement.append(row)
                
    except OSError as e:
        print(e)
        return None
       
    return statement



    
