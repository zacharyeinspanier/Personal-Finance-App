from PyQt6 import QtCore, QtGui, QtWidgets


class Rename_UI (object):
    
    def __init__(self, parent=None):
        self.parent = parent
    

    def setupUi(self, Form):
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
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Rename List", "Rename List"))
        self.renameListBtn.setText(_translate("Rename List", "Rename List"))
        self.cancelBtn.setText(_translate("Rename List", "Cancel"))
        self.title.setPlainText(_translate("Rename List", "Rename List"))

    def renameClick(self):
        if self.parent != None:
            self.parent.changeListName(newName = self.inputRename.text())

    def cancelClick(self):
        self.formObj.close()

    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Rename_UI()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
