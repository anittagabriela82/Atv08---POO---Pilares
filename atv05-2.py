from atv05 import*
class Passaro (Animal):
    def __init__(self,nome,idade):
      super().__init__(nome, idade)
    def falar(self):
       print('piu piu!')

meu_passaro= Passaro('piupiu',1)
print(f'meu passaro se chama {meu_passaro.nome} e tem {meu_passaro.idade} ano')
print()
meu_passaro.falar()

animais = [meu_animal, meu_cachorro, meu_gato,meu_passaro]

print("Agora todos os animais irão falar!\n")
for animal in animais:
    print(f"{animal.nome}: ", end="")
    animal.falar()