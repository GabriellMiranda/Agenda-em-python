from pessoa import Pessoa
class Node:
    def __init__(self, nome, idade, cpf):
        self.data = Pessoa(nome, idade, cpf)
        self.proximo = None
    
    def Imprime_Pessoa(self):
      self.data.P_pessoa()

    def loginCPF(self, cpf):
        if self.data.cpf == cpf:
            return True
        else:
            return False