import random
from exercicios_da_apostila.topico_2.subtop_2_3 import jogador
from exercicios_da_apostila.topico_2.subtop_2_3 import inimigo

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
        jogador1 = jogador.Jogador("Super Mário", 100)
        nome_dos_inimigos = ["Freeza", "Majin-Boo", "Dabura", "Baby", "Cell"]
        num_inimigos = random.randint(1, 3)
        inimigos = [inimigo.Inimigo(random.choice(nome_dos_inimigos), 100, 10) for _ in range(num_inimigos)]

        print(f"\nIniciando o jogo com {num_inimigos} inimigo(s)!")

        turnos_restantes = 10

        for i in inimigos:
            print(f"\nLutando contra {i.nome}")
            while i.vida > 0:
                jogador1.atacar(i)
                turnos_restantes -= 1
                if i.vida <= 0:
                    break
                if jogador1.energia < 10:
                    jogador1.descansar()
                    turnos_restantes -= 1
            if turnos_restantes <= 0:
                break

        print("\nFim da partida!!!")
        print(f"Pontuação final: {jogador1.pontuacao.pontos}")
        if jogador1.pontuacao.pontos == num_inimigos * 10:
            print("Parabéns! Você conseguiu vencer todos os inimigos!")
        else:
            print("Você sobreviveu, mas não conseguiu vencer todos os inimigos.")

#Inicia o menu

menu = Menu("\n##########Menu############")
menu.exibir()