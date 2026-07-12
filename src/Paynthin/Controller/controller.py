from model import classes
from model.classes import Desenho
from View import view

class Controller:
    def __init__(self, view):
        self.view = view
        self.Desenho = Desenho()

        self.view.canvas.bind('<ButtonPress-1>', self.buttonPress)
        self.view.canvas.bind('<B1-Motion>', self.atualizar_figura_nova)
        self.view.canvas.bind('<ButtonRelease-1>', self.buttonRelease)
        # liga os itens do menu Arquivo às funções salvar/abrir daqui do Controller
        self.view.comandos_arquivos(self.salvar, self.abrir)

    def buttonPress(self, event):
        tipo = self.view.tipo_figura_var.get()
        cor_borda = self.view.cor_atual
        cor_preenchimento = self.view.background

        self.Desenho.iniciar_figura_nova(
            event.x,
            event.y,
            tipo,
            cor_borda,
            cor_preenchimento
        )

        self.Desenho.iniciar_figura_nova(
            event.x,
            event.y,
            tipo,
            cor_borda,
            cor_preenchimento
        )

        self.atualizar_tela()

    def atualizar_figura_nova(self, event):
        self.Desenho.atualizar_figura_nova(
            event.x,
            event.y
        )

        self.atualizar_tela()

    def buttonRelease(self, event):
        self.Desenho.incluir_figura_nova()

        self.atualizar_tela()

    def atualizar_tela(self):
        figuras = self.Desenho.desenhar_figuras(self.view.canvas)

        self.view.desenhar_figuras(figuras)
    #Adicionando as funções de salvar e abrir arquivos, que serão chamadas pelo menu Arquivo da View
    def salvar(self):
        endereco_arq = self.view.pedir_caminho_salvar()
        if not endereco_arq:
            return
        try:
            self.Desenho.salvar(endereco_arq)
        except Exception as erro:
            self.view.mostrar_erro(f'Não foi possível salvar o desenho:\n {erro}')

    def abrir(self):
        endereco_arq = self.view.pedir_caminho_abrir()
        if not endereco_arq:
            return
        try:
            self.Desenho.carregar(endereco_arq)
            self.atualizar_tela()
        except Exception as erro:
            self.view.mostrar_erro(f'Não foi possível abrir o desenho:\n {erro}')