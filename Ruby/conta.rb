require_relative 'cliente'

class Conta
  attr_reader :numero, :titular 
  attr_accessor :saldo
  
  # Dessa forma ele recebe 4 argumentos e cria o
  # objeto dentro do método
  #def initialize(numero, nome, sobrenome, saldo)
  #  @numero = numero
  #  @titular = Cliente.new(nome, sobrenome)
  #  @saldo = saldo
  #end

  # Dessa forma ele recebe 3 argumentos, sendo que
  # Titular já é um objeto
  def initialize(numero, titular, saldo)
    @numero = numero
    @titular = titular
    @saldo = saldo
  end

  def depositar(valor)
    self.saldo += valor
  end

  def sacar(valor)
    if valor <= self.saldo
      self.saldo -= valor
      puts "Saque realizado com sucesso!"
      return true
    else
      puts "Saque não realizado, saldo insuficiente!"
      return false
    end
  end

  def transferir(conta_destino, valor)
    if sacar(valor) != false
      conta_destino.depositar(valor)
    end
  end
end