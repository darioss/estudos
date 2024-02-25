require_relative 'conta'

# ContaCorrente < (Herda) de conta
class ContaCorrente < Conta
  attr_accessor :limite
  def initialize(numero, titular, saldo, limite)
    # roda o initialize da classe pai para os atributos herdados
    # Super roda o initialize da classe conta
    super(numero, titular, saldo)
    @limite = limite
  end

  def sacar(valor)
    if valor <= (saldo + limite)
      self.saldo -= valor
      puts "Saque realizado com sucesso!"
      return true
    else
      puts "Saque não realizado, saldo insuficiente!"
      return false
    end
  end

  # O método transferir da classe conta já funciona corretamente,
  # pois em sua lógica interna ele usa o método sacar que é sobrescrito
  # nesta classe, então quando se acessa o método transferir através de
  # um objeto conta corrente, ele chama o método sacar que está na classe
  # ContaCorrente.

end