class Termostato:
    def __init__(self, material, peso, potencia, fabricante):
        self.material = material
        self.peso = peso
        self.potencia = potencia
        self.fabricante = fabricante

termostato1 = Termostato("Plástico", "120g", 110, "Full Gauge")
print(termostato1.material)
print(termostato1.peso) 
print(termostato1.potencia)
print(termostato1.fabricante)       