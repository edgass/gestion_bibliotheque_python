from email.mime import application
from logging import root
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from turtle import width
import pymysql

from bibliotheque import Bibliotheque




if __name__ == "__main__":
    root = Tk()
    application =  Bibliotheque(root)
    root.mainloop()      