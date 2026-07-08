from tkinter import *
from tkinter import ttk
from tkinter import colorchooser

class View:
    def __init__(self):
        self.cor_atual = 'black'
        self.background = None

        self.root = Tk()
        self.root.title('Terceira entrega do Projeto POO')

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

    def iniciar(self):
        self.root.mainloop()