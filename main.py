import time


def reseta(dia):
    arq = open("C:\python projects\Controle-de-Dinheiro\gastoMensal.txt", "w")
    arq.write("000.00")

def insereGasto(gasto_Atual, arq, dia,mes):
    gasto = str(input("Valor do Gasto = "))
    try:
        gastoT = str(gasto_Atual + float(gasto))
        escreveGastos(gasto, dia, mes)
        arq.write(gastoT)
        gasto = float(gastoT)
    except:
        gasto_Atual = str(gasto_Atual)
        arq.write(gasto_Atual)
        return 0
    return gasto

def escreveGastos(gasto, dia,mes):
    detalhe = str(input("Detalhamento: "))
    dia = str(dia)
    mes = str(mes)
    arqGastos = open("C:\python projects\Controle-de-Dinheiro\logGastos.txt", "a")
    saida =  dia + "/" + mes + " - " + gasto+ "- " + detalhe  + "\n"
    arqGastos.write(saida)

def mostraGasto(gasto):
    print(gasto)

def mostraMontanteRestante(gasto_Atual, dia, Tetogasto_diario):
    valorRestante = ((30)*Tetogasto_diario) - gasto_Atual

    if(dia < 5):
        if(dia == 4):
            dia = 34
        elif(dia == 3):
            dia = 33
        elif(dia == 2):
            dia = 32
        elif(dia == 5):
            dia = 1
        else:
            dia = 31

    print("Valor a Ser gasto Total = ", valorRestante)
    print("Valor a Ser gasto por Dia = ", valorRestante/(30 - dia+4))
    print("Você tem ", ((dia-4)*Tetogasto_diario) - gasto_Atual  ,"de saldo extra")

def menu():
    dia = time.localtime().tm_mday
    mes = time.localtime().tm_mon
    Tetogasto_diario = 36


    arq = open("C:\python projects\Controle-de-Dinheiro\gastoMensal.txt", "r")
    gasto_Atual = arq.readline()
    gasto_Atual = float(gasto_Atual)
    resp = 1
    while(resp != 0):
        resp = int(input("1 - Resetar Valores\n"
                         "2 - Inserir Gasto\n"
                         "3 - mostrar Restante\n"
                         "4 - mostar Gasto Total\n"))
        if(resp == 1):
            reseta(dia)
        elif(resp == 2):
            arq.close()
            arq = open("C:\python projects\Controle-de-Dinheiro\gastoMensal.txt", "w")
            gasto_Atual = insereGasto(gasto_Atual, arq, dia, mes)
            arq.close()
        elif(resp == 3):
            mostraMontanteRestante(gasto_Atual, dia, Tetogasto_diario)
        elif(resp != 0):
            mostraGasto(gasto_Atual)

menu()