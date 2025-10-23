class Cofrinho:
    def __init__(self):
        self.__saldo = 0
    def depositar(self,valor):
        if valor > 0:
            print(f'depositando: {valor}')
            self.__saldo += valor
        else:
            print('digite um valor positivo!')
    def retirar(self,valor):
        if valor <= self.__saldo:
            print(f'retirandooo!{valor}')
            self.__saldo -= valor
        else:
            print("saldo indisponivel, digite um valor menor!")
    def ver_saldo(self):
        print(f' seu saldo é de {self.__saldo}')
        return self.__saldo
meu_cofre = Cofrinho()
meu_cofre.depositar(50)
meu_cofre.retirar(20)
print(meu_cofre.ver_saldo())     


