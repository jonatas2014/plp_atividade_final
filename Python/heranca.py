#Superclasse ou classe pai, também chamada de classe base
class Funcionario:
    def __init__(self, id, nome, depto, salario):
        self.id = id
        self.nome = nome
        self.depto = depto
        self.salario = salario

#Classes filhas (extendem a superclasse) 

class Engenheiro(Funcionario): 
    def __init__(self, id, nome, depto, salario, crea):
        super().__init__(id, nome, depto, salario) 
        self.crea = crea

class Advogado(Funcionario): 
    def __init__(self, id, nome, depto, salario, n_oab):
        super().__init__(id, nome, depto, salario) 
        self.n_oab = n_oab


