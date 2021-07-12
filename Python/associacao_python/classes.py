class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self.ferramenta = None

class Caneta:
    def __init__(self, marca):
        self.marca = marca

    def escrever(self):
        print('Caneta está sendo utilizada...')

class MaquinaDeEscrever:
    def escrever(self):
        print('Máquina está sendo utilizada...')

