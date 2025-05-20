import random

from exercicios_da_apostila.topico_2.subtop_2_2 import pontuacao
from exercicios_da_apostila.topico_2.subtop_2_3 import inimigo



class Jogador:
    def __init__(self, nome, energia, pontuacao = pontuacao.Pontuacao()):
        self.nome = nome
        self.__energia = energia
        self.pontuacao = pontuacao

    @property
    def energia(self):
        return self.__energia
    
    @energia.setter
    def energia(self, valor):
        self.__energia += valor
        
    def adicionar_pontos(self, valor):
        self.pontuacao += valor

    def atacar(self, oponente):

        if self.__energia < 10:
            print("Energia insuficiente para atacar, descanse primeito...")
            self.descansar()
            return 
        dano = random.randint(5, 20)
        print(f"Jogador atacou {oponente.nome} e causou {dano} de dano!")

        self.__energia -= 10
        print(f"Energia restante: {self.__energia}")

        derrotado = oponente.tomar_dano(dano)
        if derrotado:
            self.pontuacao.adicionar_pontos(10)
        
    def descansar(self):
        if self.energia + 20 > 100:
            recuperado = 100 - self.__energia
        else:
            recuperado = 20
        self.__energia += recuperado
        print(f"Jogador descansou e recuperou {recuperado} de energia. Energia atual: {self.energia}")

    def usar_energia(self, valor):
        self.__energia -= valor
        print(f"Energia usada: {valor} Restante: {self.energia}")
        if self.__energia < 0:
            self.__energia = 0
            print("Sem energia suficiente!")

    def recuperar_energia(self, valor):
        if self.__energia + valor > 100:
            recuperado = 100 - self.__energia
        else:
            recuperado = valor
        self.__energia += recuperado
        print(f"Jogador recuperou {recuperado} de energia. Energia atual: {self.__energia}")

jogador1 = Jogador("Slash", 100, 0)
inimigo1 = inimigo.Inimigo("Caos", 100, 10)
print(jogador1.nome)
print(jogador1.energia)
jogador1.adicionar_pontos(10)
print(jogador1.pontuacao)
jogador1.atacar(inimigo1)
