class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def inserirEndereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def listaEnderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

    def __del__(self):
        print(self.nome, "foi APAGADO")

class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(self.cidade, self.estado, "foi APAGADO")