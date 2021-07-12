#Classe
class Pessoa:

    #Construtor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    #Métodos
    def andar(self):
        print(self.nome, "está andando")

    def comer(self):
        print(self.nome, "está comendo")

    def fazerAniversario(self):
        self.idade += 1
        print("Agora", self.nome, "tem", self.idade, "anos")

#Objeto
joao = Pessoa("João", 22)

joao.andar()
joao.comer()
joao.fazerAniversario()
