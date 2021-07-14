class Endereco

  attr_reader :cep, :numero

  def initialize(cep, numero)
    @cep = cep
    @numero = numero
  end

end

class Cliete

  def initialize(nome, idade)
    @nome = nome
    @idade = idade
    @enderecos = []
  end

  def inserirEndereco(cep, numero)
    @enderecos.push(Endereco.new(cep, numero))
  end

end