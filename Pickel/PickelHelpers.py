import pickle
import pathlib
import os


def LoadData(PICKELFILE):
    """
    This function loads data from the memory file to the list accounts
    If the file does not exist or is empty -> return 
    """
    if not goodFile(PICKELFILE):
        return False
    try:
        with open(PICKELFILE, "rb") as picf:
            dataFromLoad = pickle.load(picf)
            return dataFromLoad
    except OSError as e:
        print(e)
        return None


 
def SaveData(PICKELFILE, data):
    """
    This function handles a memory save.
    It will create the memory file if it des not exist
    Then it will write the list account to the memory
    Assumes file exists, checked with function goodFile()
    """
    try:
        with open(PICKELFILE, "wb") as picf:
            pickle.dump(data, picf)
            return True
    except OSError as e: 
        print(e)
        return False

def DeleteMemory(PICKELFILE):
    """
    This function deletes the contents of a memory file
    If the file does not exist or is empty -> return
    Assumes file exists, checked with function goodFile()
    """
    # check if file is empty
    if os.path.getsize(PICKELFILE) <= 0:
        return True
    try:
        with open(PICKELFILE, "r+") as picf:
            picf.truncate(0)
            return True
    except OSError as e: 
        print(e)
        return False

def goodFile(PICKELFILE):
    """
    This checks if a file path is good

    Returns:
        True: if the file exists or can be created
        False: if the file cannot be created
    """

    # check that file exists
    if os.path.isfile(PICKELFILE):
        return True
    # check if file path is abs and the path exists
    if os.path.isabs(PICKELFILE) and not os.path.exists(pathlib.Path(PICKELFILE)):
        return False
    try:
        f = open(PICKELFILE, "x")
        f.close()
        return True
    except OSError as e: 
        print(e)
        return False
    return False
   


def MemoryUpdate(PICKELFILE, data):
    """
    This function handels a memory update. 
    Memory file is cleared then data is written to the file
    """
    if not goodFile(PICKELFILE):
        return False

    DeleteMemory(PICKELFILE)
    return SaveData(PICKELFILE, data)
    
