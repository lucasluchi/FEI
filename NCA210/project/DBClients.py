import csv

dbClients = "quempoupatem.csv"
tbClients = ['CPF', 'NOME', 'CONTA', 'SALDO', 'SENHA']

dbBankStatement = "statement.csv"
tbBankStatement = ['CPF', 'DATA', 'VALOR', 'TARIFA', 'SALDO']

# Cadastra um novo cliente
def CreateClient(data):
    dbAppend = {
        "CPF": data[1],
        "NOME": data[0],
        "CONTA": data[2],
        "SALDO": data[3],
        "SENHA": data[4]
    }

    dbInsert = []

    # abre o arquivo e lê todos os dados
    with open(dbClients, 'r') as csvfile:
        read = csv.DictReader(csvfile)

        for item in read:
            dbInsert.append(dict(item))

    # verifica se o CPF já está cadastrado, se estiver
    # retorna False indicando que não foi possível cadastrar o cliente
    for line in dbInsert:
        for col, val in line.items():
            if str(data[1]) in val and col == 'CPF':
                return False

    # limpa os dados lidos para quando der o append não acumular
    # com o que foi lido
    dbInsert.clear()

    # da o append na nova linha com os dados do cliente
    with open(dbClients, 'a', newline="") as csvfile:
        dbInsert.append(dbAppend)

        write = csv.DictWriter(csvfile, fieldnames=tbClients)

        for item in dbInsert:
            write.writerow(item)

    # retorna True indicando que o cliente foi cadastrado com sucesso
    return True
