#Aqui ficarão as classes que permitem criar as figuras
import json

#Classe base
class Figura:
    '''
    Classe base que define os parâmetros comuns das figuras do sistema.

    Sua responsabilidade é fornecer os atributos e métodos que serão
    herdados por todas as figuras geométricas implementadas no sistema.

    Informações relevantes:
    Esta classe não deve ser utilizada diretamente para criação de
    objetos, servindo apenas como base para as subclasses.

    @author Yoseph Damaceno
    @version 1.0
    '''

    def __init__(self, x1, y1, x2, y2, cor_borda, cor_preenchimento=None):
        '''
        Inicializa os atributos básicos de uma figura.

        @param x1 Coordenada X inicial.
        @param y1 Coordenada Y inicial.
        @param x2 Coordenada X final.
        @param y2 Coordenada Y final.
        @param cor_borda Cor utilizada na borda da figura.
        @param cor_preenchimento Cor utilizada no preenchimento da figura.
        '''

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento

    def desenhar(self, canvas):
        '''
        Define o método responsável por desenhar a figura.

        @param canvas Área de desenho onde a figura será desenhada.

        Observação:
        Este método deve ser implementado obrigatoriamente pelas
        subclasses.
        '''

        raise NotImplementedError('Quem herdar, tem que implementar a função desenhar!') #aqui é pra caso tente usar a classe pra desenhar

    def atualizar(self, x2, y2):
        '''
        Atualiza as coordenadas finais da figura.

        @param x2 Nova coordenada X final.
        @param y2 Nova coordenada Y final.
        '''

        self.x2 = x2
        self.y2 = y2

    def incompleta(self):
        '''
        Verifica se a figura está incompleta.

        @return Valor booleano indicando se a figura ainda não pode ser
        considerada concluída.

        Observação:
        Este método deve ser implementado pelas subclasses.
        '''

        raise NotImplementedError('Deve ser implementado pela classe')

    #Adicionando a percistência
    def _dict(self):
        '''
        Converte a figura em um dicionário para possibilitar sua
        serialização.

        @return Dicionário contendo os atributos da figura.
        '''

        return {'tipo': self.__class__.__name__,
                'x1': self.x1,
                  'y1': self.y1,
                    'x2': self.x2,
                      'y2': self.y2,
                        'cor_borda': self.cor_borda,
                          'cor_preenchimento': self.cor_preenchimento}

    @classmethod
    def from_dict(cls, dados):
        '''
        Reconstrói uma figura a partir de um dicionário.

        @param dados Dicionário contendo os dados da figura.

        @return Objeto correspondente à figura reconstruída.

        @throws ValueError Caso o tipo da figura não seja reconhecido.
        '''

        classe = classes_nome.get(dados['tipo'])
        if classe is None:
            raise ValueError(f"Tipo de figura não reconhecido: {dados['tipo']}")
        return classe.from_dict_esp(dados)

    @classmethod
    def from_dict_esp(cls, dados):
        '''
        Reconstrói uma figura utilizando os dados armazenados no
        dicionário recebido.

        @param dados Dicionário contendo os atributos da figura.

        @return Instância da figura reconstruída.
        '''

        figura = cls(dados['x1'], dados['y1'], dados['x2'], dados['y2'], dados['cor_borda'], dados['cor_preenchimento'])
        return figura


#Subclasses
class Linha(Figura):
    '''
    Classe que representa uma linha.

    Sua responsabilidade é armazenar e desenhar uma linha na área
    de desenho utilizando os atributos herdados da classe Figura.

    Informações relevantes:
    A linha é considerada completa quando possui comprimento
    diferente de zero.

    @author Mai Ly
    @version 1.0
    '''

    def desenhar(self, canvas):
        '''
        Desenha uma linha na área de desenho.

        @param canvas Área onde a linha será desenhada.
        '''

        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill = self.cor_borda)

    def incompleta(self):
        '''
        Verifica se a linha possui comprimento válido.

        @return True caso a linha esteja incompleta ou False caso
        contrário.
        '''

        return self.x1 == self.x2 and self.y1 == self.y2

