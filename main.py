import time


def reseta(dia):
    arq = open("gastoMensal.txt", "w")
    arq.write("000.00")

def insereGasto(gasto_Atual, arq):
    gasto = float(input("Valor do Gasto = "))
    gasto = gasto_Atual + gasto
    gasto = str(gasto)
    arq.write(gasto)
    gasto = float(gasto)
    return gasto

def mostraGasto(gasto):
    print(gasto)

def mostraMontanteRestante(gasto_Atual, dia, Tetogasto_diario):
    valorRestante = ((30)*Tetogasto_diario) - gasto_Atual
    if(dia < 5):
        if(dia == 4):
            dia = 26
        elif(dia == 3):
            dia = 25
        elif(dia == 2):
            dia = 24
        else:
            dia = 23

    print("Valor a Ser gasto Total = ", valorRestante)
    print("Valor a Ser gasto por Dia = ", valorRestante/(30 - dia+4))
    print("Você tem ", ((dia-4)*21) - gasto_Atual  ,"de saldo extra")

def menu():
    dia = time.localtime().tm_mday
    Tetogasto_diario = 21
    arq = open("gastoMensal.txt", "r")
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
            arq = open("gastoMensal.txt", "w")
            gasto_Atual = insereGasto(gasto_Atual, arq)
            arq.close()
        elif(resp == 3):
            mostraMontanteRestante(gasto_Atual, dia, Tetogasto_diario)
        else:
            mostraGasto(gasto_Atual)

menu()