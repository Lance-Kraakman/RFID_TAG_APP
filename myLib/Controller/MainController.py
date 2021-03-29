from myLib.Item import Item
from myLib.Database import databaseAbstraction
from myLib.StorageSection import StorageSection
from myLib.Compartment import Compartment
from myLib.Views import MainView as mv
import tkinter as tk


class MainController:

    def __init__(self):

        # Create View
        root = tk.Tk()
        myApp = mv.MainApp(master=root)
        root.mainloop()




