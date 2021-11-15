from pessoa import Pessoa
from listaAgenda import ListaAgenda
from compromisso import Compromisso
#gabriel

AgendaDePessoas = ListaAgenda()

opcao = True
opcao1 = True
while(opcao):
    print("|-----------------------------------------------------------|")
    print("|    1 - Criar Agenda                                       |")
    print("|    2 - Faça Login                                         |")
    print("|    3 - Leitura de Arquivo                                 |")
    print("|    4 - Imprimir Agenda                                    |")
    print("|    5 - Sair                                               |")
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
            print("\nLogin Efetuado com sucesso!!\n")
            print(f'Seja Bem vindo {ponteiro.nome}')
            while(opcao1):
                print("|-----------------------------------------------------------|")
                print("|    1 - Cria Compromisso                                   |")
                print("|    2 - Alterar Prioridade                                 |")
                print("|    3 - Verificar Compromisso                              |")
                print("|    4 - Imprimir Compromisso                               |")
                print("|    5 - Imprimir dados do Usuario                          |")
                print("|    6 - Sair                                               |")
                print("|-----------------------------------------------------------|")
                op1 = int(input("Opcao:"))
                if op1 == 1:
                    dia, mes, ano = input("Digite a data - Ex: 12/12/2000").split("/")
                    hora, min = input("Digite a hora do compromisso - Ex: 00:00").split(":")
                    duracao = input("Digite a Duracao do Compromisso:")
                    descricao = input("Digite uma pequena descricao do compromisso:")
                    prioridade = int(input("Digite a prioridade deste compromisso:"))
                    #print(f'{dia}/{mes}/{ano}')
                    compromisso_individuo = Compromisso(prioridade, dia, mes, ano, hora, min, descricao, duracao)
                elif op1 == 2:
                    pass
                elif op1 == 3:
                    pass
                elif op1 == 4:
                    pass
                elif op1 == 5:
                    pass
                else:
                    print("Opcao Invalida!!")
        else:
            print("Seu CPF não foi encontrado!!")

    elif op == 3:
        nomeArquivo = input("Digite o nome do Arquivo a ser lido:")
        with open(nomeArquivo) as Arquivo:
         firstline = next(Arquivo)
        print(firstline)
        for i in range(int(firstline)):
            print(Arquivo)

    elif op == 4:
        AgendaDePessoas.imprime()

    elif op == 5:
        op = False
    else:
        print("Opcao Invalida!!")
    


