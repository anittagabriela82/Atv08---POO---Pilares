class Pessoa:  # Classe pai
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_dados(self):
        print(f'O nome do pai é {self.nome} e sua idade é {self.idade}anos')
class Aluno(Pessoa):  # Classe filha
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)  # chama o construtor da classe pai
        self.matricula = matricula
    def exibir_dados(self):
        print(f'O nome do aluno é {self.nome}, tem {self.idade} anos e a matrícula foi feita em {self.matricula}.')
class Professor (Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade) 
        self.disciplina = disciplina
        super().exibir_dados()
        print(f'O nome do aluno é {self.nome}, tem {self.idade},com as disciplinas {self.disciplina}')
print("---PAI---") 
pai = Pessoa("sergio", 45)
pai.exibir_dados()
print("---ALUNO---") 
aluno = Aluno("ana", 28, "2025")
aluno.exibir_dados()
print("---PROFESSOR---") 
professor = Professor('luiz',27,'Portugues e matematica')
professor.exibir_dados()