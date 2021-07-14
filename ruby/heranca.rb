class Carro
  
    def initialize; end
  
    def setar_cor(cor)
      @cor = cor
    end

    def informar_cor
        puts "Cor: #{@cor}"
    end

end
  
# relação é do tipo
class Camaro < Carro

    def initialize(modelo)
        @modelo = "Camaro " + modelo
    end

    def informar_modelo
      puts "Modelo: #{@modelo}"
    end
end

if __FILE__ == $0
    camaro = Camaro.new("2018")
    camaro.setar_cor("Amarelo")
    camaro.informar_modelo
    camaro.informar_cor
end