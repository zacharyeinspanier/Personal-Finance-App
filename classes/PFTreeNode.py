
class treeNode:
    """
    This class holds data for personal finance
        name: str: name of the node
        withdraw: float: total withdraw 
        deposit: float: total deposit
        balance: float: sum of withdraw and deposit
        type: str: type of node: Bank Accounts, Account, Statement, Transactions, SingleTransaction 
        children = {}: dictionary of treeNodes, Key = treeNode.name
        parent = None: Parent treeNode

    """

    def __init__(
        self, 
        name: str,
        withdraw: float, 
        deposit: float, 
        balance: float,
        type: str,
        children = {},
        parent = None,
    ):
        self.name = name
        self.children = children
        self.withdraw = withdraw
        self.deposit = deposit
        self.balance = balance
        self.parent = parent
        self.type = type

    def sum(self):
        """
        This function calculates the withdraw, deposit, and balance 
        """
        self.withdraw = 0
        self.balance = 0
        self.deposit = 0
        if not len(self.children) > 0:
            return

        for node in self.children.keys():
            if self.children[node].withdraw < 0:
                self.withdraw += self.children[node].withdraw

            if self.children[node].deposit  > 0:
                self.deposit += self.children[node].deposit
            else:
                continue
        self.balance = float(self.withdraw + self.deposit)
        self.hasSum = True

    def add(self, node):
        """
        This function add a new treeNode to the children dictionary
        """
        # key would be name
        if node.name not in self.children:
            self.children[node.name] = node
            return True
        else: 
            return False
        

    def removeChildren(self):
        """
        This function removes a treeNode from the children dictionary
        """ 
        # if child is type node then call remove, else deliete
        deleteItems = list(self.children.keys())
        for key in deleteItems:  
            if isinstance(self.children[key], treeNode):
                deleteItem = self.children.pop(key)
                deleteItem.removeChildren()
                del deleteItem

        self.children.clear()