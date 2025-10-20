#ENCAPSULAMENTO
class ContaBancaria:
    def __init__(self,saldo_inicial):
        self.__saldo = saldo_inicial
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f'Depositado: R${valor}')
        else:
            print('Erro: O valor do depósito deve ser positivo.')
    def sacar(self, valor):
        if valor <= 0:
            print('Erro: O valor do saque deve ser positivo.')
        elif valor > self.__saldo:
            print('Erro: Saldo insuficiente.')
        else:
            self.__saldo -= valor
            print(f'Sacado: R${valor}')
    def get_saldo(self):
        return self.__saldo
    
conta = ContaBancaria(500)  
conta.depositar(500)          
conta.sacar(200)              
print(f'Saldo atual: R${conta.get_saldo()}') 