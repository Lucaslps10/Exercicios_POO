
############## Construtores ###############

import random

class Personagem:
    def __init__(self, nome, vida, defesa=0):
        self.nome = nome
        self.__vida = vida
        self.__defesa = defesa

    def mostrar_vida(self):
        return self.__vida

    @property
    def vida(self):
        return self.__vida
    
    @property
    def defesa(self):
        return self.__defesa
    
    @defesa.setter
    def defesa(self, valor):
        if valor >= 0 and valor <= 100:
            self.__defesa = valor
        else:
            print("Valor tem que estar entre 0 e 100.")

p1 = Personagem("Doni", 100, 200)
print(p1.nome)
print(p1.vida)
print(p1.defesa)


class Inimigo:
    def __init__(self, nome, vida, forca):
        self.nome = nome
        self.vida = vida
        self.__forca = random.randint(5, 20)
        self.forca = forca

    @property
    def forca(self):
        return self.__forca
    
    @forca.setter
    def forca(self, valor):
        if valor >=0:
            self.__forca = valor ########## Corrigir esse método


    def tomar_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nome} foi derrotado!")
            return True
        else:
            print(f"{self.nome} tem {self.vida} de vida restante!")
            return False
    
    def atacar(self, alvo):
        print(f"{self.nome} atacou com {self.mostrar_forca()} de força!")
        alvo.energia -= self.__forca
        if alvo.energia <= 0:
            alvo.energia = 0
            print("Energia insuficiente.")
            
        print(f"Energia do Jogador: {self.energia}")