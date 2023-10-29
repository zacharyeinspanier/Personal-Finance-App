from PyQt6 import QtCore, QtGui, QtWidgets

from classes.PFTreeNode import treeNode
from Pickel.PickelHelpers import LoadData, MemoryUpdate
from main_ui import Ui_MainWindow
import argparse
import sys



parser = argparse.ArgumentParser(
                    prog='Personal Finance App',
                    description='Enter bank statements for tracking spending',
                    epilog='Usage: python main.py --data=[new | load] --file = [pickel file].pkl'
                    )

parser.add_argument("--data", choices = ["new", "load"], default = "new") 
parser.add_argument("--pfile", default = "Pickel/newPickelFile.pkl")


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