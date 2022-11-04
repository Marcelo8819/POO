class Pessoa:
    ano_atual = 2022 # atributo da class Pessoa 

    def __init__(self,nome, idade): # construtor  e atributo da instância
        self.nome = nome 
        self.idade = idade

    def get_ano_nasc(self):
        print(self.ano_atual- self.idade) # são atributos da instância

    @classmethod
    def por_ano_nasc(cls,nome, ano_nasc):
        idade = cls.ano_atual - ano_nasc
        return cls(nome,idade)

#p1 = Pessoa.por_ano_nasc('Luiz',1989)
p1 = Pessoa('Luiz',33)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nasc()