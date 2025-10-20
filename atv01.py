#carro
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False 
    def ligar(self):
        self.ligado = True
        print("O carro está ligado.")
    def desligar(self):
        self.ligado = False
        print("O carro está desligado.")
    def acelerar(self, valor):
        if self.ligado:
            print(f"Acelerando a {valor} km/h!")
        else:
            print("Não é possível acelerar. O carro está desligado.")
    def frear(self, valor):
        if self.ligado:
            print(f"Freando... reduzindo {valor} km/h.")
        else:
            print("O carro está desligado, não é possível frear.")
    def exibir_informacoes(self):
        print(f"A marca do carro é {self.marca}, o modelo é {self.modelo} e o ano é {self.ano}.")

meu_carro = Carro("Ferrari", "12CILINDRI", 1947)

meu_carro.exibir_informacoes()
meu_carro.ligar()
meu_carro.acelerar(80)
meu_carro.frear(30)
meu_carro.desligar()