class Rabisco(Figura):
    '''
    Classe que herda os parâmetros da classe Figura.

    Sua responsabilidade é representar um rabisco contínuo
    na área de desenho, armazenando todos os pontos
    percorridos pelo usuário.

    Informações relevantes:
    Diferentemente das demais figuras, o rabisco é composto
    por uma sequência de pontos e possui implementação
    própria para persistência.

    @author Mai Ly
    @version 1.0
    '''

    def __init__(self, x, y, cor_borda):
        '''
        Inicializa um novo rabisco.

        @param x Coordenada X do primeiro ponto.
        @param y Coordenada Y do primeiro ponto.
        @param cor_borda Cor utilizada para desenhar o rabisco.
        '''

        super().__init__(x, y, x, y, cor_borda) #aqui a gnt importa o x1, x2... mas o rabisco começa com um ponto só
        self.pontos = [(x, y)]

    def atualizar(self, x, y):
        '''
        Adiciona um novo ponto ao rabisco.

        @param x Coordenada X do novo ponto.
        @param y Coordenada Y do novo ponto.
        '''

        self.pontos.append((x, y))

    def desenhar(self, canvas):
        '''
        Desenha o rabisco na área de desenho.

        @param canvas Área onde o rabisco será desenhado.
        '''

        canvas.create_line(self.pontos, fill = self.cor_borda)

    def incompleta(self):
        '''
        Verifica se o rabisco possui pontos suficientes
        para ser considerado válido.

        @return True caso o rabisco esteja incompleto ou
        False caso contrário.
        '''

        return len(self.pontos) < 2

    #aqui a gnt adiciona diretamente a persistencia pq é diferete
    def to_dict(self):
        '''
        Converte o rabisco em um dicionário para possibilitar
        sua serialização.

        @return Dicionário contendo os dados do rabisco.
        '''

        return {
            'tipo': self.__class__.__name__,
            'cor_borda': self.cor_borda,
            'pontos': self.pontos, #lista de tuplas (x, y)
        }

    @classmethod
    def _from_dict_especifico(cls, dados):
        '''
        Reconstrói um objeto Rabisco a partir dos dados
        armazenados em um dicionário.

        @param dados Dicionário contendo os dados do rabisco.

        @return Instância da classe Rabisco reconstruída.
        '''

        primeiro_x, primeiro_y = dados['pontos'][0]
        figura = cls(primeiro_x, primeiro_y, dados['cor_borda'])
        figura.pontos = [tuple(ponto) for ponto in dados['pontos']] #json vira lista, convertemos de volta pra tupla
        return figura

class Retangulo(Figura):
    '''
    Classe que herda os parâmetros da classe Figura e
    representa um retângulo.

    Sua responsabilidade é desenhar um retângulo na
    área de desenho utilizando as coordenadas
    fornecidas.

    Informações relevantes:
    O retângulo pode possuir cor de borda e,
    opcionalmente, cor de preenchimento.

    @author Jayk Abreu
    @version 1.0
    '''

    def desenhar(self, canvas):
        '''
        Desenha um retângulo na área de desenho.

        @param canvas Área onde o retângulo será desenhado.
        '''

        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline = self.cor_borda, fill = self.cor_preenchimento)

    def incompleta(self):
        '''
        Verifica se o retângulo possui dimensões válidas.

        @return True caso o retângulo esteja incompleto ou
        False caso contrário.
        '''

        return self.x1 == self.x2 and self.y1 == self.y2


class Oval(Figura):
    '''
    Classe que herda os parâmetros da classe Figura e
    representa um oval.

    Sua responsabilidade é desenhar um oval (elipse)
    na área de desenho utilizando as coordenadas
    fornecidas.

    Informações relevantes:
    O oval pode possuir cor de borda e,
    opcionalmente, cor de preenchimento.

    @author Luciano Davi
    @version 1.0
    '''

    def desenhar(self, canvas):
        '''
        Desenha um oval na área de desenho.

        @param canvas Área onde o oval será desenhado.
        '''

        canvas.create_oval(self.x1, self.y1, self.x2, self.y2, outline = self.cor_borda, fill = self.cor_preenchimento)

    def incompleta(self):
        '''
        Verifica se o oval possui dimensões válidas.

        @return True caso o oval esteja incompleto ou
        False caso contrário.
        '''

        return self.x1 == self.x2 and self.y1 == self.y2

class Circulo(Figura):
    '''
    Classe que herda os parâmetros da Classe
    figura e define uma figura específica. 
    
    É responsável por representar a figura
    de um círculo na área de desenho.

    @author Yoseph Damaceno
    @version 1.0
    '''

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
    '''
    Classe que herda os parâmetros da Classe
    figura e define uma figura específica. 
    
    É responsável por representar a figura
    de um triângulo na área de desenho.

    @author Luciano Davi
    @version 1.0
    '''

    def desenhar(self, canvas):
        pontos = [(self.x1 + self.x2)/2, self.y1, self.x1, self.y2, self.x2, self.y2]
        canvas.create_polygon(pontos, outline = self.cor_borda, fill = self.cor_preenchimento if self.cor_preenchimento else '') #concertado
    def incompleta(self):
        return self.x1 == self.x2 and self.y1 == self.y2

class Pentagono(Figura):
    '''
    Classe que herda os parâmetros da Classe
    figura e define uma figura específica. 
    
    É responsável por representar a figura
    de um pentágono na área de desenho.

    @author Luciano Davi
    @version 1.0
    '''

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
    '''
    Classe que herda os parâmetros da Classe
    figura e define uma figura específica. 
    
    É responsável por representar a figura
    de um hexágono na área de desenho.

    @author Luciano Davi
    @version 1.0
    '''

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
    '''
    Classe base que define tudo que está relacionado
    a desenhar na área de desenho.

    Responsável por específicar quais métodos serão
    utilizados para diferentes ações na área do canvas.

    @author Yoseph Damaceno
    @version 1.0
    '''

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
        