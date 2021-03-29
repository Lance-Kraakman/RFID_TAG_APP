import tkinter as tk
from tkinter import ttk
from myLib.Views import ListSection as ls
from myLib.Rfid import RfidNetworkService as rf


class ListSectionController(tk.Tk):
    def __init__(self, parent):
        print("Hello World!")

        # Tag Model
        self.model = rf.RfidNetworkService()

        # Tag View
        self.sectionFrame = ls.ListSection(parent, self, self.model)
        self.sectionFrame.pack(expand="False")  # This sets the position with main frame i think :)

        # Bind Events
        self.sectionFrame.getListBox().bind("<<ListboxSelect>>", self.tagSelectedCallback)
        self.sectionFrame.getListBox().bind('<Double-1>', self.tagDoubleClick)

    def tagSelectedCallback(self, event):
        print("Selected")

    def getModelList(self):
        return self.sectionFrame.listBox.getModelList()

    def tagDoubleClick(self, event):
        print("Double Click")

    def updateModel(self):
        self.model.setRfidTagList(self.model.getRfidTagsFromDB())  # Updates the List of RFID Tags. Getting them from the database

    def updateView(self):
        self.sectionFrame.getListSection().updateList()

    def updateListGUI(self):
        self.updateModel()
        self.updateView()
