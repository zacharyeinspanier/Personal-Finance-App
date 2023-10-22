# Form implementation generated from reading ui file 'Personal_Finance_Main.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets

from classes.PFTreeNode import treeNode
from Pickel.PickelHelpers import LoadData, MemoryUpdate


"""
Ideas:
    Use same window but just update the names and display based on what the user clicks
        Update title
        update button connection
        update the manager
            Dictionary of objets
            {account: statementManager}
            {statment: transactionManager}
            self.manager will be chnaged to the correct manager depending on clicks
        
        When an account is clicked in the list, all of the objects are:
            1: manager becomes the account[i] manager
            2: item names are set to be the account manager items
        Data type could be a tree to enable back button
        EX
                        All accounts
                            |
                        [lsit of all accounts]
                            |   |   |
                            [List of statements]
                            |   |   |
                            [List of transactions]
        Each object would have the current object, a parent, and list of children
        On list item click-> Item becomes the manager and all ui objects are updated to match this item
        on back button click-> the partent becomes the manager and all ui objects are updated to match partent

        4 classes:
            1: All accounts manager
            2: account manager
            3: statment manager
            4: transaction manager
        classes prams:
            self.parent: single object
            self. children: list of objects
            self. title
            self. list title
        
        How do we update the UI??
        Need to be updated:
            Title text-> textEdit and textEdit_2
                Only update the inner text
            List widget -> listWidget
                update all times that are being displayed, can be done when the manager is updated
                change will be simple becuse using manager
                *** TRIGGER UPDATE: click on list will update everything
            Add button -> addAccount
                Update inner text
                Update the connection
                Change will be simple because using manager
            Back button -> back
                Update inner text
                Update the connection
                *** TRIGGER UPDATE: click on button will update everything
        
        List item clicked function:
            Set partent to manager
            set manager to item clicked
            update:
                back button
                titles
                add button
        Back button clicked function:
            set manager to partent
            set partement to manager.parent
            update:
                back button
                titles
                add button

                    
"""

HTML =  ["<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\np, li { white-space: pre-wrap; }\nhr { height: 1px; border-width: 0; }\nli.unchecked::marker { content: \"\\2610\"; }\nli.checked::marker { content: \"\\2612\"; }\n</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; text-decoration: underline;\">","</span></p></body></html>"]
PICKELFILE = "PersonalFinanceData.pkl"

class Ui_MainWindow(object):

    def __init__(self, manager = None):
        self.parent = None
        self.manager = manager
        self.count = 0
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
        self.addBtn.setGeometry(QtCore.QRect(360, 520, 221, 71))

        self.backBtn = QtWidgets.QPushButton(parent=self.centralwidget) 
        self.backBtn.setGeometry(QtCore.QRect(40, 620, 221, 71))

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

        self.listTitle.setHtml(_translate("MainWindow", self.listHtml))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.update()
    
    


    def addButton(self):
        nodeType = self.getChildType()
        
        childNode = treeNode(
            name = "test" +str(self.count), 
            withdraw = 0,
            deposit = 0, 
            balance = 0,
            type = nodeType, 
            children = {},
            parent = self.manager
            )
        res = self.manager.add(childNode)
        if not res:
            print("This name alread exists in the ", nodeType, " list. Enter a new name" )
        self.count += 1
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
            self.parent = self.manager
            self.manager = self.manager.children[key]
            self.update()
            
            return True
        return False


    def backButton(self):
        if self.parent != None:
            self.manager = self.parent
            self.parent = self.manager.parent
            self.update()
            return True

        return False

    def update(self):
        _translate = QtCore.QCoreApplication.translate
        self.addBtn.setText(_translate("MainWindow", "Add " + self.getChildType())) # text is depended on the type child node
        # manger.type , " List: ", manager.name
        self.listHtml = self.listHtml = HTML[0] + self.manager.type + " " + self.manager.name + " List" + HTML[1]
        self.listTitle.setHtml(_translate("MainWindow", self.listHtml))
        #update display list
        self.listWidget.clear()
        self.displayList()
    
    def getChildType(self):
        nodeType = ""
        match self.manager.type:
            case "Bank Accounts":
                nodeType = "Account"

            case "Account":
                nodeType = "Statement"

            case "Statement":
                nodeType = "Transaction"

            case _:
                nodeType = "No more Children Allowed"
        return nodeType


def closeApp(app, manager):
    
    app.exec()
    # save data to pickle file
    if manager != None:
        MemoryUpdate(PICKELFILE, manager)





if __name__ == "__main__":
    import sys
    load = True
    manager = None
    if load:
        manager = LoadData(PICKELFILE)
    elif manager == None:
        #create new manager
        manager = treeNode(
            name = "Personal Finance Manager", 
            withdraw = 0,
            deposit = 0, 
            balance = 0,
            type = "Bank Accounts",
            children = {},
            parent = None
        )
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(manager)
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(closeApp(app, manager))
    