import os
import keyboard
import time
import DBClients

#####################################################################
# ---------------------- Variáveis Globais ------------------------ #
#####################################################################

accountType = ["salário", "comum", "plus"]
accountFees = [0.05, 0.03, 0.01]
accountLimits = [0.00, -500.00, -5000.00]

#####################################################################
# ---------------------------- Funções ---------------------------- #
#####################################################################

# tela principal
def ScreenHome():
    os.system("cls")
    print("################# QuemPoupaTem! #################")
    print(" Onde seu dinheiro é mais do que apenas números!\n")
    print("1 - Novo Cliente")
    print("2 - Apaga Cliente")
    print("3 - Debita")
    print("4 - Deposita")
    print("5 - Saldo")
    print("6 - Extrato\n")
    print("0 - Sair")

# tela de dados inválidos
def ScreenInvalidData():
    os.system("cls")
    print("Dados inválidos!")
    print("Verificar os dados com o cliente.")

    # Aguarda 5s para o funcionário ler a mensagem
    time.sleep(5)

    # Volta para a tela pricipal
    ScreenHome()


# menu para cadastro de cliente
def MenuNewClient():
    client = []

    os.system("cls")
    print("Cadastro de novo cliente\n")

    # recebe os dados do cliente
    client.append(input("Nome: "))

    # proteção para caso o cliente insira dados errados
    try:
        client.append(int(input("CPF (somente números): ")))
        print("(0 - salário, 1 - comum e 2 - plus)")
        client.append(int(input("Tipo de conta: ")))
        client.append(float(input("Saldo inicial da conta: R$ ").replace(",",".")))
    except ValueError as e:
        ScreenInvalidData()
        return

    client.append(input("Senha do usuário: "))
    
    # Verifica se o CPF tem o tamanho certo e se o tipo de conta está correta
    if len(str(client[1])) != 11 or (client[2] < 0 or client[2] > 2):   
        # Exibe mensagem de dados inválidos
        ScreenInvalidData()
        return

    # pede uma confirmação dos dados do cliente
    os.system("cls")
    print("Os dados do cliente estão corretos?\n")

    print(f"Nome: {client[0]}")
    print(f"CPF: {client[1]}")
    print(f"Tipo de conta: {accountType[client[2]]}")
    print(f"Saldo inicial da conta: R$ {client[3]:.2f}")
    print(f"Senha do usuário: {client[4]}")

    print("\n\nENTER - sim, salvar")
    print("ESC - não, descartar")

    # aguarda a confirmação
    while True:
        key = keyboard.read_key(True)
        keyboard.read_event(True)

        if key == 'esc':
            ScreenHome()

            break
        elif key == 'enter':
            os.system("cls")

            # cria o cadastro do cliente
            if DBClients.CreateClient(client) == True:
                print("Cliente cadastrado com sucesso!")
            else:
                print("Erro! CPF já cadastrado!")

            time.sleep(3)
            ScreenHome()

            break
        

# menu para deletar o cliente
def MenuDeleteClient():
    # recebe os dados do cliente
    os.system("cls")
    print("Entre com o CPF do cliente que deseja excluir")
    cpf = str(input("CPF (somente números): "))

    # busca os dados do cliente pelo cpf
    client = DBClients.SearchClient(cpf)

    os.system("cls")

    # verifica se o cpf está correto e pede uma confirmação
    if cpf == client['CPF']:
        print("Os dados do cliente estão corretos?\n")

        print(f"Nome: {client['NOME']}")
        print(f"CPF: {client['CPF']}")
        print(f"Tipo de conta: {accountType[int(client['CONTA'])]}")
        print(f"Saldo inicial da conta: R$ {float(client['SALDO']):.2f}")

        print("\n\nENTER - apagar cliente")
        print("ESC - cancelar e retornar")

        # aguardar confirmar ou retornar
        while True:
            key = keyboard.read_key(True)
            keyboard.read_event(True)

            if key == 'esc':
                ScreenHome()
                break
            elif key == 'enter':
                os.system("cls")

                DBClients.DeleteClient(cpf)

                print("Cliente deletado!")

                time.sleep(3)

                ScreenHome()
                break

    else:
        print("Erro! Cliente não encontrado.")

        time.sleep(3)

        ScreenHome()
        

# menu para debitar a conta do cliente
def MenuDebitClient():
    os.system("cls")
    print("Debitar saldo! Entre com os dados do cliente!")

    # pede cpf e senha para liberar o débito
    cpf = str(input("CPF (somente números): "))
    password = str(input("Senha: "))

    # busca os dados do cliente pelo cpf
    client = DBClients.SearchClient(cpf)

    # verifica se o cpf e a senha estão ok
    if cpf == client['CPF']:
        if password == client['SENHA']:

            # pede o valor a ser debitado e calcula o saldo já com o debito e taxas
            value = float(input("Valor a ser debitado: R$ ").replace(",", "."))
            balance = float(client['SALDO']) - value - value * accountFees[int(client['CONTA'])]

            os.system("cls")

            # verifica pelo tipo de conta se o saldo é suficiente
            if balance >= accountLimits[int(client['CONTA'])]:
                client['SALDO'] = balance

                # atualiza o saldo do cliente e salva o histórico
                DBClients.UpdateClient(client)
                DBClients.UpdateBalance(client, value * -1, value * accountFees[int(client['CONTA'])])

                # informa que o valor foi debitado e exibe o novo saldo
                os.system("cls")
                print("Valor debitado com sucesso!\n")

                print(f"Nome: {client['NOME']}")
                print(f"CPF: {client['CPF']}")
                print(f"Saldo: R$ {balance:.2f}")

                time.sleep(2)
            else:
                print("Erro! Saldo insuficiente.")
                print(f"Saldo: R$ {float(client['SALDO']):.2f}")
        else:
            print("Erro! Senha incorreta.")
    else:
        print("Erro! Cliente não encontrado.")

    time.sleep(3)

    ScreenHome()


