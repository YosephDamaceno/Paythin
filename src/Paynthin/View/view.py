from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import messagebox

class View:

    '''
    Classe responsável por apresentar a interface gráfica do sistema.

    Sua responsabilidade é exibir os componentes visuais da aplicação,
    permitindo que o usuário interaja com o sistema por meio da janela,
    botões, menus e área de desenho. Todas as ações realizadas pelo
    usuário serão posteriormente tratadas pelo Controller.

    Informações relevantes:
    Esta classe não realiza o processamento das regras de negócio nem
    manipula diretamente os dados do sistema.

    @author Luciano Davi
    @version 1.0
    '''

    def __init__(self):
        '''
        Constrói a interface gráfica da aplicação.

        Inicializa todos os componentes visuais da janela principal,
        incluindo menus, botões, área de desenho e seleção das figuras.

        @throws Nenhuma exceção é lançada diretamente.
        '''

        self.cor_atual = 'black'
        self.background = None
        paddings = {'padx': 5, 'pady': 5}

        self.root = Tk()
        self.root.title('Paynthin')

        #Parte da persistência, menu Arquivo (Salvar/Abrir)
        self.menu_bar = Menu(self.root)
        self.menu_arquivo = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='Arquivo', menu=self.menu_arquivo)
        self.root.config(menu=self.menu_bar)

        self.frame = Frame(self.root)


        self.label = ttk.Label(
            self.frame,
            text='Tipo da Figura:'
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

        self.option_menu.grid(column=0, row=1, sticky=W, **paddings)

        self.canvas = Canvas(self.frame, bg='white', width=1080, height=720)
        self.canvas.grid(
            column=0, 
            row=3, 
            columnspan=3, 
            sticky=W, 
            **paddings
            )

        self.label = ttk.Label(
            self.frame,
            text='Cor da Figura:'
        )
        self.label.grid(column=1, row=0, sticky=W, **paddings)

        self.botao_cor_preenchimento = Button(
            self.frame,
            text="Preenchimento",
            command=self.escolher_cor_preenchimento
        )
        self.botao_cor_preenchimento.grid(column=1, row=1, sticky=W, **paddings)

        self.label = ttk.Label(
            self.frame,
            text='Cor da Borda:'
        )
        self.label.grid(column=2, row=0, sticky=W, **paddings)

        self.botao_cor_borda = Button(
            self.frame,
            text="Borda",
            command=self.escolher_cor_borda
        )
        self.botao_cor_borda.grid(column=2, row=1, sticky=W, **paddings)


        self.frame.pack()

        self.root.attributes('-topmost', 1)

    def escolher_cor_borda(self):
        '''
        Abre uma janela para que o usuário escolha a cor da borda das
        próximas figuras desenhadas.

        Observação:
        Caso nenhuma cor seja escolhida, a cor anteriormente utilizada
        permanece inalterada.
        '''

        cor = colorchooser.askcolor()[1]
        if cor:
            self.cor_atual = cor

    def escolher_cor_preenchimento(self):
        '''
        Abre uma janela para que o usuário escolha a cor de preenchimento
        das próximas figuras desenhadas.

        Observação:
        Caso nenhuma cor seja escolhida, o preenchimento anteriormente
        configurado permanece inalterado.
        '''

        cor = colorchooser.askcolor()[1]
        if cor:
            self.background = cor

    def desenhar_figuras(self, figuras):
        '''
        Desenha todas as figuras presentes na lista recebida sobre a
        área de desenho da aplicação.

        @param figuras Lista contendo os objetos que deverão ser
        desenhados no Canvas.

        @see Figura.desenhar()
        '''

        self.canvas.delete("all")
        for figura in figuras:
            figura.desenhar(self.canvas)
            
    #Persistência
    def comandos_arquivos(self, comando_salvar, comando_abrir):
        '''
        Associa as funções responsáveis por salvar e abrir arquivos
        aos comandos do menu "Arquivo".

        @param comando_salvar Função que será executada ao selecionar
        a opção "Salvar".

        @param comando_abrir Função que será executada ao selecionar
        a opção "Abrir".

        Observação:
        As funções recebidas são implementadas pelo Controller,
        permitindo que a View permaneça desacoplada da lógica do sistema.
        '''

        #o Controller chama isso passando suas próprias funções (comando_salvar, comando_abrir)
        self.menu_arquivo.add_command(label = 'Salvar', command = comando_salvar)
        self.menu_arquivo.add_command(label = 'Abrir', command = comando_abrir)

    def pedir_caminho_salvar(self):
        '''
        Abre uma janela para que o usuário escolha o local e o nome
        do arquivo onde o desenho será salvo.

        @return Caminho selecionado pelo usuário. Retorna uma string
        vazia caso a operação seja cancelada.
        '''

        caminho = filedialog.asksaveasfilename(
        defaultextension = ".json",
        filetypes = [("Arquivos JSON", "*.json")],
        title = "Salvar desenho como:")

        return caminho

    def pedir_caminho_abrir(self):
        '''
        Abre uma janela para que o usuário selecione um arquivo
        contendo um desenho previamente salvo.

        @return Caminho do arquivo selecionado. Retorna uma string
        vazia caso a operação seja cancelada.
        '''

        caminho = filedialog.askopenfilename(
        defaultextension = ".json",
        filetypes = [("Arquivos JSON", "*.json")],
        title = "Abrir desenho:")

        return caminho

    def mostrar_erro(self, mensagem):
        '''
        Exibe uma janela de erro contendo a mensagem recebida.

        @param mensagem Texto que será apresentado ao usuário na
        janela de erro.
        '''

        messagebox.showerror("Erro", mensagem)

    def iniciar(self):
        '''
        Inicia a execução da interface gráfica da aplicação.

        Observação:
        Este método deve ser chamado apenas uma vez, ao final da
        configuração do sistema, para iniciar o loop principal do
        Tkinter.
        '''

        self.root.mainloop()