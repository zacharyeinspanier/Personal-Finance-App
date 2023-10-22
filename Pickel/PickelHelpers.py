import pickle
import os


def LoadData(PICKELFILE):
    """
    This function loads data from the memory file to the list accounts
    If the file does not exist or is empty -> return 
    """
    
    if not os.path.isfile(PICKELFILE):
        print("No memory file to load")
        return None
    elif os.path.getsize(PICKELFILE) <= 0:
        print("Memory file is empty")
        return None
    else:
        with open(PICKELFILE, "rb") as picf:
            dataFromLoad = pickle.load(picf)
            return dataFromLoad
 
def SaveData(PICKELFILE, manager):
    """
    This function handles a memory save.
    It will create the memory file if it des not exist
    Then it will write the list account to the memory
    """
    if not os.path.isfile(PICKELFILE):
        f = open(PICKELFILE, "x")
        f.close()
        print("Memory file created")
    with open(PICKELFILE, "wb") as picf:
        pickle.dump(manager, picf) # need way to save manager 
    print("Memory is saved")

def DeleteMemory(PICKELFILE):
    """
    This function deletes the contents of a memory file
    If the file does not exist or is empty -> return
    """
    if not os.path.isfile(PICKELFILE):
        print("Memory File has not been created.")
        return
    elif os.path.getsize(PICKELFILE) <= 0:
        print("Memory file is empty")
        return 
    else:
        with open(PICKELFILE, "r+") as picf:
            picf.truncate(0)
        return

def MemoryUpdate(PICKELFILE, manager):
    """
    This function handels a memory update. 
    Memory file is cleared then data is written to the file
    """
    DeleteMemory(PICKELFILE)
    SaveData(PICKELFILE, manager)
