#POLIMORFISMO
class ExportadorDeDados:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo
    def exportar(self, dados):
        NotImplementedError("Este método deve ser implementado pelas classes filhas.")
class ExportadorParaCSV(ExportadorDeDados):# Classe filha para CSV
    def exportar(self, dados):
        with open(self.caminho_arquivo, 'w', encoding='utf-8') as arquivo:
            for linha in dados:
                arquivo.write(','.join(str(valor) for valor in linha) + '\n')
class ExportadorParaTXT(ExportadorDeDados):  # Classe filha para TXT
        def exportar(self, dados):
            with open(self.caminho_arquivo, 'w', encoding='utf-8') as arquivo:
                for linha in dados:
                    arquivo.write(' | '.join(str(valor) for valor in linha) + '\n')
        def gerar_relatorios(exportadores, dados):
            for exportador in exportadores:
                exportador.exportar(dados)

class ExportadorDeDados:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo

    def exportar(self, dados):
        raise NotImplementedError("Este método deve ser implementado pelas classes filhas.")

class ExportadorParaCSV(ExportadorDeDados):
    def exportar(self, dados):
        with open(self.caminho_arquivo, 'w', encoding='utf-8') as arquivo:
            for linha in dados:
                arquivo.write(','.join(str(valor) for valor in linha) + '\n')

class ExportadorParaTXT(ExportadorDeDados):
    def exportar(self, dados):
        with open(self.caminho_arquivo, 'w', encoding='utf-8') as arquivo:
            for linha in dados:
                arquivo.write(' | '.join(str(valor) for valor in linha) + '\n')

def gerar_relatorios(exportadores, dados):
    for exportador in exportadores:
        exportador.exportar(dados)


# Exemplo de uso
if __name__ == "__main__":
    dados = [
        ["Nome", "Idade", "Cidade"],
        ["Ana", 28, "RECIFE"],
        ["JE", 28, "OLINDA"]
    ]

    exportadores = [
        ExportadorParaCSV("relatorio.csv"),
        ExportadorParaTXT("relatorio.txt")
    ]

    gerar_relatorios(exportadores, dados)
    print("Relatórios gerados com sucesso!")
