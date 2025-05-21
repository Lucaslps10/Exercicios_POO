from exercicios_da_apostila.topico_2.subtop_2_3.inimigo import Inimigo

class Chefe(Inimigo):
    def __init__(self, nome, vida, forca):

        super().__init__(nome, vida * 2, forca * 2)

chefe = Chefe("Dragão", 100, 10)
print(chefe.nome)
print(chefe.forca)
print(chefe.vida)
chefe.tomar_dano(10)

    
