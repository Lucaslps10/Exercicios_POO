from exercicios_da_apostila.topico_2.subtop_2_3.jogador import Jogador
from exercicios_da_apostila.topico_2.subtop_2_2.pontuacao import Pontuacao
from exercicios_da_apostila.topico_2.subtop_2_3.inimigo import Inimigo

class JogadorPremium(Jogador):
    def __init__(self, nome, energia, pontuacao = Pontuacao()):
        super().__init__(nome, energia, pontuacao)

    # Usando Extending
    def adicionar_pontos(self, valor):
        super().adicionar_pontos(valor)
        print(f"Bônus Premium de 20 pontos adicionado")

    def atacar(self, oponente):
        return super().atacar(oponente)
    

jp = JogadorPremium("Super boy", 50)
i = Inimigo("Chan", 5, 10)
print(jp.nome)
print(jp.energia)
print(jp.pontuacao)
jp.adicionar_pontos(10)
print(jp.pontuacao)
jp.atacar(i)