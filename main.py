import tkinter
from pathlib import Path
import os

currentLibrary = []
currentLocation = Path("./Library")
mainWindow = tkinter.Tk()
screenWidth = mainWindow.winfo_screenwidth()
screenHeight = mainWindow.winfo_screenheight()
mainWindow.geometry("400x{}+{}+0".format(screenHeight ,screenWidth-400))


def run_Library():
    global currentLocation
    tkinter.Button(mainWindow, text="Back",fg ="white",bg="grey", width = 30, command=lambda: goBack(currentLocation)).pack(pady=10)
    populate(currentLocation)
    mainWindow.mainloop()

def populate(loc):
    currentLibrary.clear()
    for item in loc.iterdir():
        currentLibrary.append(item)
    createButtons()

def createButtons():
    for item in currentLibrary:
        tkinter.Button(mainWindow, text=item.stem, width=70, command=lambda item=item:fileHandler(item)).pack(pady=3)

def fileHandler(inpt):
    global currentLocation
    if inpt.is_dir():
        clearFrame()
        currentLocation = inpt
        populate(currentLocation)
    else:
        os.startfile(inpt)

def goBack(loc):
    global currentLocation
    if not currentLocation.name == "Library":
        clearFrame()
        currentLocation = loc.parent
        populate(loc.parent)


def clearFrame():
    optionList = mainWindow.pack_slaves()
    for btn in optionList:
        if not btn["text"]=="Back":
            btn.destroy();

run_Library()
