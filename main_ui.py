from PyQt6 import QtCore, QtGui, QtWidgets
import argparse
import sys
import os

from classes.PFTreeNode import treeNode
from Pickel.PickelHelpers import LoadData, MemoryUpdate
from Scripts.StatementReader import StatementReader
from Rename_ui import Rename_UI

HTML =  ["<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\np, li { white-space: pre-wrap; }\nhr {  border:0;}\nli.unchecked::marker { content: \"\\2610\"; }\nli.checked::marker { content: \"\\2612\"; }\n</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; text-align: center; border : 0px;\"><span style=\" font-size:22pt; text-decoration: underline; text-align: center;\">","</span></p></body></html>"]

HTML_TRANSACTION =  ["<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\np, li { white-space: pre-wrap; }\nhr {  border:0;}\nli.unchecked::marker { content: \"\\2610\"; }\nli.checked::marker { content: \"\\2612\"; }\n</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; border : 0px;\"><span style=\" font-size:14pt;\">","</span></p></body></html>"]

BTN_Y_POS = 600
MID_DISP_X_POS = 350 
TITLE_TABLE_LEN = 500
TITLE_TABEL_X_POS = 250
WDB_X_POS = 200
WDB_Y_POS = 200

class Ui_MainWindow(object):
    """
    This class is the user interface for displaying information about all treeNodes.

    manager: The current treeNode to display
    savePfile: Path of save pickel file
    listHtml: The inner HTML to diplay for the list title
    titleHtml: The inner HTML to display for the app title
    """


    def __init__(self, savePfile, manager = None ):
        self.manager = manager
        self.savePfile = savePfile
        self.listHtml = HTML[0] + self.manager.type + " " + self.manager.name + " List" + HTML[1]
        self.titleHtml = HTML[0] + "Personal Finance" + HTML[1]

    def setupUi(self, MainWindow):
        """
        This function declares and sets all of the widgest for the UI. 
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(977, 721)
        MainWindow.setStyleSheet("background-color: rgb(229, 229, 229)")

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 981, 131))
        self.widget.setStyleSheet("background-color: rgb(255, 110, 43)")
        self.widget.setObjectName("widget")

        self.title = QtWidgets.QTextEdit(parent=self.widget)
        self.title.setGeometry(QtCore.QRect(MID_DISP_X_POS, 30, 281, 71))
        self.title.setObjectName("title")
        self.title.setStyleSheet("border: 0px")

        self.addBtn = QtWidgets.QPushButton(parent=self.centralwidget) 
        self.addBtn.setGeometry(QtCore.QRect(470, 520, 221, 71))

        self.backBtn = QtWidgets.QPushButton(parent=self.centralwidget) 
        self.backBtn.setGeometry(QtCore.QRect(40, BTN_Y_POS, 221, 71))

        self.saveBtn = QtWidgets.QPushButton(parent=self.centralwidget) 
        self.saveBtn.setGeometry(QtCore.QRect(260, BTN_Y_POS, 221, 71))

        self.removeBtn = QtWidgets.QPushButton(parent=self.centralwidget) 
        self.removeBtn.setGeometry(QtCore.QRect(480, BTN_Y_POS, 221, 71))

        self.browseBtn = QtWidgets.QPushButton(parent=self.centralwidget) 
        self.browseBtn.setGeometry(QtCore.QRect(700, BTN_Y_POS, 221, 71))

        self.editTitle = QtWidgets.QPushButton(parent=self.centralwidget) 
        self.editTitle.setGeometry(QtCore.QRect(875, 133, 100, 50))

        self.inputName = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.inputName.setGeometry(QtCore.QRect(290, 520, 191, 71))
        self.inputName.setPlaceholderText("Enter a name")

        self.message = QtWidgets.QLabel(parent=self.centralwidget)
        self.message.setGeometry(QtCore.QRect(375, 680, 400, 25))
        self.message.setObjectName("messageText")

        self.withdraw = QtWidgets.QLabel(parent=self.centralwidget)
        self.withdraw.setGeometry(QtCore.QRect(WDB_X_POS, WDB_Y_POS, 200, 100))
        self.withdraw.setObjectName("WithdrawText")

        self.deposit = QtWidgets.QLabel(parent=self.centralwidget)
        self.deposit.setGeometry(QtCore.QRect(WDB_X_POS+250, WDB_Y_POS, 200, 100))
        self.deposit.setObjectName("DepositText")

        self.balance = QtWidgets.QLabel(parent=self.centralwidget)
        self.balance.setGeometry(QtCore.QRect(WDB_X_POS+500, WDB_Y_POS, 200, 100))
        self.balance.setObjectName("BalanceText")

        self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(MID_DISP_X_POS, 290, 256, 192))
        self.listWidget.setObjectName("listWidget")

        self.transactionDisplay = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.transactionDisplay.setGeometry(QtCore.QRect(MID_DISP_X_POS, 290, 350, 200))
        self.transactionDisplay.setObjectName("transactionDisplay")

        self.transactionTable = QtWidgets.QTableWidget(parent=self.centralwidget) 
        self.transactionTable.setGeometry(QtCore.QRect(TITLE_TABEL_X_POS, 290, TITLE_TABLE_LEN, 275))
        self.transactionTable.setObjectName("transactionTable")

        self.listTitle = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.listTitle.setGeometry(QtCore.QRect(TITLE_TABEL_X_POS, 150, TITLE_TABLE_LEN, 70))
        self.listTitle.setObjectName("listTitle")
        self.listTitle.setStyleSheet("border: 0px")


        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)

        font_message = QtGui.QFont()
        font_message.setPointSize(10)
        font_message.setBold(True)

        self.message.setFont(font_message)

        self.addBtn.setFont(font)
        self.addBtn.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.addBtn.setIconSize(QtCore.QSize(19, 19))
        self.addBtn.setObjectName("addButton")
        self.addBtn.clicked.connect(self.addButton)

        self.backBtn.setFont(font)
        self.backBtn.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.backBtn.setIconSize(QtCore.QSize(19, 19))
        self.backBtn.setObjectName("backButton")
        self.backBtn.clicked.connect(self.backButton)

        self.saveBtn.setFont(font)
        self.saveBtn.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.saveBtn.setIconSize(QtCore.QSize(19, 19))
        self.saveBtn.setObjectName("addButton")
        self.saveBtn.clicked.connect(self.saveToPKL)
        
        self.removeBtn.setFont(font)
        self.removeBtn.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.removeBtn.setIconSize(QtCore.QSize(19, 19))
        self.removeBtn.setObjectName("removeButton")
        self.removeBtn.clicked.connect(self.removeButton)

        self.browseBtn.setFont(font)
        self.browseBtn.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.browseBtn.setIconSize(QtCore.QSize(19, 19))
        self.browseBtn.setObjectName("browseFolders")
        self.browseBtn.clicked.connect(self.browseFiles)

        self.editTitle.setFont(font)
        self.editTitle.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.editTitle.setIconSize(QtCore.QSize(19, 19))
        self.editTitle.setObjectName("editTitle")
        self.editTitle.clicked.connect(self.editListTitle)

        self.inputName.setFont(font)
        self.inputName.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.inputName.setMaxLength(30)
        self.inputName.setObjectName("inputTextName")

        self.withdraw.setFont(font)
        self.deposit.setFont(font)
        self.balance.setFont(font)
       
        
        self.listWidget.setStyleSheet("font: 22pt \"Segoe UI\";\n" "background-color: rgb(255, 255, 255)")
        self.listWidget.itemClicked.connect(self.listClick)

        self.transactionTable.itemClicked.connect(self.listClick)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 977, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """
        This function sets the inner text for all of the widgest for the UI. 
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setHtml(_translate("MainWindow", self.titleHtml))
        self.listTitle.setHtml(_translate("MainWindow", self.listHtml))

        self.listTitle.setReadOnly(True)
        self.title.setReadOnly(True)
        self.transactionDisplay.setReadOnly(True)

        self.addBtn.setText(_translate("MainWindow", "Add Bank Account"))
        self.backBtn.setText(_translate("MainWindow", "Go Back"))
        self.saveBtn.setText(_translate("MainWindow", "SaveData"))
        self.browseBtn.setText(_translate("MainWindow", "Open File"))
        self.removeBtn.setText(_translate("MainWindow", "Remove"))
        self.editTitle.setText(_translate("MainWindow", "Edit"))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.update()
    
    def update(self):
        """
        This function handels any updates to the widgets displayed. 
        """
        
        # close open window
        if hasattr(self,"renameListWindow"):
            self.renameListWindow.close()
        
        self.inputName.clear() 
        _translate = QtCore.QCoreApplication.translate
        #set text for titles
        self.addBtn.setText(_translate("MainWindow", "Add " + self.getChildType())) 
        self.listHtml = self.listHtml = HTML[0] + self.manager.name + HTML[1] 
        self.listTitle.setHtml(_translate("MainWindow", self.listHtml))
        self.updateListDisplay() 

        if self.manager.type != "SingleTransaction":
            self.manager.sum()
            # if any child not is not summed update hasSum of current node
        #set text for float display
        self.withdraw.setText("Withdraw: " + str('{:,.2f}'.format(self.manager.withdraw)))
        self.deposit.setText("Deposit: " + str('{:,.2f}'.format(self.manager.deposit)))
        self.balance.setText("Balance: " + str('{:,.2f}'.format(self.manager.balance)))
        
        
        #This will be depended on state
        match self.manager.type:
            case "Bank Accounts":
                self.stateAccout()
            case "Account":
                self.stateAccout()
            case "Statement":
                self.stateStatement()
            case "Transactions":
                self.stateTransactions()
            case "SingleTransaction":
                self.stateSingleTransaction()
            case _:
                return
        return

    def stateAccout(self):
        """
        This function set the windgest to display for state Account
        """
        #hide
        self.browseBtn.hide()
        self.transactionDisplay.hide()
        self.transactionTable.hide()
        #show
        self.addBtn.show()
        self.inputName.show()
        self.listTitle.show()
        self.listWidget.show()
        
    def stateStatement(self):
        """
        This function set the windgest to display for state Statement
        """
        #hide
        self.browseBtn.hide()
        self.transactionDisplay.hide()
        self.transactionTable.hide()
        #show
        self.addBtn.show()
        self.inputName.show()
        self.listTitle.show()
        self.listWidget.show()
        
    def stateTransactions(self):
        """
        This function set the windgest to display for state Transactions
        """
        #hide
        self.addBtn.hide()
        self.transactionDisplay.hide()
        self.listWidget.hide()
        self.inputName.hide()
        #show
        self.browseBtn.show()
        self.listTitle.show()
        self.transactionTable.show()

    def stateSingleTransaction(self):
        """
        This function set the windgest to display for state singleTransaction
        """
        #hide
        self.addBtn.hide()
        self.browseBtn.hide()
        self.inputName.hide()
        self.listWidget.hide()
        self.transactionTable.hide()
        #show
        self.transactionDisplay.show()
        self.listTitle.show()
    
    def updateListDisplay(self):
        """
        This function prints the items to the list widget.
        """
        self.listWidget.clear() 
        self.transactionDisplay.clear()
        self.transactionTable.clear()
        _translate = QtCore.QCoreApplication.translate
        # Display for SingleTransaction
        if self.manager.type == "SingleTransaction":
            innerText = "" 
            for key in self.manager.children.keys(): 
                innerText += str(key) + ": " + str(self.manager.children[key]) + "<br>"

            transaction_display = HTML_TRANSACTION[0]+ innerText + HTML_TRANSACTION[1]
            self.transactionDisplay.setText(_translate("MainWindow", transaction_display))
        # Display for Transactions
        elif self.manager.type == "Transactions":
            if len(self.manager.children) == 0:
                self.transactionTable.setRowCount(0) # this is the length of the list
                self.transactionTable.setColumnCount(0) #this is the length of the keys   
                return
            else:
                row = 0
                col = 0

                allTransactions = list(self.manager.children.keys())
                colCount = len(self.manager.children[allTransactions[0]].children)
                colNames = list(self.manager.children[allTransactions[0]].children.keys())
                colNames.insert(0, "Transaction Name")   
                        
                self.transactionTable.setRowCount(len(self.manager.children))
                self.transactionTable.setColumnCount(colCount+1) 
                self.transactionTable.setHorizontalHeaderLabels(colNames)

                for dict in self.manager.children:
                    self.transactionTable.setItem(row, col, QtWidgets.QTableWidgetItem(dict))
                    col+=1
                    for key in self.manager.children[dict].children:
                        dict_item = self.manager.children[dict].children[key]
                        self.transactionTable.setItem(row, col, QtWidgets.QTableWidgetItem(str(dict_item)))
                        col += 1
                    row += 1
                    col = 0
        # Display for list         
        else:
            for i, key in enumerate(self.manager.children.keys()):
                item = QtWidgets.QListWidgetItem() 
                self.listWidget.addItem(item) 
                item = self.listWidget.item(i) 
                item.setText(_translate("MainWindow", self.manager.children[key].name))

    
    def addButton(self):
        """
        This function handes the addition of a new treeNode
        """

        if self.manager.type == "SingleTransaction":
            self.message.setText("Error: Cannot add from here")
            return

        nameFromInput = self.inputName.text()

        if nameFromInput == "":
            self.message.setText("Error: The name field is empty.")
            return

        nodeType = self.getChildType()
        childNode = treeNode(
            name = nameFromInput, 
            withdraw = 0,
            deposit = 0, 
            balance = 0,
            type = nodeType, 
            children = {},
            parent = self.manager,
            )
        res = self.manager.add(childNode)

        if not res:
            self.message.setText("This name alread exists in the " + nameFromInput + " list. Enter a new name." )
        else: 
            self.message.setText("Successfully added " + nameFromInput + " to list.")

        self.update()
    
    def listClick(self, item):
        """
        This function handels user click on a list item
        """
        self.message.clear()
        if self.manager.type == "Transactions": 
            keyItem = self.transactionTable.item(item.row(), 0)
            if keyItem is None:
                return
            key = keyItem.text()
        else:
            key = item.text()
        if key in self.manager.children:
            self.manager = self.manager.children[key]
            self.update()
    
    def backButton(self):
        """
        This function handels user click on a back button
        """
        if self.manager.parent != None:
            self.manager = self.manager.parent
            self.message.clear()
            self.update()
        else:
            self.message.setText("Error: no previous page.")

    def removeButton(self):
        """
        This function handels user click on a remove button
        """
        if self.manager.parent is not None:
            self.manager.removeChildren()
            manager_pointer = self.manager
            self.manager = self.manager.parent
            del self.manager.children[manager_pointer.name]
            del manager_pointer
            self.update()
        else:
            self.message.setText("Error: nothing to remove.")
    
    def editListTitle(self):
        """
        This function handels user click on a edit button
        Opens new UI for display
        """
        self.renameListWindow = QtWidgets.QWidget()
        self.renameUI = Rename_UI(parent = self)
        self.renameUI.setupUi(self.renameListWindow)
        self.renameListWindow.show()
    
    def changeListName(self, newName = ""):
        """
        This function changes the name of the current treeNode
        """
        if self.manager.parent != None:
            self.manager.parent.children[newName] = self.manager.parent.children.pop(self.manager.name)
        self.manager.name = newName
        self.update()

        return 0


    def getChildType(self):
        """
        This function return the next type of tree node to create
        """
        nodeType = ""
        match self.manager.type:
            case "Bank Accounts":
                nodeType = "Account"
            case "Account":
                nodeType = "Statement"
            case "Statement":
                nodeType = "Transactions"
            case "Transactions":
                nodeType = "SingleTransaction"
            case _:
                nodeType = "No more Children Allowed"
        return nodeType
    
    def browseFiles(self):
        """
        This function allows the user to select a new .csv file to parse 
        """
        dlg = QtWidgets.QFileDialog()
        fileName = ""
        if dlg.exec():
            fileName = dlg.selectedFiles()


        if len(fileName) <= 0 or fileName == "" or ".csv" not in fileName[0]:
            self.message.setText("Failed to open File. Not CSV file")
            return
        
        self.addTransactions(fileName[0])

    def addTransactions(self, fileName):
        """
        This function handels the parsing and entry of each new transaction

        fileName(str): path of the file to parse
        """
        transactions = StatementReader(fileName)        
        nodeType = self.getChildType()
        count = len(self.manager.children) + 1
        
        for transaction in transactions:
            key = "#" + str(count)

            transactionWithdraw = 0
            transactionDeposit = 0

            if "Amount" in transaction:
                amount =  transaction["Amount"]
            elif "amount"  in transaction:
                amount = transaction["amount"]

            if amount >= 0:
                transactionDeposit = float(amount)
            else:
                transactionWithdraw = float(amount)

            transactionBalance = transactionWithdraw + transactionDeposit
            
            
            childNode = treeNode(
            name = key, 
            withdraw = float(transactionWithdraw),
            deposit = float(transactionDeposit), 
            balance = float(transactionBalance),
            type = nodeType, 
            children = transaction,
            parent = self.manager,
            )
            if key not in self.manager.children.keys():
                self.manager.children[key] = childNode
                count +=1
        self.manager.hasTransaction = True
        self.update()
        return

    def saveToPKL(self):
        """
        This function handels the savedata button press
        """
        root = self.manager
        rootParent = self.manager.parent

        while rootParent != None:
            root = root.parent
            rootParent = root.parent
        
        if root != None and MemoryUpdate(self.savePfile, root):
            self.message.setText("Successfully saved data to " + self.savePfile)
        else:
            self.message.setText("Failed to saved data to " + self.savePfile)
