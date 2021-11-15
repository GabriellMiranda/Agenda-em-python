from nodeCompromisso import NodeCompromisso
class ListaCompromisso:
    def __init__(self, cont):
        self.cabeca = None
        self.id = cont
    
    def Insere_compromisso(self, object):
        if self.cabeca:
            ponteiro = self.cabeca
            while(ponteiro.proximo):
                ponteiro = ponteiro.proximo
            ponteiro = NodeCompromisso(object)
        else:
            self.cabeca = NodeCompromisso(object)
       
    def imprimir_compromissos(self):
        pass
