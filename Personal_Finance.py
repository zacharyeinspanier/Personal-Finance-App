import csv
import PyPDF2
import sys
from collections import namedtuple


def main():
    # usage python <filename> <filetype>
    if len(sys.argv) != 2:
        sys.exit("Usage: python Personal_Finance.py <filename>")

    fileName = sys.argv[1]
 
    fileType = namedtuple("fileType", ["fileName", "endsWith", "statement"])

    if fileName.endswith(".csv"):
        statement = parseCVS(fileName)
        file = fileType(fileName, "csv", statement) # is this needed
    else:
        sys.exit("This is not a .csv or .pdf file")
    
    newStat = castAmount(file.statement)
    print(newStat)
    # the next step is to take the statment and separate it to withdraw and deposit
    # do addition and save the file


def castAmount(statement = []):

    for transaction in statement:
        if "Amount" in transaction:
            amount = float(transaction["Amount"])
            transaction["Amount"] = amount
    return statement


def parseCVS(fileName):
    statement = []
    # open and reading csv
    with open(fileName, 'r') as file:
        header = []
        # remove spaces
        for key in next(file).split(","):
            header.append(key.strip())
        # create dictoaries using stripped header
        reader = csv.DictReader(file, fieldnames=header)

        for row in reader:
            statement.append(row)
       
    return statement


def parsePDF(fileName):    
    statement = ""
    pdfFileObj = open(fileName, 'rb')

    pdfReader = PyPDF2.PdfReader(pdfFileObj)

    numPages = len(pdfReader.pages)

    for i in range(numPages):
        pageObj = pdfReader.pages[i]
        statement += pageObj.extract_text()
        
    print(statement)
    # how do I turn this into a list?
    # pdfquery 
    #elif fileName.endswith(".pdf"):
#parsePDF(fileName)
#file = fileType(fileName, "pdf")
    return statement
    
   
if __name__ == "__main__":
    main()