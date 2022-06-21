from email.mime import application
from logging import root
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from turtle import width
import pymysql


class ConnectorDB:
    def __init__(self,root) -> None:
        self.root = root
        titleSpace = " "
        self.root.title(102 * titleSpace + "Gestion Bibliotheque")
        self.root.geometry("776x700+300+0")
        self.root.resizable(width = False, height = False)


if __name__ == "__main__":
    root = Tk()
    application =  ConnectorDB
    root.mainloop()      