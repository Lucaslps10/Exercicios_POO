class Personagem:
    def __init__(self, nome, vida, defesa=0):
        self.nome = nome
        self.__vida = vida
        self.__defesa = defesa

    def mostrar_vida(self):
        return f"{self.nome} tem {self.__vida} de vida."

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
        




    
p = Personagem("Sky", 100)
print(p.vida)
print(p.mostrar_vida())

p.defesa = 50
print(p.defesa)

p.defesa = 110    
print(p.defesa)

p.defesa = -10
print(p.defesa)