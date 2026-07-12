from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import messagebox

class View:
    def __init__(self):
        self.cor_atual = 'black'
        self.background = None

        self.root = Tk()
        self.root.title('Quarta entrega do Projeto POO')

        #Parte da persistência, menu Arquivo (Salvar/Abrir)
        self.menu_bar = Menu(self.root)
        self.menu_arquivo = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='Arquivo', menu=self.menu_arquivo)
        self.root.config(menu=self.menu_bar)

        self.frame = Frame(self.root)

        paddings = {'padx': 5, 'pady': 5}

        self.label = ttk.Label(
            self.frame,
            text='Escolha o que vai desenhar:'
        )
        self.label.grid(column=0, row=0, sticky=W, **paddings)

        self.tipo_figura_var = StringVar(self.root)

        self.option_menu = ttk.OptionMenu(
            self.frame,
            self.tipo_figura_var,
            'Linha',
            'Linha',
            'Rabisco',
            'Retângulo',
            'Oval',
            'Círculo',
            'Triângulo',
            'Pentágono',
            'Hexágono'
        )

        self.option_menu.grid(column=1, row=0, sticky=W, **paddings)

        self.canvas = Canvas(self.frame, bg='white', width=600, height=600)
        self.canvas.grid(column=0, row=3, columnspan=2, sticky=W, **paddings)

        self.botao_cor_borda = Button(
            self.frame,
            text="Cor da Borda",
            command=self.escolher_cor_borda
        )
        self.botao_cor_borda.grid(column=0, row=1, sticky=W, **paddings)

        self.botao_cor_preenchimento = Button(
            self.frame,
            text="Preenchimento",
            command=self.escolher_cor_preenchimento
        )
        self.botao_cor_preenchimento.grid(column=1, row=1, sticky=W, **paddings)

        self.frame.pack()

        self.root.attributes('-topmost', 1)

    def escolher_cor_borda(self):
        cor = colorchooser.askcolor()[1]
        if cor:
            self.cor_atual = cor

    def escolher_cor_preenchimento(self):
        cor = colorchooser.askcolor()[1]
        if cor:
            self.background = cor

    def desenhar_figuras(self, figuras):
        self.canvas.delete("all")
        for figura in figuras:
            figura.desenhar(self.canvas)

    #Persistência
    def comandos_arquivos(self, comando_salvar, comando_abrir):
        #o Controller chama isso passando suas próprias funções (comando_salvar, comando_abrir)
        self.menu_arquivo.add_command(label = 'Salvar', command = comando_salvar)
        self.menu_arquivo.add_command(label = 'Abrir',  command = comando_abrir)

    def pedir_caminho_salvar(self):
        caminho = filedialog.asksaveasfilename(defaultextension = ".json",
        filetypes=[("Arquivos JSON", "*.json")],
        title= "Salvar desenho como:")

    def pedir_caminho_abrir(self):
        caminho = filedialog.askopenfilename(defaultextension=".json",
        filetypes=[("Arquivos JSON", "*.json")],
        title="Abrir desenho:")

    def mostrar_erro(self, mensagem):
        messagebox.showerror("Erro", mensagem)


    def iniciar(self):
        self.root.mainloop()