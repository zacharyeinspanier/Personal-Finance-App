import csv
import PyPDF2
import sys
import os
from collections import namedtuple


def StatementReader(PathToFile):

    fileName = PathToFile

    if fileName.endswith(".csv"):
        statement = parseCVS(fileName)
    else:
        sys.exit("This is not a .csv or .pdf file")
    
    statement = castAmount(statement)
    return statement


def castAmount(statement = []):

    for transaction in statement:
        if "Amount" in transaction:
            amount = float(transaction["Amount"])
            transaction["Amount"] = amount
    return statement


def parseCVS(fileName):
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


def parsePDF(fileName):    
    statement = ""
    pdfFileObj = open(fileName, 'rb')

    pdfReader = PyPDF2.PdfReader(pdfFileObj)

    numPages = len(pdfReader.pages)

    for i in range(numPages):
        pageObj = pdfReader.pages[i]
        statement += pageObj.extract_text()

    return statement
    
   
if __name__ == "__main__":
    main()