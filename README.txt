Description:
This python application allows users to input their bank statments(csv) to track their spending. People often have a few different accounts for their finincal needs (EX: savings, checking, credit). 
The user can create multiple accound a submit their mmonthy statments for each account. For security, this is a local desktop application to keep bank account information local. 

This application will do the following wiht user bank statements:
    1. Allow user to create create multiple accounts
    2. Allow user to add statments to an account
    3. Allow user to name the statment, EX: "May-June 2023"
    4. Display all transactions for the statment
    5. Sum total with drawls and deposits
    6. Genorate a file to save all statmens in the app. Can be use later when adding additional statments

How To use App:

python main.py --data=[new or load] --pfile=[file path]

    --data:
        new[default]: a new save file to store personal finance data
        load: load from a save file 
    
    --pfile:
        path to file EX: C:\personal_finance\myPersonalFinance.pkl
        Must be a pickle file ending with pkl.
        To create a new file, specify the path and file. The program will create a file. 
        EX: C:\personal_finance\nonExistantFile.pkl
        default = Pickel/newPickelFile.pkl
    
