from model import classes
from model.classes import Desenho
from View import view

class Controller:
    '''
    Classe responsável por intermediar as interações
    entre a View e o Model do programa. Gerencia as
    solicitações que serão feitas na View com as respostas
    vindas do Model nos seus métodos específicos.

    @author Jayk Abreu
    @version 1.0
    '''

    def __init__(self, view):
        '''
        Inicializa o controlador estabelecendo a
        ligação entre o View e o Model. Recebe também
        os eventos de mouse que acontecem no View e
        associa aos arquivos relacionados no Model.

        @param view: parte que é responsável
        pela interface gráfica do programa.

        @see View
        '''

        self.view = view
        self.Desenho = Desenho()

        self.view.canvas.bind('<ButtonPress-1>', self.buttonPress)
        self.view.canvas.bind('<B1-Motion>', self.atualizar_figura_nova)
        self.view.canvas.bind('<ButtonRelease-1>', self.buttonRelease)
        # liga os itens do menu Arquivo às funções salvar/abrir daqui do Controller
        self.view.comandos_arquivos(self.salvar, self.abrir)

    def buttonPress(self, event):
        '''
        Esse método é ativado quando o botão
        esquerdo do mouse é pressionado.

        Ele recebe as informações do evento de botão 
        pressionado do View e é resposável por iniciar 
        figuras na interface.

        @param event: responsável por receber as
        informações do clique na interface, nesse
        caso, as coordenadas x e y iniciais.

        @see Desenho.iniciar_figura_nova
        @see atualizar_tela
        '''
        
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

        self.atualizar_tela()

    def atualizar_figura_nova(self, event):
        '''
        Esse método atualiza a figura que está sendo
        desenhada na área de desenho.

        Ele recebe as informações do evento de botão
        pressionado na interface e é responsável por
        atualizar a tela sempre que seus valores
        se alteram.

        @see Desenho.atualizar_figura_nova
        @see atualizar_tela
        '''
        self.Desenho.atualizar_figura_nova(
            event.x,
            event.y
        )

        self.atualizar_tela()

    def buttonRelease(self, event):
        '''
        Esse método é ativado quando o botão
        esquerdo do mouse é solto.

        Ele recebe as informações do evento de botão 
        quando é solto na interface e é responsável por
        incluir o desenho na tela sempre que o evento ocorre.

        @param event: responsável por receber as
        informações do clique na interface, nesse
        caso, as coordenadas x e y finais.

        @see Desenho.incluir_figura_nova
        @see atualizar_tela
        '''
        
        self.Desenho.incluir_figura_nova()

        self.atualizar_tela()

    def atualizar_tela(self):
        '''
        Atualiza a tela da aplicação.

        Solicita ao Model todas as figuras que devem
        ser exibidas e envia essas informações para
        a View desenhá-las na tela.

        @see desenhar_figuras
        '''

        figuras = self.Desenho.desenhar_figuras(self.view.canvas)

        self.view.desenhar_figuras(figuras)
    #Adicionando as funções de salvar e abrir arquivos, que serão chamadas pelo menu Arquivo da View
    def salvar(self):
        '''
        Salva o desenho em um arquivo.

        Solicita à View um local para salvar o arquivo
        e envia esse caminho para o Model realizar
        o salvamento. Caso ocorra algum erro, uma
        mensagem é exibida ao usuário.

        @see pedir_caminho_salvar
        @see mostrar_erro
        '''
        endereco_arq = self.view.pedir_caminho_salvar()
        if not endereco_arq:
            return
        try:
            self.Desenho.salvar(endereco_arq)
        except Exception as erro:
            self.view.mostrar_erro(f'Não foi possível salvar o desenho:\n {erro}')

    def abrir(self):
        '''
        Abre um desenho salvo anteriormente.

        Solicita à View o arquivo que será aberto,
        envia esse caminho para o Model carregar
        as figuras e atualiza a tela.

        Caso ocorra algum erro durante o processo,
        uma mensagem é exibida ao usuário.

        @see pedir_caminho_abrir
        @see atualizar_tela
        @see mostrar_erro
        '''
        endereco_arq = self.view.pedir_caminho_abrir()
        if not endereco_arq:
            return
        try:
            self.Desenho.carregar(endereco_arq)
            self.atualizar_tela()
        except Exception as erro:
            self.view.mostrar_erro(f'Não foi possível abrir o desenho:\n {erro}')