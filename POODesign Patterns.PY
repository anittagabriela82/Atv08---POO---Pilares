# "CinePython"

class FabricaDeProdutos:
    def eras(self, ingressos):
        self.ingressos = ingressos

    def FabricaRetro(self):
        print("Você escolheu o estilo retrô!")
        print("Ingresso de papel + combo clássico com pipoca e refrigerante.")
        return None

    def FabricaModerna(self):
        print("Você escolheu o estilo moderno!")
        if self.ingressos == 1:
            print("Ingresso com QR code + pipoca gourmet + suco natural.")
        return None


print("Bem-vindo ao CinePython!")
opcao = int(input("Escolha o tipo de ingresso que deseja comprar:\n1 - Retrô ('Ingresso de papel + combo clássico com pipoca e refrigerante.')\n2 - Moderna ('Ingresso com QR code + pipoca gourmet + suco natural')\n→ "))

meu_ingresso = FabricaDeProdutos()
meu_ingresso.eras(opcao)

if opcao == 1:
    meu_ingresso.FabricaRetro()
    print("Ingresso de papel + combo clássico com pipoca e refrigerante.")
elif opcao == 2:
    meu_ingresso.FabricaModerna()
    print("Ingresso com QR code + pipoca gourmet + suco natural.")
else:
    print("Opção inválida!")

        

