#Fazendo uso de módulos, utilizando-os como mixins
  module Foo
    def increment(number)
      number += 1
    end
  end

  class Bar
    include Foo
  
    def initialize; end
  
    def action(number)
      increment(number)
    end
  end
  
  class Something
    include Foo
  
    def initialize; end
  
    def action(number)
      increment(number)
    end
  end