# menu para creditar a conta do cliente
def MenuCreditClient():
    os.system("cls")
    print("Creditar saldo! Entre com os dados do cliente!")

    # pede o cpf
    cpf = str(input("CPF (somente números): "))

    # faz a busca dos dados do cliente pelo cpf
    client = DBClients.SearchClient(cpf)

    # verifica se encontrou o cliente
    if cpf == client['CPF']:

        # pede o valor para ser creditado e calcula o novo saldo
        value = float(input("Valor a ser creditado: R$ ").replace(",", "."))
        balance = float(client['SALDO']) + value

        os.system("cls")

        client['SALDO'] = balance

        # atualiza o saldo do cliente e salva o histórico
        DBClients.UpdateClient(client)
        DBClients.UpdateBalance(client, value)

        # informa que o valor foi creditado e exibe o novo saldo
        os.system("cls")
        print("Valor creditado com sucesso!\n")

        print(f"Nome: {client['NOME']}")
        print(f"CPF: {client['CPF']}")
        print(f"Saldo: R$ {balance:.2f}")

        time.sleep(2)
    else:
        print("Erro! Cliente não encontrado.")

    time.sleep(3)

    ScreenHome()


# menu para consultar o saldo do cliente
def MenuBalanceClient():
    os.system("cls")
    print("Consultar saldo! Entre com os dados do cliente!")

    # pede cpf e senha
    cpf = str(input("CPF (somente números): "))
    password = str(input("Senha: "))

    # faz a busca dos dados do cliente pelo cpf
    client = DBClients.SearchClient(cpf)

    # verifica se encontrou o cliente e se a senha está correta
    if cpf == client['CPF']:
        if password == client['SENHA']:
            os.system("cls")

            # exibe o saldo atualizado do cliente
            print(f"Nome: {client['NOME']}")
            print(f"CPF: {client['CPF']}")
            print(f"Tipo de conta: {accountType[int(client['CONTA'])]}")
            print(f"Saldo: R$ {float(client['SALDO']):.2f}")

            print("\n\nESC - para voltar")

            while True:
                key = keyboard.read_key(True)
                keyboard.read_event(True)

                if key == 'esc':
                    ScreenHome()
                    return
        else:
            print("Erro! Senha incorreta.")
    else:
        print("Erro! Cliente não encontrado.")

    time.sleep(3)

    ScreenHome()


# menu para consultar o extrato do cliente
def MenuStatementClient():
    os.system("cls")
    print("Consultar saldo! Entre com os dados do cliente!")

    # pede cpf e senha
    cpf = str(input("CPF (somente números): "))
    password = str(input("Senha: "))

    # faz a busca dos dados do cliente pelo cpf
    client = DBClients.SearchClient(cpf)

    # verifica se encontrou o cliente e se a senha está correta
    if cpf == client['CPF']:
        if password == client['SENHA']:
            os.system("cls")

            # monta a tela com NOME, CPF e tipo de conta
            print(f"Nome: {client['NOME']}")
            print(f"CPF: {client['CPF']}")
            print(f"Tipo de conta: {accountType[int(client['CONTA'])]}")

            # faz a busca dos dados do extrato exibe todos
            DBClients.PrintStatement(cpf)

            print("\n\nESC - para voltar")

            while True:
                key = keyboard.read_key(True)
                keyboard.read_event(True)

                if key == 'esc':
                    ScreenHome()
                    return
        else:
            print("Erro! Senha incorreta.")
    else:
        print("Erro! Cliente não encontrado.")

    time.sleep(3)

    ScreenHome()

#####################################################################
# --------------- O programa principal começa aqui ---------------- #
#####################################################################

# printa a tela principal com todas as opções que o sistema oferece
ScreenHome()

# aguarda a escolha de alguma opção
while True:

    # recebe a tecla digitada
    key = keyboard.read_key(True)

    # limpa o evento para não acumular quando entrar nos menus
    keyboard.read_event(True)

    if key == '0':
        break
    elif key == 'esc':
        ScreenHome()
    elif key == '1':
        MenuNewClient()
    elif key == '2':
        MenuDeleteClient()
    elif key == '3':
        MenuDebitClient()
    elif key == '4':
        MenuCreditClient()
    elif key == '5':
        MenuBalanceClient()
    elif key == '6':
        MenuStatementClient()
