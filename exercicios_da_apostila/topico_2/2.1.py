#################### Encapsulamento (Public, Private) ############################
import random

class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.__vida = vida

    def mostrar_vida(self):
        return self.__vida

p1 = Personagem("Lucas", 100)
print(p1.mostrar_vida())


class Pontuacao:
    def __init__(self, pontos):
        self.__pontos = pontos

    def adicionar_pontos(self, valor):
        self.__pontos += valor
        
    def mostrar_pontos(self):
        return self.__pontos
    
pontuacao = Pontuacao(0)
pontuacao.adicionar_pontos(10)
print(pontuacao.mostrar_pontos())

class Inimigo:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.__forca = random.randint(5, 20)


    def tomar_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nome} foi derrotado!")
            return True
        else:
            print(f"{self.nome} tem {self.vida} de vida restante!")
            return False

    def mostrar_forca(self):
        return self.__forca
    
    def atacar(self, alvo):
        print(f"{self.nome} atacou com {self.mostrar_forca()} de força!")
        alvo.energia -= self.__forca
        if alvo.energia <= 0:
            alvo.energia = 0
        print(f"Energia do Jogador: {self.energia}")
        
inimigo = Inimigo()

class Jogador:
    def __init__(self):
        self.__energia = 100
        self.pontuacao = Pontuacao()

    def atacar(self, inimigo):
        if self.__energia < 10:
            print("Energia insuficiente para atacar, descanse primeito...")
            self.descansar()
            return 
        dano = random.randint(5, 20)
        print(f"Jogador atacou {inimigo.nome} e causou {dano} de dano!")

        self.__energia -= 10
        print(f"Energia restante: {self.__energia}")

        derrotado = inimigo.tomar_dano(dano)
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
            print("Sem energia suficiente!")

    def recuperar_energia(self, valor):
        if self.__energia + valor > 100:
            recuperado = 100 - self.__energia
        else:
            recuperado = valor
        self.__energia += recuperado
        print(f"Jogador descansou e recuperou {recuperado} de energia. Energia atual: {self.__energia}")
        
       


