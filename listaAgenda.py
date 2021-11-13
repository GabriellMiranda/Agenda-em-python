from nodeAgenda import Node

class ListaAgenda:
    def __init__(self):
        self.cabeca = None
        self.size = 0
    
    def InserePessoa(self, nome, idade, cpf):
        if self.cabeca:
            ponteiro = self.cabeca
            while(ponteiro.proximo):
                ponteiro = ponteiro.proximo
            ponteiro.proximo = Node(nome, idade, cpf)
        else:
            self.cabeca = Node(nome, idade, cpf)
    
    def login(self, cpf):
        if self.cabeca:
            ponteiro = self.cabeca
            while(ponteiro.loginCPF(cpf) == False):
                ponteiro = ponteiro.proximo
            return ponteiro.data

    def imprime(self):
        pointer = self.cabeca
        while(pointer != None):
            pointer.Imprime_Pessoa()
            pointer = pointer.proximo