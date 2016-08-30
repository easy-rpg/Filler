#coding=utf-8
from Tkinter import *
from tkFileDialog import askopenfilename
import tkMessageBox
from Personagem import *
# import sys

personagem = Personagem()

atualizar = False
clear = False
stop = False


personagem = load_personagem("personagens/Assis.rf")
# atualizar = True
# clear = True

class MenuBar(Menu):
    def __init__(self, parent):
        Menu.__init__(self, parent)
        fileMenu = Menu(self, tearoff=False)
        self.add_cascade(label="File",underline=0, menu=fileMenu)

        fileMenu.add_command(label="New", underline=1, command=self.NewChar)
        fileMenu.add_command(label="Load...", underline=1, command=self.LoadChar)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", underline=1, command=self.quit)

        helpMenu = Menu(self, tearoff=False)
        self.add_cascade(label="Help",underline=0, menu=helpMenu)

        helpMenu.add_command(label="About...", underline=1, command=self.About)

    def NewChar(self):
        global personagem
        personagem = Personagem()

        global clear
        clear = True
        
        # self.t = Toplevel(self)
        # self.t.wm_title("Novo Personagem")

        # self.lnome = Label(self.t, text="Nome: ").grid(row=0)
        # self.enome = Entry(self.t)
        # self.enome.grid(row=0, column=1)

        # self.lattfor = Label(self.t, text="Força: ").grid(row=1, column=0)
        # self.eattfor = Entry(self.t)
        # self.eattfor.grid(row=1, column=1)

        # self.lattdex = Label(self.t, text="Destreza: ").grid(row=2, column=0)
        # self.eattdex = Entry(self.t)
        # self.eattdex.grid(row=2, column=1)
         
        # self.lattcon = Label(self.t, text="Constituição: ").grid(row=3, column=0)
        # self.eattcon = Entry(self.t)
        # self.eattcon.grid(row=3, column=1)

        # self.lattint = Label(self.t, text="Inteligência: ").grid(row=4, column=0)
        # self.eattint = Entry(self.t)
        # self.eattint.grid(row=4, column=1)

        # self.lattsab = Label(self.t, text="Sabedoria: ").grid(row=5, column=0)
        # self.eattsab = Entry(self.t)
        # self.eattsab.grid(row=5, column=1)

        # self.lattcar = Label(self.t, text="Carisma: ").grid(row=6, column=0)
        # self.eattcar = Entry(self.t)
        # self.eattcar.grid(row=6, column=1)

        # self.button = Button(self.t)
        # self.button["text"] = "Cadastrar",
        # self.button["command"] = self.cadastrar
        # self.button.grid(row=8, columnspan=2)

    def LoadChar(self):
        char = askopenfilename()
        global personagem
        personagem = load_personagem(char)
        # print personagem
        global atualizar
        atualizar = True
        # self.mensagem("Aviso", "Personagem carregado com sucesso")

    def mensagem(self, title, string):
        tkMessageBox.showinfo(title, string)

    def About(self):
        string = "O RPG Filler é um programa para automatizar a criação de personagens para o sistema de rpg D&D 3.5."
        string += "\n"
        string += "Para mais informações acessar https://github.com/rodrigondec/RPG-Filler"
        self.mensagem("about", string)

    def quit(self):
        global stop
        stop = True

