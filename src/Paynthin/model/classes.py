#Aqui ficarão as classes que permitem criar as figuras
import json
#Classe base
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
    #Adicionando a percistência
    def _dict(self): #transforma a figura em um dicionário, que é serializável
        return {'tipo': self.__class__.__name__,
                'x1': self.x1,
                  'y1': self.y1,
                    'x2': self.x2,
                      'y2': self.y2,
                        'cor_borda': self.cor_borda,
                          'cor_preenchimento': self.cor_preenchimento}
    @classmethod
    def from_dict(cls, dados): #reconstrói com base no nome da classe, não no  do menu
        classe = classes_nome.get(dados['tipo'])
        if classe is None:
            raise ValueError(f'Tipo de figura não reconhecido: {dados['tipo']}')
        return classe.from_dict_esp(dados)
    @classmethod
    def from_dict_esp(cls, dados):  #reconstrução "padrão", serve pra quase todas as figuras (menos o Rabisco)
        figura = cls(dados['x1'], dados['y1'], dados['x2'], dados['y2'], dados['cor_borda'], dados['cor_preenchimento'])
        return figura

    

#Subclasses
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
    #aqui a gnt adiciona diretamente a persistencia pq é diferete
    def to_dict(self):
        return {
            'tipo': self.__class__.__name__,
            'cor_borda': self.cor_borda,
            'pontos': self.pontos, #lista de tuplas (x, y)
        }

    @classmethod
    def _from_dict_especifico(cls, dados):
        primeiro_x, primeiro_y = dados['pontos'][0]
        figura = cls(primeiro_x, primeiro_y, dados['cor_borda'])
        figura.pontos = [tuple(ponto) for ponto in dados['pontos']] #json vira lista, convertemos de volta pra tupla
        return figura

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

class Triangulo(Figura):
    def desenhar(self, canvas):
        pontos = [(self.x1 + self.x2)/2, self.y1, self.x1, self.y2, self.x2, self.y2]
        canvas.create_polygon(pontos, outline = self.cor_borda, fill = self.cor_preenchimento if self.cor_preenchimento else '') #concertado
    def incompleta(self):
        return self.x1 == self.x2 and self.y1 == self.y2

class Pentagono(Figura):
    def desenhar(self, canvas):
        pontos = [(self.x1 + self.x2)/2, self.y1,
                  self.x1, (self.y1 + self.y2)/2,
                  self.x1 + (self.x2-self.x1)*0.2, self.y2,
                  self.x2 - (self.x2-self.x1)*0.2, self.y2,
                  self.x2, (self.y1 + self.y2)/2]
        canvas.create_polygon(pontos, outline = self.cor_borda, fill = self.cor_preenchimento if self.cor_preenchimento else '') #concertado
    def incompleta(self):
        return self.x1 == self.x2 and self.y1 == self.y2

class Hexagono(Figura):
    def desenhar(self, canvas):
        pontos = [self.x1 + (self.x2-self.x1)*0.25, self.y1,
                  self.x2 - (self.x2-self.x1)*0.25, self.y1,
                  self.x2, (self.y1+self.y2)/2,
                  self.x2 - (self.x2-self.x1)*0.25, self.y2,
                  self.x1 + (self.x2-self.x1)*0.25, self.y2,
                  self.x1, (self.y1+self.y2)/2]
        canvas.create_polygon(pontos, outline = self.cor_borda, fill = self.cor_preenchimento if self.cor_preenchimento else '') #concertado
    def incompleta(self):
        return self.x1 == self.x2 and self.y1 == self.y2
#registrando as classes por nome, pra poder reconstruir depois
classes_nome = { classe.__name__: classe
                for classe in [Linha, Rabisco, Retangulo, Oval, Circulo, Triangulo, Pentagono, Hexagono]}
tipo_figura = {
    'Linha': Linha,
    'Retângulo': Retangulo,
    'Oval': Oval,
    'Círculo': Circulo,
    'Triângulo': Triangulo,
    'Pentágono': Pentagono,
    'Hexágono': Hexagono,}


# Como já inclui os tipos, agora posso criar a classe Desenho
class Desenho:
    def __init__(self):
        self.figuras = []
        self.figura_nova = None
    def iniciar_figura_nova(self, x, y, tipo, cor_borda, cor_preenchimento):
        classe = tipo_figura.get(tipo)
        if classe is not None:
            self.figura_nova = classe(x, y, x, y, cor_borda, cor_preenchimento)
        else:
            self.figura_nova = Rabisco(x, y, cor_borda) 
        return self.figura_nova
    def atualizar_figura_nova(self, x, y):
        if self.figura_nova is None:
            return
        self.figura_nova.atualizar(x, y)       
    def incluir_figura_nova(self):
        if self.figura_nova is None:
            return 
        if not self.figura_nova.incompleta():
            self.figuras.append(self.figura_nova)
        self.figura_nova = None
    def desenhar_figuras(self, canvas): #aqui é pra gnt garantir que todas as figuras(concluidas e em andamento) seja mostrada 
        if self.figura_nova is not None:
            return self.figuras + [self.figura_nova] 
        else:
            return self.figuras
    #Persistência
    def salvar(self, endereco_arq):
        dados = [ figura._dict() for figura in self.figuras]
        with open(endereco_arq, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
    def carregar(self, endereco_arq):
        with open(endereco_arq, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            self.figuras = [Figura.from_dict(item) for item in dados]
            self.figura_nova = None #qauando carregar, não vai ter figura em andamento
        