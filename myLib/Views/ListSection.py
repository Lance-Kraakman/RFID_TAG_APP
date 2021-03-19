import tkinter as tk
from tkinter import ttk
from myLib.Rfid import Rfid as rf


class ListSection(ttk.Frame):
    def __init__(self, parent, controller, TagList):
        ttk.Frame.__init__(self, parent)

        self.listSection = List(self, self, TagList)
        self.listSection.pack(expand="False")

    def getListSection(self):
        return self.listSection

    def getListBox(self):
        return self.listSection.getListBox()

# Look at Design Pattern for Java
class List(ttk.Frame):
    def __init__(self, parent, controller, TagList):
        tk.Frame.__init__(self, parent)
        self.model = TagList
        sectionFrame = ttk.Frame(self)

        label = tk.Label(sectionFrame, text="RFID TAGS")
        label.pack(expand="False")

        self.listBox = tk.Listbox(sectionFrame, height=100, width=200, font=('arial', 16, 'bold'), bg="black", fg="white")
        self.listBox.pack(expand="False")

        sectionFrame.pack(expand="False")  # List takes up whole window
        self.updateList()

    def updateList(self):
        self.listBox.delete(0, self.model.getItemCount())
        for item in self.model.getRfidTagList():
            self.insertItemToList(item)

    def insertItemToList(self, item):
        self.listBox.insert(tk.END, item)

    def deleteFromList(self):
        print("To-Do")

    def getModelList(self):
        return self.model

    def getListBox(self):
        return self.listBox
