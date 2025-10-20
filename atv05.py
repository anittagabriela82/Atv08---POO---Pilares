class Animal:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def falar (self):
        print("O animal faz um som.")

meu_animal = Animal('HELA',2)

meu_animal.falar()
class Cachorro(Animal): 
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    def falar(self):
            print('o meu cachorro está latindo')    

meu_cachorro= Cachorro ('Dog',3)  
meu_cachorro.falar()

class Gato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    def falar(self):
        print('o gato mia!') 

meu_gato = Gato('mimiu',3) 
meu_gato.falar()   
print(f'Meu cachorro se chama {meu_cachorro.nome}, tem {meu_cachorro.idade}')
meu_cachorro.falar()
print()
print(f'meu gato se chama {meu_gato.nome}, tem {meu_gato.idade} anos.')
meu_gato.falar()

# Lista com vários animais (polimorfismo em ação)
animais = [meu_animal, meu_cachorro, meu_gato,]

print("\n🐾 Agora todos os animais vão se apresentar:\n")

for animal in animais:
    print(f"Nome: {animal.nome}, Idade: {animal.idade}")
    animal.falar()
    print()  # linha em branco pra separar
