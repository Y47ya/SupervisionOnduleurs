import os
from webbrowser import open
import shutil

FOLDER_PATH = "./src/documentation"


def listDir():
    fileNames = os.listdir(FOLDER_PATH)
    return fileNames


def openFile(fileName):
    open(os.path.join(FOLDER_PATH, fileName))


def copyFile(filePath):
    try:
        shutil.copy(filePath, FOLDER_PATH)
        print("Copied")

    except:
        raise ValueError()


def deleteFile(fileName):
    try:
        os.remove(os.path.join(FOLDER_PATH, fileName))

    except:
        raise ValueError()
