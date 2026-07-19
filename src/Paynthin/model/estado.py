"""
Implementação do padrão State para a classe Desenho.

Ideia geral:
- EstadoDesenho é a interface (classe abstrata) que todo estado deve seguir.
- EstadoOcioso representa a situação em que nenhuma figura está sendo criada.
- EstadoDesenhando representa a situação em que uma figura está em andamento.

A classe Desenho (em model/classes.py) deixa de checar "if self.figura_nova
is None" e passa a delegar cada ação para o estado atual (self.estado).

@author Yoseph Damaceno
@version: 1.0
"""

from abc import ABC, abstractmethod

class EstadoDesenho(ABC):
    '''
    Interface que define as ações que dependem do estado atual
    do desenho: iniciar, atualizar e incluir uma figura.

    Cada subclasse concreta implementa essas ações de acordo
    com a situação que representa (ocioso ou desenhando).

    @author Yoseph Damaceno
    @version: 1.0
    '''

    @abstractmethod
    def iniciar(self, desenho, x, y, tipo, cor_borda, cor_preenchimento):
        pass

    @abstractmethod
    def atualizar(self, desenho, x, y):
        pass

    @abstractmethod
    def incluir(self, desenho):
        pass


class EstadoOcioso(EstadoDesenho):
    '''
    Estado em que não há nenhuma figura sendo desenhada no momento.
    Só faz sentido "iniciar" uma figura nova; atualizar e incluir
    não têm efeito, pois não há nada em andamento.

    @author Yoseph Damaceno
    @version: 1.0
    '''

    def iniciar(self, desenho, x, y, tipo, cor_borda, cor_preenchimento):
        from model.classes import tipo_figura, Rabisco #importamos aqui pra evitar o erro novamente
        classe = tipo_figura.get(tipo)
        if classe is not None:
            desenho.figura_nova = classe(x, y, x, y, cor_borda, cor_preenchimento)
        else:
            desenho.figura_nova = Rabisco(x, y, cor_borda)

        # a partir de agora, o desenho passa a estar no estado "desenhando"
        desenho.estado = EstadoDesenhando()

    def atualizar(self, desenho, x, y):
        pass  # não há figura em andamento, nada a atualizar

    def incluir(self, desenho):
        pass  # não há figura em andamento, nada a incluir


class EstadoDesenhando(EstadoDesenho):
    '''
    Estado em que uma figura está sendo criada (o usuário
    está com o botão do mouse pressionado, arrastando).

    @author Yoseph Damaceno
    @version: 1.0
    '''

    def iniciar(self, desenho, x, y, tipo, cor_borda, cor_preenchimento):
        # se por algum motivo tentar iniciar outra figura no meio docaminho, primeiro finaliza a atual e depois inicia a nova
        desenho.incluir_figura_nova()
        desenho.estado.iniciar(desenho, x, y, tipo, cor_borda, cor_preenchimento)

    def atualizar(self, desenho, x, y):
        desenho.figura_nova.atualizar(x, y)

    def incluir(self, desenho):
        if not desenho.figura_nova.incompleta():
            desenho.figuras.append(desenho.figura_nova)
        desenho.figura_nova = None

        # volta para o estado ocioso, pronto para uma nova figura
        desenho.estado = EstadoOcioso()
