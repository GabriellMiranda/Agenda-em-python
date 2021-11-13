from random import randint

class Pessoa:
    ano_atual = 2021
    def __init__(self, nome, idade, cpf):#construtor
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
    
    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome):
        self.nome = nome
    
    def get_idade(self):
        return self.idade
    
    def set_idade(self, idade):
        self.idade = idade
  
    @classmethod #decorado que está decorando este método desta classe
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
    
    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand

    def P_pessoa(self):
        print(f'Nome:{self.get_nome()}, idade:{self.get_idade()}')
