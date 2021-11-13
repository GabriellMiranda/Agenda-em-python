from pessoa import Pessoa
from listaAgenda import Agenda

#gabriel

AgendaDePessoas = Agenda()

opcao = True
while(opcao):
    print("|-----------------------------------------------------------|")
    print("|    1 - Criar Agenda                                       |")
    print("|    2 - Faça Login                                         |")
    print("|    6 - Imprimir Agenda                                    |")
    print("|    7 - Sair                                               |")
    print("|-----------------------------------------------------------|")
    op = int(input("Opcao:"))
    if op == 1:
        nome = input("Digite o nome da pessoa:")
        idade = int(input(f"{nome} digite sua idade:"))
        cpf = input("Digite seu CPF:")
        AgendaDePessoas.InserePessoa(nome, idade, cpf)
    elif op == 2:
        cpf = input("Digite seu cpf para fazer login:")
        ponteiro = AgendaDePessoas.login(cpf)
        if ponteiro.cpf == cpf:
            print("Login Efetuado com sucesso!!")
        else:
            print("Seu CPF não foi encontrado!!")
    elif op == 6:
        AgendaDePessoas.imprime()
    elif op == 7:
        op = False