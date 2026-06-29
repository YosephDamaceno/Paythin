#Classes e Subclasses do projeto

#Classe principal
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
        canvas.create_polygon(pontos, outline = self.cor_borda, fill = self.cor_preenchimento)
    def incompleta(self):
        return self.x1 == self.x2 and self.y1 == self.y2

class Pentagono(Figura):
    def desenhar(self, canvas):
        pontos = [(self.x1 + self.x2)/2, self.y1,
                  self.x1, (self.y1 + self.y2)/2,
                  self.x1 + (self.x2-self.x1)*0.2, self.y2,
                  self.x2 - (self.x2-self.x1)*0.2, self.y2,
                  self.x2, (self.y1 + self.y2)/2]
        canvas.create_polygon(pontos, outline = self.cor_borda, fill = self.cor_preenchimento)
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
        canvas.create_polygon(pontos, outline = self.cor_borda, fill = self.cor_preenchimento)
    def incompleta(self):
        return self.x1 == self.x2 and self.y1 == self.y2