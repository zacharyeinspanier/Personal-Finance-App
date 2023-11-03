from PyQt6 import QtCore, QtGui, QtWidgets


class Rename_UI (object):
    """
    This class is a user interface for changing the name of a treeNode

    Parent: parent class
    """
    
    def __init__(self, parent=None):
        self.parent = parent
    

    def setupUi(self, Form):
        """
        This function declares and sets all of the widgest for the UI. 
        """
        Form.setObjectName("Rename List")
        Form.resize(331, 212)
        Form.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.formObj = Form

        self.renameListBtn = QtWidgets.QPushButton(parent=Form)
        self.renameListBtn.setGeometry(QtCore.QRect(170, 70, 121, 31))
        self.renameListBtn.setStyleSheet("\n""background-color: rgb(227, 227, 227);")
        self.renameListBtn.setObjectName("renameList")
        self.renameListBtn.clicked.connect(self.renameClick)

        self.cancelBtn = QtWidgets.QPushButton(parent=Form)
        self.cancelBtn.setGeometry(QtCore.QRect(110, 140, 121, 31))
        self.cancelBtn.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.cancelBtn.setObjectName("cancelBtn")
        self.cancelBtn.clicked.connect(self.cancelClick)

        self.inputRename = QtWidgets.QLineEdit(parent=Form)
        self.inputRename.setGeometry(QtCore.QRect(20, 70, 141, 31))
        self.inputRename.setObjectName("inputRename")
        self.inputRename.setPlaceholderText("Enter a list name")

        self.title = QtWidgets.QPlainTextEdit(parent=Form)
        self.title.setGeometry(QtCore.QRect(100, 10, 200, 41))
        self.title.setStyleSheet("font: 16pt \"Segoe UI\";\n""background:transparent;border : 0;")
        self.title.setObjectName("title")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
          

    def retranslateUi(self, Form):
        """
        This function sets the inner text for all of the widgest for the UI. 
        """
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Rename List", "Rename List"))
        self.renameListBtn.setText(_translate("Rename List", "Rename List"))
        self.cancelBtn.setText(_translate("Rename List", "Cancel"))
        self.title.setPlainText(_translate("Rename List", "Rename List"))

    def renameClick(self):
        """
        This function calls a function from the parent calss to change the name of a treeNode
        """
        if self.parent != None:
            self.parent.changeListName(newName = self.inputRename.text())

    def cancelClick(self):
        """
        This function closes the widget
        """
        self.formObj.close()

