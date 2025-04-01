class Tarefa:
    def __init__(self, tipo_de_tarefa, data_inicio, horas_por_dia, data_fim):
        self.tipo_de_tarefa = tipo_de_tarefa
        self.data_inicio = data_inicio
        self.horas_por_dia = horas_por_dia
        self.data_fim = data_fim

tarefa1 = Tarefa("Organzar a biblioteca", "20/01/25", "4 horas", "10/03/25")

print(tarefa1.tipo_de_tarefa)
print(tarefa1.data_inicio)
print(tarefa1.horas_por_dia)
print(tarefa1.data_fim)        