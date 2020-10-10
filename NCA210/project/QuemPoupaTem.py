import os
import keyboard
import csv
import time

#####################################################################
# ---------------------- Variáveis Globais ------------------------ #
#####################################################################

tipoConta = ["salário", "comum", "plus"]

bdNome = "quempoupatem.csv"
bdTabelas = ["CPF", "NOME", "CONTA", "SALDO", "SENHA"]
bdDados = []
bdDadosParaAdd = []

#####################################################################
# ---------------------------- Funções ---------------------------- #
#####################################################################

def TelaPrincipal():
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

def TelaDadosInvalidos():
    os.system("cls")
    print("Dados inválidos!")
    print("Verificar os dados com o cliente.")

    # Aguarda 5s para o funcionário ler a mensagem
    time.sleep(5)

    # Volta para a tela pricipal
    TelaPrincipal()


#def CadastroCliente(nome, cpf, tipo_conta, valor, senha):


def MenuNovoCliente():
    nome = ""
    cpf = 0
    conta = 0
    valor = 0.00
    senha = ""

    os.system("cls")
    print("Cadastro de novo cliente\n")

    nome = input("Nome: ")

    try:
        cpf = int(input("CPF (somente números): "))
        print("(0 - salário, 1 - comum e 2 - plus)")
        conta = int(input("Tipo de conta: "))
        valor = float(input("Saldo inicial da conta: R$ ").replace(",","."))
    except ValueError as e:
        TelaDadosInvalidos()
        return

    senha = input("Senha do usuário: ")
    
    # Verifica se o CPF tem o tamanho certo e se o tipo de conta está correta
    if len(str(cpf)) != 11 or (conta < 0 or conta > 2):   
        # Exibe mensagem de dados inválidos
        TelaDadosInvalidos()
        return

    os.system("cls")
    print("Os dados do cliente estão corretos?\n")

    print("Nome: " + nome)
    print(f"CPF: {cpf}")
    print("Tipo de conta: " + tipoConta[conta])
    print(f"Saldo inicial da conta: R$ {valor:.2f}")
    print("Senha do usuário: " + senha)

    print("\n\nENTER - sim, salvar")
    print("ESC - não, descartar")

    while True:
        key = keyboard.read_key(True)

        if key == 'esc':
            TelaPrincipal()
            break
        elif key == 'enter':
            
            break
        

#####################################################################
# --------------- O programa principal começa aqui ---------------- #
#####################################################################

# printa a tela principal com todas as opções que o sistema oferece
TelaPrincipal()

while True:

    key = keyboard.read_key(True)

    if key == '0':
        if tela == 0:
            break
    elif key == 'esc':
        TelaPrincipal()
    elif key == '1':
        MenuNovoCliente()
    

