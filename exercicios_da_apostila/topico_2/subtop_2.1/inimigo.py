import jogador

class Inimigo:
    def __init__(self, nome, vida, forca):
        self.nome = nome
        self.vida = vida
        self.__forca = forca

    @property
    def forca(self):
        return self.__forca
    
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
        print(f"Energia do Jogador: {alvo.energia}")

j1 = jogador.Jogador(100, 15)      
inimigo = Inimigo("Goblin", 100, 20)
inimigo.atacar(j1)