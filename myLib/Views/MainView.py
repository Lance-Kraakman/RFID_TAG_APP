import tkinter as tk
from tkinter import ttk
from myLib.Views import ListSection as ls
from myLib.Rfid import Rfid as rf
from myLib.Controller import ListSectionController as lc


class MainApp(tk.Frame):
    def __init__(self, master=None):
        master.title('RFID TAG APP')
        master.geometry("500x500")


        tk.Frame.__init__(self, master)
        #self.title("Robot Control App")
        custom_style = ttk.Style()
        custom_style.configure('Custom.TNotebook.Tab', paddx=(10, 0), pady=(10, 10), font=('Helvetica', 15))
        #
        mainFrame = ttk.Frame(self)
        mainFrame.pack(expand="False")

        # Add List Section
        self.listSectionController = lc.ListSectionController(mainFrame)

        self.onUpdate()
        self.pack()



    # Using theese we can use MVC in controller application
    def getListSection(self):
        #return self.sectionFrame
        print()

    def getPersonList(self):
       # return self.sectionFrame.listBox
        print()

    def onUpdate(self):
        self.listSectionController.updateListGUI()
        self.after(500, self.onUpdate)

