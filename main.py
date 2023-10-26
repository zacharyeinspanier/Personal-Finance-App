# Form implementation generated from reading ui file 'Personal_Finance_Main.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog
import argparse
import sys
import os

from classes.PFTreeNode import treeNode
from Pickel.PickelHelpers import LoadData, MemoryUpdate
from Scripts.StatementReader import StatementReader

parser = argparse.ArgumentParser(
                    prog='Personal Finance App',
                    description='Enter bank statements for tracking spending',
                    epilog='Usage: python main.py --data=[new | load] --file = [pickel file].pkl')

parser.add_argument("--data", choices = ["new", "load"], default = "new") 
parser.add_argument("--pfile", default = "Pickel/newPickelFile.pkl") 


HTML =  ["<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\np, li { white-space: pre-wrap; }\nhr { height: 1px; border-width: 0; }\nli.unchecked::marker { content: \"\\2610\"; }\nli.checked::marker { content: \"\\2612\"; }\n</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; text-decoration: underline;\">","</span></p></body></html>"]


class Ui_MainWindow(object):

    def __init__(self, savePfile, manager = None ):
        self.manager = manager
        self.savePfile = savePfile
        self.listHtml = HTML[0] + self.manager.type + " " + self.manager.name + " List" + HTML[1]
        self.titleHtml = HTML[0] + "Personal Finance" + HTML[1]

    def setupUi(self, MainWindow):
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
        self.title.setGeometry(QtCore.QRect(350, 30, 281, 71))
        self.title.setObjectName("title")

        self.addBtn = QtWidgets.QPushButton(parent=self.centralwidget) 
        self.addBtn.setGeometry(QtCore.QRect(470, 520, 221, 71))

        self.backBtn = QtWidgets.QPushButton(parent=self.centralwidget) 
        self.backBtn.setGeometry(QtCore.QRect(40, 620, 221, 71))

        self.saveBtn = QtWidgets.QPushButton(parent=self.centralwidget) 
        self.saveBtn.setGeometry(QtCore.QRect(40, 320, 221, 71))

        self.browseBtn = QtWidgets.QPushButton(parent=self.centralwidget) 
        self.browseBtn.setGeometry(QtCore.QRect(700, 320, 221, 71))

        self.inputName = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.inputName.setGeometry(QtCore.QRect(270, 520, 191, 71))
        self.inputName.setPlaceholderText("Enter a name")

        self.message = QtWidgets.QLabel(parent=self.centralwidget)
        self.message.setGeometry(QtCore.QRect(665, 680, 400, 25))
        self.message.setObjectName("messageText")


        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)

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
        

        self.browseBtn.setFont(font)
        self.browseBtn.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.browseBtn.setIconSize(QtCore.QSize(19, 19))
        self.browseBtn.setObjectName("browseFolders")
        self.browseBtn.clicked.connect(self.browseFiles)

        self.inputName.setFont(font)
        self.inputName.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.inputName.setMaxLength(30)
        self.inputName.setObjectName("inputTextName")
       

        self.listTitle = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.listTitle.setGeometry(QtCore.QRect(325, 190, 350, 71))
        self.listTitle.setObjectName("listTitle")
        self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(350, 290, 256, 192))
        self.listWidget.setStyleSheet("font: 22pt \"Segoe UI\";\n"
"background-color: rgb(255, 255, 255)")
        self.listWidget.setObjectName("listWidget")
        self.listWidget.itemClicked.connect(self.listClick)
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
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setHtml(_translate("MainWindow", self.titleHtml))

        self.addBtn.setText(_translate("MainWindow", "Add Bank Account"))

        self.backBtn.setText(_translate("MainWindow", "Go Back"))

        self.saveBtn.setText(_translate("MainWindow", "SaveData"))

        self.browseBtn.setText(_translate("MainWindow", "Open File"))

        self.listTitle.setHtml(_translate("MainWindow", self.listHtml))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.update()
    
    


    def addButton(self):

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
            parent = self.manager
            )
        res = self.manager.add(childNode)

        if not res:
            self.message.setText("This name alread exists in the " + nameFromInput + " list. Enter a new name." )
        else: 
            self.message.setText("Successfully added " + nameFromInput + " to list.")

        self.inputName.clear()
        self.displayList()
   
    def displayList(self):
        """
        This function prints the items to the list widget.

        TODO: current the item text is set for each item every time function is called
            Find a way to only add 1 time to the end of the list widget
        """
        _translate = QtCore.QCoreApplication.translate
        for i, key in enumerate(self.manager.children.keys()):
            item = QtWidgets.QListWidgetItem() #create item
            self.listWidget.addItem(item) # add item to list
            item = self.listWidget.item(i) # get the item
            item.setText(_translate("MainWindow", self.manager.children[key].name))# set item text
    
    def listClick(self, item):
        # as items are deleted need to re structure the keys
        # or need a way to consistantly get keys
        
        
        key = item.text()
        if key in self.manager.children:
            #NEED TO FIX
            if self.manager.children[key].type == "SingleTransaction":
                return False
            self.manager = self.manager.children[key] # this is not an object it is a dictionary
            self.update()
            return True
        return False


    def backButton(self):
        if self.manager.parent != None:
            self.manager = self.manager.parent
            self.update()
            return True

        return False

    def update(self):
        _translate = QtCore.QCoreApplication.translate
        self.addBtn.setText(_translate("MainWindow", "Add " + self.getChildType()))
        self.listHtml = self.listHtml = HTML[0] + self.manager.type + " " + self.manager.name + " List" + HTML[1]
        self.listTitle.setHtml(_translate("MainWindow", self.listHtml))
        self.listWidget.clear()
        self.inputName.clear()
        self.message.clear()
        self.displayList()
        self.updateWidgets()
    
    def updateWidgets(self):
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
        self.addBtn.show()
        self.browseBtn.hide()
        self.inputName.show()
        self.listTitle.show()
        self.listWidget.show()
        return
    def stateStatement(self):
        self.addBtn.show()
        self.browseBtn.hide()
        self.inputName.show()
        self.listTitle.show()
        self.listWidget.show()
        return
    def stateTransactions(self):
        self.addBtn.hide()
        self.browseBtn.show()
        self.inputName.hide()
        self.listTitle.show()
        self.listWidget.show()
        return
    def stateSingleTransaction(self):
        self.addBtn.hide()
        self.browseBtn.hide()
        self.inputName.hide()
        self.listTitle.show()
        self.listWidget.hide()
        return



    def getChildType(self):
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
    
    def saveToPKL(self):
        root = self.manager
        rootParent = self.manager.parent

        while rootParent != None:
            root = root.parent
            rootParent = root.parent
        
        if root != None and MemoryUpdate(self.savePfile, root):
            self.message.setText("Successfully saved data to " + self.savePfile)
        else:
            self.message.setText("Failed to saved data to " + self.savePfile)

    def browseFiles(self):
        dlg = QtWidgets.QFileDialog()
        fileName = ""
        if dlg.exec():
            fileName = dlg.selectedFiles()

        if ".csv" not in fileName[0]:
            self.message.setText("Failed to open File. Not CSV file")
            return
        
        self.addTransactions( fileName[0])

    def addTransactions(self, fileName):
        transactions = StatementReader(fileName)        
        nodeType = self.getChildType()
        count = 0
        for transaction in transactions:
            key = "#" + str(count) + " "
            if "Date" in transaction:
                key += transaction["Date"]
            elif "date"  in transaction:
                key += transaction["date"]
            
            childNode = treeNode(
            name = key, 
            withdraw = 0,
            deposit = 0, 
            balance = 0,
            type = nodeType, 
            children = transaction,
            parent = self.manager
            )
            
            self.manager.children[key] = childNode
            count +=1
        self.displayList()
        return

            



def closeApp(app, manager, pfile):
    app.exec()
    # save data to pickle file
    if manager != None:
        MemoryUpdate(pfile, manager)


if __name__ == "__main__":


    startUpManager = None
    args = parser.parse_args()
    if ".pkl" not in args.pfile:
        sys.exit("The file entered is not a pickel file.")
    pfile = args.pfile

    # Load pickel
    if args.data == "load" :
        startUpManager = LoadData(pfile)
        if startUpManager == None or not isinstance(startUpManager, treeNode):
            sys.exit("Pickel file does not have readable data")
    #Create new manager
    elif args.data == "new":
        startUpManager = treeNode(
            name = "Personal Finance Manager", 
            withdraw = 0,
            deposit = 0, 
            balance = 0,
            type = "Bank Accounts",
            children = {},
            parent = None
        )
    else:
        sys.exit("Please enter new or load for data.")
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(manager = startUpManager, savePfile = pfile)
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(closeApp(app, startUpManager, pfile))
    
