from pessoa import Pessoa
from lista import Agenda

#gabriel

AgendaDePessoas = Agenda()

opcao = True
while(opcao):
    print("|-----------------------------------------------------------|\n")
    print("|    1 - Criar Agenda                                       |\n")
    print("|    6 - Imprimir Agenda                                    |\n")
    print("|    7 - Sair                                               |\n")
    print("|-----------------------------------------------------------|\n")
    op = int(input("Opcao:"))
    if op == 1:
        nome = input("Digite o nome da pessoa:")
        idade = int(input(f"{nome} digite sua idade:"))
        AgendaDePessoas.InserePessoa(nome, idade)
    elif op == 6:
        AgendaDePessoas.imprime()
    elif op == 7:
        op = False