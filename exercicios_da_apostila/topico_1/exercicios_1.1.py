class Jogo:
    def iniciar(self):
        print("O jogo começou!")

jogo = Jogo()
jogo.iniciar()


class Personagem:
    def pular(self):
        print("O personagem pulou!")

p1 = Personagem()
p1.pular()


class Inimigo:
    def atacar(self):
        print("O inimigo atacou!")

inimigo = Inimigo()
inimigo.atacar()

class Pontuacao:
    def zerar_pontos(self):
        print("Pontuação zerada!")

pontuacao = Pontuacao()
pontuacao.zerar_pontos()

class Menu:
    def iniciar_jogo(self):
        print("Carregando jogo...")

    def mostrar_opcoes(self):
            print("Escolha uma opcao!")

    def sair(self):
        print("Você saiu do jogo!")

menu = Menu()
menu.iniciar_jogo()
menu.mostrar_opcoes()
menu.sair()




