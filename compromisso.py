class Compromisso:
    def __init__(self, prioridade, dia, mes, ano, hora, min, descricao, duracao):
        self.prioridade = prioridade
        self.dia = dia
        self.mes = mes
        self.ano  = ano
        self.hora = hora
        self.min = min
        self.descricao = descricao
        self.duracao = duracao
    
    def alterar_prioridade(self, new_prioridade):
        self.prioridade = new_prioridade
    
    def retorna_prioridade(self):
        return self.prioridade

    def tem_comflito(self):
        pass

    def imprime_compromisso(self):
        print(f'|Prioridade:{self.prioridade}')
        print(f'|Data:{self.dia}/{self.mes}/{self.ano}')
        print(f'|Hora:{self.hora}:{self.min}')
        print(f'|Descricao do compromisso:{self.descricao}')
        print(f'|Duracao do compromisso:{self.duracao}')    