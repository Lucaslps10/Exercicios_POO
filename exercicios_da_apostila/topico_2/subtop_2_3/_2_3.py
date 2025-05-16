
############## Construtores ###############

import random
from subtop_2_2.pontuacao import Pontuacao


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
        self.__forca = forca

    @property
    def forca(self):
        return self.__forca
    
    @forca.setter
    def forca(self, valor):
        if valor >=5 and valor <= 20:
            self.__forca = valor
        else:
            print("A força deve ser no mínimo 5 e no máximo 20!")


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
        print(f"{self.nome} atacou com {self.__forca} de força!")
        alvo.energia -= self.__forca
        if alvo.energia <= 0:
            alvo.energia = 0
            print("Energia insuficiente.")
            
        print(f"Energia do Jogador: {self.energia}")

inimigo = Inimigo("Thanos", 100, 15)


print(inimigo.nome)
print(inimigo.vida)
print(inimigo.forca)

inimigo.forca = 25 

print(inimigo.forca)

class Jogador:
    def __init__(self, nome, energia, pontuacao = Pontuacao):
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

class Menu:
    def __init__(self, titulo):
        self.titulo = titulo

    def exibir(self):
        while True:
            print(self.titulo)
            print("1. Iniciar Jogo")
            print("2. Mostrar Opções")
            print("3. Sair")
            opcao_escolhida = input("Escolha uma opção: ")

            if opcao_escolhida == "1":
                self.iniciar_jogo()
            elif opcao_escolhida == "2":
                self.mostrar_opcoes()
            elif opcao_escolhida == "3":
                print("Saindo do jogo. Bye bye!")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def mostrar_opcoes(self):
        print("\nOpções do jogo: ")
        print("Cada ataque gasta 10 pontos de energia.")
        print("Descansar recupera 20 pontos de energia (máximo 100)")
        print("Cada inimigo derrotado vale 10 pontos.")

    def iniciar_jogo(self):
        jogador = Jogador("Super Mário", 100, 0)
        nome_dos_inimigos = ["Freeza", "Majin-Boo", "Dabura", "Baby", "Cell"]
        num_inimigos = random.randint(1, 3)
        inimigos = [Inimigo(random.choice(nome_dos_inimigos), 100, 10) for _ in range(num_inimigos)]

        print(f"\nIniciando o jogo com {num_inimigos} inimigo(s)!")

        turnos_restantes = 10

        for inimigo in inimigos:
            print(f"\nLutando contra {inimigo.nome}")
            while inimigo.vida > 0:
                jogador.atacar(inimigo)
                turnos_restantes -= 1
                if inimigo.vida <= 0:
                    break
                if jogador.energia < 10:
                    jogador.descansar()
                    turnos_restantes -= 1
            if turnos_restantes <= 0:
                break

        print("\nFim da partida!!!")
        print(f"Pontuação final: {jogador.pontuacao.pontos}")
        if jogador.pontuacao.pontos == num_inimigos * 10:
            print("Parabéns! Você conseguiu vencer todos os inimigos!")
        else:
            print("Você sobreviveu, mas não conseguiu vencer todos os inimigos.")

#Inicia o menu

menu = Menu("\n##########Menu############")
menu.exibir()


        