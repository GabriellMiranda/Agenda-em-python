from node import Node

class Agenda:
    def __init__(self):
        self.cabeca = None
        self.seze = 0
    
    def InserePessoa(self, nome, idade):
        if self.cabeca:
            ponteiro = self.cabeca
            while(ponteiro.proximo):
                ponteiro = ponteiro.proximo
            ponteiro.proximo = Node(nome, idade)
        else:
            self.cabeca = Node(nome, idade)
        
    def imprime(self):
        pointer = self.cabeca
        while(pointer != None):
            pointer.Imprime_Pessoa()
            pointer = pointer.proximo