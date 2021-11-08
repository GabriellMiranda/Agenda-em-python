from pessoa import Pessoa
class Node:
    def __init__(self, nome, idade):
        self.data = Pessoa(nome, idade)
        self.proximo = None
    
    def Imprime_Pessoa(self):
      self.data.P_pessoa()