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
    
 def backButton(self):
        if self.manager.parent != None:
            self.manager = self.manager.parent
            self.update()
            return True

        return False

def displayTransaction(self): #TODO Retitle
        innerText = ""
        _translate = QtCore.QCoreApplication.translate
        
        
        for key in self.manager.children.keys(): 
            innerText += str(key) + ": " + str(self.manager.children[key]) + "<br>"


        transaction_display = HTML_TRANSACTION[0]+ innerText + HTML_TRANSACTION[1]
        self.listHtml = self.listHtml = HTML[0]  + self.manager.name + " Transaction" + HTML[1]
        self.transactionDisplay.setText(_translate("MainWindow", transaction_display))
        self.listTitle.setHtml(_translate("MainWindow", self.listHtml))
        self.updateWidgets()

 def listClick(self, item):

        key = item.text()
        if key in self.manager.children:
            self.manager = self.manager.children[key] # this is not an object it is a dictionary
            if self.manager.type == "SingleTransaction":
                self.displayTransaction()
                return True
            else:
                self.update()
                return True
        return False

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