
from cgitb import text
from tkinter import ttk
from re import M
from textwrap import fill
from tkinter import BOTH, Entry, Frame, Label, Scrollbar, ttk
from turtle import left, right

from mysqlx import Column


class Bibliotheque:
    def __init__(self,root):
        self.root = root
        titleSpace = " "
        self.root.title(102 * titleSpace + "Gestion Bibliotheque")
        self.root.geometry("800x700+300+0")
        self.root.resizable(width = False, height = False)

        MainFrame = Frame(self.root,bd=10,width=800,height=700)
        MainFrame.grid()

        TitleFrame = Frame(MainFrame,bd=10,width=770,height=100,)
        TitleFrame.grid(row=0,column=0)
        TopFrame3 = Frame(MainFrame,bd=10,width=770,height=500)
        TopFrame3.grid(row=1,column=0)

        LeftFrame = Frame(TopFrame3,bd=5,width=770,height=400,padx=2)
        LeftFrame.pack(side="left")
        LeftFrame1 = Frame(LeftFrame,bd=5,width=600,height=180,padx=2,pady=4)
        LeftFrame1.pack(side="top",padx=0,pady=0)

        RightFrame1 = Frame(TopFrame3,bd=5,width=100,height=400,padx=2)
        RightFrame1.pack(side="right")
        RightFrame1a = Frame(RightFrame1,bd=5,width=90,height=300,padx=2,pady=2)
        RightFrame1a.pack(side="top")

        #===================================================================================================

  
        self.labTitle = Label(TitleFrame,font=('arial',30,'bold'),text="Gestion Bibliotheque")
        self.labTitle.grid(row=0,column=0,padx=132)

        self.labCode = Label(LeftFrame1,font=('arial',12,'bold'),text="Code Livre",bd=7)
        self.labCode.grid(row=1,column=0,padx=5)
        self.entCode = Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=44,justify='left')
        self.entCode.grid(row=1,column=1,padx=5)

        self.labName = Label(LeftFrame1,font=('arial',12,'bold'),text="Nom du livre",bd=7)
        self.labName.grid(row=2,column=0,padx=5)
        self.entName = Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=44,justify='left')
        self.entName.grid(row=2,column=1,padx=5)

        self.labDesc = Label(LeftFrame1,font=('arial',12,'bold'),text="Description",bd=7)
        self.labDesc.grid(row=3,column=0,padx=5)
        self.entDesc = Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=44,justify='left')
        self.entDesc.grid(row=3,column=1,padx=5)

        self.labAuthor = Label(LeftFrame1,font=('arial',12,'bold'),text="Auteur",bd=7)
        self.labAuthor.grid(row=4,column=0,padx=5)
        self.entAuthor = Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=44,justify='left')
        self.entAuthor.grid(row=4,column=1,padx=5)

        self.labTotal = Label(LeftFrame1,font=('arial',12,'bold'),text="Quantité",bd=7)
        self.labTotal.grid(row=5,column=0,padx=5)
        self.labTotal = Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=44,justify='left')
        self.labTotal.grid(row=5,column=1,padx=5)


        #==================================Tableau des livres===============================
        scroll_param= Scrollbar(LeftFrame,orient='vertical')
        self.list_livres = ttk.Treeview(LeftFrame,height=12,columns=("code","nom","auteur","quantité"),yscrollcommand = scroll_param)
        scroll_param.pack(side='right',fill='y')

        self.list_livres.heading("code",text="Code")
        self.list_livres.heading("nom",text="Nom")
        self.list_livres.heading("auteur",text="Auteur")
        self.list_livres.heading("quantité",text="Quantité")

        self.list_livres['show']='headings'

        self.list_livres.column("code",width=70)
        self.list_livres.column("nom",width=70)
        self.list_livres.column("auteur",width=70)
        self.list_livres.column("quantité",width=70)

        self.list_livres.pack(fill=BOTH,expand=1)


       

