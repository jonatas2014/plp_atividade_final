class CarrinhodeCompras

    def initialize
        @produtos = []
    end

    def inserir_produto(produto)
        @produtos.push(produto)
    end

    def lista_produtos
        @produtos.each do |produto|
            puts "Nome: #{produto.nome} Valor: #{produto.valor}"
        end
    end

end

class Produto

    attr_reader :nome, :valor

    def initialize(nome, valor)
        @nome = nome
        @valor = valor
    end

end

if __FILE__ == $0

    leite = Produto.new("Leite", 10)
    uva = Produto.new("Uva", 5)

    carrinho = CarrinhodeCompras.new
    carrinho.inserir_produto(leite)
    carrinho.inserir_produto(uva)

    carrinho.lista_produtos

end