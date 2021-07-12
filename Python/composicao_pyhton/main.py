from classes import Cliente

cliente1 = Cliente('Luiz', 32)
cliente1.inserirEndereco('Belo Horizonte', 'MG')
print(cliente1.nome)
cliente1.listaEnderecos()
del cliente1
print()

cliente2 = Cliente('Maria', 42)
cliente2.inserirEndereco('Salvador', 'BA')
cliente2.inserirEndereco('Porto Alegre', 'RS')
print(cliente2.nome)
cliente2.listaEnderecos()
del cliente2
print()

cliente3 = Cliente('Otavio', 55)
cliente3.inserirEndereco('Brasilia', 'DF')
print(cliente3.nome)
cliente3.listaEnderecos()
del cliente3
print()

