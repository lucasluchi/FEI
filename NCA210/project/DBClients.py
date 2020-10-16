import csv
from datetime import datetime

# banco de dados dos clientes
dbClients = "quempoupatem.csv"
tbClients = ['CPF', 'NOME', 'CONTA', 'SALDO', 'SENHA']

# banco de dados dos extratos
dbBalance = "statement.csv"
tbBalance = ['CPF', 'DATA', 'VALOR', 'TARIFA', 'SALDO']

# cadastra um novo cliente
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

            break

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



# faz a busca do cliente e retonar seus dados através do CPF
def SearchClient(cpf):
    notfound = {
        "CPF": '',
        "NOME": '',
        "CONTA": '',
        "SALDO": '',
        "SENHA": ''
    }

    dbData = []

    # abre o arquivo e lê todos os dados
    with open(dbClients, 'r') as csvfile:
        read = csv.DictReader(csvfile)

        for item in read:
            dbData.append(dict(item))

    # verifica o CPF e retonar os dados do cliente se encontrar
    for line in dbData:
        for col, val in line.items():
            if str(cpf) in val and col == 'CPF':
                return line

            break

    return notfound


# delete o cliente pelo CPF
def DeleteClient(cpf):
    dbData = []

    # abre o arquivo e lê todos os dados
    with open(dbClients, 'r') as csvfile:
        read = csv.DictReader(csvfile)

        for item in read:
            dbData.append(dict(item))

    # verifica o CPF e deleta os dados do cliente se encontrar
    for line in dbData:
        for col, val in line.items():
            if str(cpf) in val and col == 'CPF':
                dbData.remove(line)
            
            break

    # reescreve todo o arquivo sem o cliente que foi deletado
    with open(dbClients, 'a', newline="") as csvfile:
        # limpa todo o arquivo
        csvfile.seek(0)
        csvfile.truncate()
        
        # escreve os dados
        write = csv.DictWriter(csvfile, fieldnames=tbClients)
        write.writeheader()

        for item in dbData:
            write.writerow(item)


# atualiza o saldo do cliente
def UpdateClient(client):
    dbData = []

    # abre o arquivo e lê todos os dados
    with open(dbClients, 'r') as csvfile:
        read = csv.DictReader(csvfile)

        for item in read:
            dbData.append(dict(item))

    # verifica o CPF e atualiza o saldo
    for line in dbData:
        for col, val in line.items():
            if str(client['CPF']) in val and col == 'CPF':
                line['SALDO'] = client['SALDO']
            
            break

    # reescreve todo o arquivo com o novo saldo do cliente
    with open(dbClients, 'a', newline="") as csvfile:
        # limpa todo o arquivo
        csvfile.seek(0)
        csvfile.truncate()
        
        # escreve os dados
        write = csv.DictWriter(csvfile, fieldnames=tbClients)
        write.writeheader()

        for item in dbData:
            write.writerow(item)


# atualiza o extrato do cliente
def UpdateBalance(client, value, fees=0.0):
    dbAppend = {
        "CPF": client['CPF'],
        "DATA": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "VALOR": value,
        "TARIFA": fees,
        "SALDO": client['SALDO']
    }

    dbData = []

    # abre o arquivo e lê todos os dados
    with open(dbBalance, 'r') as csvfile:
        read = csv.DictReader(csvfile)

        for item in read:
            dbData.append(dict(item))

    # limpa os dados lidos para quando der o append não acumular
    # com o que foi lido
    dbData.clear()

    # da o append na nova linha com os dados do extrato
    with open(dbBalance, 'a', newline="") as csvfile:
        dbData.append(dbAppend)

        write = csv.DictWriter(csvfile, fieldnames=tbBalance)

        for item in dbData:
            write.writerow(item)


# printa o extrato atrvés do CPF
def PrintStatement(cpf):
    dbData = []

    # abre o arquivo e lê todos os dados
    with open(dbBalance, 'r') as csvfile:
        read = csv.DictReader(csvfile)

        for item in read:
            dbData.append(dict(item))

    # faz a busca pelo CPF e printa as linhas que encontrar
    for line in dbData:
        for col, val in line.items():
            if str(cpf) in val and col == 'CPF':

                signal = ''
                date = line['DATA']
                fees = f"{float(line['TARIFA']):.2f}"
                balance = f"{float(line['SALDO']):.2f}"

                if float(line['VALOR']) > 0: 
                    signal = '\t+' 
                else: 
                    signal = '\t-'
                    line['VALOR'] = float(line['VALOR']) * -1

                value = f"{float(line['VALOR']):.2f}"

                print('DATA: ' + date + signal + value.rjust(10, ' ') + '\tTarifa: ' + fees.rjust(10, ' ') + '\tSaldo: ' + balance.rjust(10, ' '))
            
            break