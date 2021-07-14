class Escritor

    def initialize(nome)
        @nome = nome
        @ferramenta = nil
    end

    def atribuir_ferramenta(ferramenta)
        @ferramenta = ferramenta
    end

end

class Caneta

    def initialize(marca)
        @marca = marca
    end

    def escrever
        puts "Caneta está sendo utilizada"
    end

end

if __FILE__ == $0

    pedro = Escritor.new("Pedro")
    caneta = Caneta.new("bic")
    pedro.atribuir_ferramenta(caneta)

end