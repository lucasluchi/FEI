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

        if key == 'esc':
            ScreenHome()

            break
        elif key == 'enter':
            os.system("cls")

            # verifica se o CPF já esta cadastrado, se não tenta inserir os dados do cliente
            if DBClients.CreateClient(client) == True:
                print("Cliente cadastrado com sucesso!")
            else:
                print("Erro! CPF já cadastrado!")

            time.sleep(3)
            ScreenHome()

            break
        
# deleta o cliente
def MenuDeleteClient():
    os.system("cls")
    print("Entre com o CPF do cliente que deseja excluir")
    cpf = str(input("CPF (somente números): "))

    client = DBClients.SearchClient(cpf)

    os.system("cls")

    if cpf == client['CPF']:
        print("Os dados do cliente estão corretos?\n")

        print(f"Nome: {client['NOME']}")
        print(f"CPF: {client['CPF']}")
        print(f"Tipo de conta: {accountType[int(client['CONTA'])]}")
        print(f"Saldo inicial da conta: R$ {float(client['SALDO']):.2f}")

        print("\n\nENTER - apagar cliente")
        print("ESC - cancelar e retornar")

        while True:
            key = keyboard.read_key(True)

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
        

#####################################################################
# --------------- O programa principal começa aqui ---------------- #
#####################################################################

# printa a tela principal com todas as opções que o sistema oferece
ScreenHome()

while True:

    key = keyboard.read_key(True)
    
    if key == '0':
        break
    elif key == 'esc':
        ScreenHome()
    elif key == '1':
        MenuNewClient()
    elif key == '2':
        MenuDeleteClient()
    

