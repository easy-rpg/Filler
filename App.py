#coding=utf-8
from Tkinter import *
from tkFileDialog import askopenfilename
import tkMessageBox
from Personagem import *
# import sys

personagem = None
personagem = load_personagem("personagens/Assis.rf")

atualizar = False
clear = False
# print personagem

class MenuBar(Menu):
    def __init__(self, parent):
        Menu.__init__(self, parent)
        fileMenu = Menu(self, tearoff=False)
        self.add_cascade(label="File",underline=0, menu=fileMenu)

        fileMenu.add_command(label="New", underline=1, command=self.NewChar)
        fileMenu.add_command(label="Load...", underline=1, command=self.LoadChar)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", underline=1, command=quit)

        helpMenu = Menu(self, tearoff=False)
        self.add_cascade(label="Help",underline=0, menu=helpMenu)

        helpMenu.add_command(label="About...", underline=1, command=self.About)

    def NewChar(self):
        global personagem
        personagem = None

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

    def cadastrar(self):
        if not self.enome.get() or not self.eattfor.get() or not self.eattdex.get() or not self.eattcon.get() or not self.eattint.get() or not self.eattsab.get() or not self.eattcar.get():
            self.mensagem("Erro", "preencha todos os campos!")
            return
        forca, destreza, constituicao, inteligencia, sabedoria, carisma = int(self.eattfor.get()), int(self.eattdex.get()), int(self.eattcon.get()), int(self.eattint.get()), int(self.eattsab.get()), int(self.eattcar.get())
        global personagem
        personagem = Personagem(self.enome.get(), forca, destreza, constituicao, inteligencia, sabedoria, carisma)
        print personagem
        self.t.withdraw()
        # self.mensagem("Aviso", "Personagem criado com sucesso")

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

class Application(Frame):

    def salvar_char(self):
        print "salvar char"
        if not self.entry_nome.get() or not self.entry_for.get() or not self.entry_dex.get() or not self.entry_con.get() or not self.entry_int.get() or not self.entry_sab.get() or not self.entry_car.get():
            self.mensagem("Erro", "Prencha o campo de nome e de atributos antes de salvar!")
            return
        if  not self.entry_for.get().isdigit() or not self.entry_dex.get().isdigit() or not self.entry_con.get().isdigit() or not self.entry_int.get().isdigit() or not self.entry_sab.get().isdigit() or not self.entry_car.get().isdigit():
            self.mensagem("Erro", "Prencha os campos de atributos com números para salvar!")
            return
        # forca, destreza, constituicao, inteligencia, sabedoria, carisma = int(self.eattfor.get()), int(self.eattdex.get()), int(self.eattcon.get()), int(self.eattint.get()), int(self.eattsab.get()), int(self.eattcar.get())
        # global personagem
        # personagem = Personagem(self.enome.get(), forca, destreza, constituicao, inteligencia, sabedoria, carisma)
        # print personagem

    def NewClass(self):
        print "nova classe"

    def salvar_classe(self):
        print "salvar classe"
    def att(self): 
        global personagem
        if personagem:       
            self.rnome.set("Nome: "+personagem.nome)

            string = "Força: " + str(personagem.atributos['for'])
            string += " | "
            string += "Destreza: " + str(personagem.atributos['dex'])
            string += " | "
            string += "Constituição: " + str(personagem.atributos['con'])
            string += " | "
            string += "Inteligência: " + str(personagem.atributos['int'])
            string += " | "
            string += "Sabedoria: " + str(personagem.atributos['sab'])
            string += " | "
            string += "Carisma: " + str(personagem.atributos['car'])
            string += " | "
            self.rattr.set(string)

            self.rlvl.set("lvl: "+str(personagem.nivel))

            string = "Classes: "
            for index in personagem.classes:
                string += index + " ("+str(personagem.classes[index].nivel)+") "
            self.rcls.set(string)

            self.rbba.set("BBA: "+str(personagem.bba))

            string = "FOR: " + str(personagem.fortitude)
            string += " | "
            string += "REF: " + str(personagem.reflexos)
            string += " | "
            string += "VON: " + str(personagem.vontade)
            self.rres.set(string)

    def createWidgets(self):
        # self.nome = Text(self, state="disabled", height="1", width=30)
        # self.nome.insert(END, str(personagem.nome))
        self.rnome = StringVar()
        self.nome = Label(self, textvariable=self.rnome, bg="white")
        self.nome.pack()

        self.rattr = StringVar()
        self.attr = Label(self, textvariable=self.rattr, bg="white")
        self.attr.pack()

        self.rlvl = StringVar()
        self.lvl = Label(self, textvariable=self.rlvl, bg="white")
        self.lvl.pack()

        self.rcls = StringVar()
        self.cls = Label(self, textvariable=self.rcls, bg="white")
        self.cls.pack()

        self.rbba = StringVar()
        self.bba = Label(self, textvariable=self.rbba, bg="white")
        self.bba.pack()

        self.rres = StringVar()
        self.res = Label(self, textvariable=self.rres, bg="white")
        self.res.pack()

        self.upd = Button(self)
        self.upd["text"] = "Atualizar",
        self.upd["command"] = self.att

        self.upd.pack(side="bottom")  

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
        menubar = MenuBar(self)
        master.config(menu=menubar)
        master.bind("<Escape>", quit)

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
    app.update_idletasks()
    app.update()
# app.mainloop()

root.destroy()