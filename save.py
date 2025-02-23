import pandas as pd
import time
import calendar
from datetime import datetime

pathGeral ="gastoMensal.txt"
tetoGastosGeral = 975

def resetaDinheiro(filePathGeral):
    check = int(input('Resetar?\n'
                      '1 - Sim\n'
                      '2 - Nao\n'))
    if(check != 1):
        return 0
    gastosGeral = getGastos(filePathGeral)
    restanteGeral = gastosGeral - tetoGastosGeral
    f = open(filePathGeral, "w")
    f.write(str(restanteGeral))
    f.close()


def getGastos(filePath):
    arq = open(filePath)
    gastoAtual = arq.readline()
    gastoAtual = float(gastoAtual)
    return gastoAtual


def inseriGasto(filePath, total):
    try:
        gastoTotal = getGastos(filePath)
        gastoTotal = gastoTotal + total
        gastoTotal = str(gastoTotal)
        with open(filePath, "w") as f:
            f.write(gastoTotal)

        df = pd.read_csv('logGastos.csv')
        data_atual = datetime.now().strftime("%d/%m %H:%M")
        novo_registro = pd.DataFrame({'data': [data_atual], 'valor': [total]})
        df = pd.concat([df, novo_registro], ignore_index=True)
        df.to_csv('logGastos.csv', index=False)
        print()
    except:
        print("Erro")

def getInformacoesMes():
    dia = time.localtime().tm_mday
    mes = time.localtime().tm_mon
    ano = time.localtime().tm_year
    _, diasMes = calendar.monthrange(ano, mes)
    return dia, mes, ano, diasMes

def mostraRestante(dia, diasMes, tetoGastos, filePath):
    dia += 1
    limiteDiario = tetoGastos/diasMes
    valorGasto = getGastos(filePath)
    
    print(f"Valor a Ser gasto Total: {tetoGastos - valorGasto}")
    print(f"Você tem: {(limiteDiario * dia - valorGasto):.2f} de saldo extra")

def menu(filePathGeral):
    dia, mes, ano, diasMes = getInformacoesMes()
    resp = 1
    while (resp != 0):
        resp = int(input("1 - Resetar Valores\n"
                         "2 - Inserir Gasto Geral\n"
                         "3 - mostar Gasto Total\n"))
        if (resp == 1):
            resetaDinheiro(filePathGeral)
        elif (resp == 2):
            total = float(input("Total: "))
            inseriGasto(filePathGeral, total)
            mostraRestante(dia, diasMes, tetoGastosGeral, pathGeral)
        elif (resp == 3):
            print('\nRestante Geral:')
            mostraRestante(dia, diasMes, tetoGastosGeral, pathGeral)
            print()
menu(pathGeral)