class Application(Frame):

    def event_salvar_char(self, event):
        self.salvar_char()

    def salvar_char(self):
        print "salvar char"
        if not self.entry_nome.get() or not self.entry_for.get() or not self.entry_dex.get() or not self.entry_con.get() or not self.entry_int.get() or not self.entry_sab.get() or not self.entry_car.get():
            self.mensagem("Erro", "Prencha o campo de nome e de atributos antes de salvar!")
            return
        if  not self.entry_for.get().isdigit() or not self.entry_dex.get().isdigit() or not self.entry_con.get().isdigit() or not self.entry_int.get().isdigit() or not self.entry_sab.get().isdigit() or not self.entry_car.get().isdigit():
            self.mensagem("Erro", "Prencha os campos de atributos com números para salvar!")
            return

        global personagem

        personagem = Personagem(self.entry_nome.get(), int(self.entry_for.get()), int(self.entry_dex.get()), int(self.entry_con.get()), int(self.entry_int.get()), int(self.entry_sab.get()), int(self.entry_con.get()))

        personagem.atualizar()
        self.clr()
        self.att()

    def NewClass(self):
        print "nova classe"

    def salvar_classe(self):
        print "salvar classe"

    def clr(self):
        self.entry_nome.delete(0, END)
        self.entry_for.delete(0, END)
        self.entry_dex.delete(0, END)
        self.entry_con.delete(0, END)
        self.entry_int.delete(0, END)
        self.entry_sab.delete(0, END)
        self.entry_car.delete(0, END)
        self.entry_lvl.delete(0, END)
        self.entry_life.delete(0, END)
        self.entry_classes.delete(0, END)
        self.entry_bba.delete(0, END)
        self.entry_fort.delete(0, END)
        self.entry_ref.delete(0, END)
        self.entry_von.delete(0, END)

    def att(self): 
        self.clr()
        global personagem

        self.entry_nome.insert(0, personagem.nome)  

        self.entry_for.insert(0, str(personagem.atributos['for']))
        self.entry_dex.insert(0, str(personagem.atributos['dex'])) 
        self.entry_con.insert(0, str(personagem.atributos['con'])) 
        self.entry_int.insert(0, str(personagem.atributos['int'])) 
        self.entry_sab.insert(0, str(personagem.atributos['sab'])) 
        self.entry_car.insert(0, str(personagem.atributos['car'])) 

        self.entry_lvl.insert(0, str(personagem.nivel))
        self.entry_life.insert(0, str(personagem.life))

        string = ""
        for index in personagem.classes:
            string += index + " ("+str(personagem.classes[index].nivel)+") "
        self.entry_classes.insert(0, string)

        self.entry_bba.insert(0, str(personagem.bba))

        self.entry_fort.insert(0, str(personagem.fortitude))
        self.entry_ref.insert(0, str(personagem.reflexos))
        self.entry_von.insert(0, str(personagem.vontade))

    def createWidgets(self):
        # self.nome = Text(self, state="disabled", height="1", width=30)
        # self.nome.insert(END, str(personagem.nome))
        self.label_nome = Label(self, text="Nome: ").grid(row=0, column=0)
        self.string_nome = StringVar()
        self.entry_nome = Entry(self, textvariable=self.string_nome, width=17)
        self.entry_nome.grid(row=0, column=1 ,columnspan=3)

        self.label_for = Label(self, text="For: ").grid(row=1, column=0)
        self.string_for = StringVar()
        self.entry_for = Entry(self, textvariable=self.string_for, width=5)
        self.entry_for.grid(row=1, column=1)

        self.label_dex = Label(self, text="Dex: ").grid(row=2, column=0)
        self.string_dex = StringVar()
        self.entry_dex = Entry(self, textvariable=self.string_dex, width=5)
        self.entry_dex.grid(row=2, column=1)

        self.label_con = Label(self, text="Con: ").grid(row=3, column=0)
        self.string_con = StringVar()
        self.entry_con = Entry(self, textvariable=self.string_con, width=5)
        self.entry_con.grid(row=3, column=1)

        self.label_int = Label(self, text="Int: ").grid(row=1, column=2)
        self.string_int = StringVar()
        self.entry_int = Entry(self, textvariable=self.string_int, width=5)
        self.entry_int.grid(row=1, column=3)

        self.label_sab = Label(self, text="Sab: ").grid(row=2, column=2)
        self.string_sab = StringVar()
        self.entry_sab = Entry(self, textvariable=self.string_sab, width=5)
        self.entry_sab.grid(row=2, column=3)

        self.label_car = Label(self, text="Car: ").grid(row=3, column=2)
        self.string_car = StringVar()
        self.entry_car = Entry(self, textvariable=self.string_car, width=5)
        self.entry_car.grid(row=3, column=3)

        self.label_lvl = Label(self, text="Nivel: ").grid(row=4, column=0)
        self.string_lvl = StringVar()
        self.entry_lvl = Entry(self, textvariable=self.string_lvl, width=5)
        self.entry_lvl.grid(row=4, column=1)

        self.label_life = Label(self, text="Life: ").grid(row=4, column=2)
        self.string_life = StringVar()
        self.entry_life = Entry(self, textvariable=self.string_life, width=5)
        self.entry_life.grid(row=4, column=3)

        self.label_classes = Label(self, text="Classes: ").grid(row=5, column=0)
        self.string_classes = StringVar()
        self.entry_classes = Entry(self, textvariable=self.string_classes, width=17)
        self.entry_classes.grid(row=5, column=1, columnspan=3)

        self.label_bba = Label(self, text="BBA: ").grid(row=6, column=0)
        self.string_bba = StringVar()
        self.entry_bba = Entry(self, textvariable=self.string_bba, width=5)
        self.entry_bba.grid(row=6, column=1)

        self.label_fort = Label(self, text="FORT: ").grid(row=6, column=2)
        self.string_fort = StringVar()
        self.entry_fort = Entry(self, textvariable=self.string_fort, width=5)
        self.entry_fort.grid(row=6, column=3)

        self.label_ref = Label(self, text="REF: ").grid(row=7, column=0)
        self.string_ref = StringVar()
        self.entry_ref = Entry(self, textvariable=self.string_ref, width=5)
        self.entry_ref.grid(row=7, column=1)

        self.label_von = Label(self, text="VON: ").grid(row=7, column=2)
        self.string_von = StringVar()
        self.entry_von = Entry(self, textvariable=self.string_von, width=5)
        self.entry_von.grid(row=7, column=3)

        self.cadastrar_classe = Button(self)
        self.cadastrar_classe["text"] = "Adicionar Classe"
        self.cadastrar_classe["command"] = self.NewClass
        self.cadastrar_classe.grid(row=8, column=0, columnspan=2)

        self.cadastrar_char = Button(self)
        self.cadastrar_char["text"] = "Salvar"
        self.cadastrar_char["command"] = self.salvar_char
        self.cadastrar_char.grid(row=8, column=2, columnspan=2)

    def mensagem(self, title, string):
        tkMessageBox.showinfo(title, string)

    def event_exit(self, event):
        global stop
        stop = True

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
        menubar = MenuBar(self)
        master.config(menu=menubar)
        master.bind("<Escape>", self.event_exit)
        master.bind("<Return>", self.event_salvar_char)

root = Tk()
root.wm_title("RPG Filler")
root.resizable(width=False, height=False)
root.geometry('{}x{}'.format(300, 220))

app = Application(master=root)
# app.pack(side="top", fill="both", expand=True)

while True:
    if atualizar:
        app.att()
        atualizar = False
    if clear:
        app.clr()
        clear = False
    if stop:
        break
    app.update_idletasks()
    app.update()
root.destroy()