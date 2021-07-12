from classes import CarrinhodeCompras, Produto

p1 = Produto('Placa de vídeo', 3000)
p2 = Produto('Processador', 1500)
p3 = Produto('Placa mãe', 1000)
p4 = Produto('Memória RAM', 500)
p5 = Produto('Fonte', 500)
p6 = Produto('Gabinete', 400)


mycart = CarrinhodeCompras()

mycart.inserir_produto(p1)
mycart.inserir_produto(p2)
mycart.inserir_produto(p3)
mycart.inserir_produto(p4)
mycart.inserir_produto(p5)
mycart.inserir_produto(p6)

mycart.lista_produto()

print(mycart.soma_total())
