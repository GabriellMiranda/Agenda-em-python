from pessoa import Pessoa
from listaCompromisso import ListaCompromisso, ListaCompromisso
class Node:
    lista_de_compromisso = ListaCompromisso()
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

    def insere_compromisso_node_agenda(self, object):
        self.lista_de_compromisso.Insere_compromisso(object)