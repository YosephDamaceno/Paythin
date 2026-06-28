from tkinter import *
from tkinter import ttk
from tkinter import colorchooser 

#Adicionando opção de escolher cores
cor_atual = 'black'
background = None

def escolher_cor_borda():
    global cor_atual
    global background
    cor = colorchooser.askcolor()[1]
    if cor:
        cor_atual = cor

def escolher_cor_preenchimento():
    global cor_atual
    global background
    cor = colorchooser.askcolor()[1]
    if cor:
        background = cor

#iniciando a mudança pra POO
class Figura:
    def __init__(self, x1, y1, x2, y2, cor_borda, cor_preenchimento=None):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento
    def desenhar(self, canvas):
        raise NotImplementedError('Quem herdar, tem que implementar a função desenhar!') #aqui é pra caso tente usar a classe pra desenhar
    def atualizar(self, x2, y2):
        self.x2 = x2
        self.y2 = y2
    def incompleta(self): #pra não precisar da função separada depois
        raise NotImplementedError('Deve ser implementado pela classe')
    
class Linha(Figura):
    def desenhar(self, canvas):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill = self.cor_borda)
    def incompleta(self):
        return self.x1 == self.x2 and self.y1 == self.y2 

class Rabisco(Figura):
    def __init__(self, x, y, cor_borda):
        super().__init__(x, y, x, y, cor_borda) #aqui a gnt importa o x1, x2... mas o rabisco começa com um ponto só 
        self.pontos = [(x, y)]
    def atualizar(self, x, y):
        self.pontos.append((x, y))
    def desenhar(self, canvas):
        canvas.create_line(self.pontos, fill = self.cor_borda)
    def incompleta(self):
        return len(self.pontos) < 2

class Retangulo(Figura):
    def desenhar(self, canvas):
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline = self.cor_borda, fill = self.cor_preenchimento)
    def incompleta(self):
        return self.x1 == self.x2 and self.y1 == self.y2
class Oval(Figura):
    def desenhar(self, canvas):
        canvas.create_oval(self.x1, self.y1, self.x2, self.y2, outline = self.cor_borda, fill = self.cor_preenchimento)
    def incompleta(self):
        return self.x1 == self.x2 and self.y1 == self.y2

class Circulo(Figura):
    def atualizar(self, x2, y2):
        dx = x2 - self.x1
        dy = y2 - self.y1

        tamanho = max(abs(dx), abs(dy))

        self.x2 = tamanho + self.x1 if dx >= 0 else self.x1 - tamanho
        self.y2 = tamanho + self.y1 if dy >= 0 else self.y1 - tamanho
    def desenhar(self, canvas):
        canvas.create_oval(self.x1, self.y1, self.x2, self.y2, outline = self.cor_borda, fill = self.cor_preenchimento)
    def incompleta(self):
        return self.x1 == self.x2 and self.y1 == self.y2

# Quando mouse é pressionado
def iniciar_figura_nova(event):
    global figura_nova

    tipo = tipo_figura_var.get()

    if tipo == 'Linha':
        figura_nova = Linha(event.x, event.y, event.x, event.y, cor_atual)

    elif tipo == 'Retângulo':
        figura_nova = Retangulo(event.x, event.y, event.x, event.y, cor_atual, background)

    elif tipo == 'Oval':
        figura_nova = Oval(event.x, event.y, event.x, event.y, cor_atual, background) ### novo ###

    elif tipo == 'Círculo':
        figura_nova = Circulo(event.x, event.y, event.x, event.y, cor_atual, background)
    else:
        figura_nova =  Rabisco(event.x, event.y, cor_atual)


# Quando mouse é movido com o botão pressionado
def atualizar_figura_nova(event):
    global figura_nova
    if figura_nova is None:
        return 
    figura_nova.atualizar(event.x, event.y)
    desenhar_figuras()
    figura_nova.desenhar(canvas)

# Quando mouse é solto
def incluir_figura_nova(event):
    # para evitar incluir figuras incompletas,
    # como uma linha sem comprimento ou um rabisco com um único ponto
    global figura_nova
    if figura_nova is None:
        return 
    if not figura_nova.incompleta():
        figuras.append(figura_nova)
    
    figura_nova = None
    desenhar_figuras()

    desenhar_figuras()

def desenhar_figuras(): #aqui a gnt usa o polimorfismo
    canvas.delete("all")
    for figura in figuras:
        figura.desenhar(canvas)

# a função de desenhar figura nova não vai ser mais necessária



# ******* MAIN ******* #

figuras = []       # Todas as figuras desenhadas
figura_nova = None # Figura que está sendo desenhada, mas ainda não foi incluída em figuras

root = Tk()
root.title('Primeira entrega do Projeto POO')

frame = Frame(root)

# Widgets arranjados com Layout grid dentro de frame
paddings = {'padx': 5, 'pady': 5}

# label
label = ttk.Label(
    frame,
    text='Escolha se vai desenhar linha, Rabisco, retangulo ou oval:'
)
label.grid(column=0, row=0, sticky=W, **paddings)

# option menu
# Guarda o tipo de figura selecionado no option menu
tipo_figura_var = StringVar(root)

option_menu = ttk.OptionMenu(
    frame,
    tipo_figura_var,
    'Linha',
    'Linha',
    'Rabisco',
    'Retângulo',
    'Oval',
    'Círculo'
)

option_menu.grid(column=1, row=0, sticky=W, **paddings)

# Área de desenho
canvas = Canvas(frame, bg='white', width=600, height=600)
canvas.grid(column=0, row=3, columnspan=2, sticky=W, **paddings)
#botão pra escolher cores
botao_cor_borda = Button(frame, text = "Cor da Borda", command = escolher_cor_borda)
botao_cor_borda.grid(column=0, row=1, sticky=W, **paddings)
botao_cor_preenchimento = Button(frame, text = "Preenchimento", command = escolher_cor_preenchimento)
botao_cor_preenchimento.grid(column=1, row=1, sticky=W, **paddings)
frame.pack()

# Eventos de mouse associados ao canvas - com seus callbacks
canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
canvas.bind('<B1-Motion>', atualizar_figura_nova)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)

root.attributes('-topmost', 1)
root.mainloop()
