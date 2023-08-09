import random

custoTotal = 0


n = 20
custoRequisitos = []
requisitos = []
Xi = []
for i in range(0, n):
    Xi.append(1)
    requisitos.append(i)
    custoRequisitos.append(random.randint(1, 5))
    custoTotal += custoRequisitos[i] * Xi[i]



m = 20
importanciaClientes = []
clientes = []
scorei = 0
for i in range(0, m):
    clientes.append(i)
    importanciaClientes.append(random.randint(1, 5))
    for q in range(n):
        scorei += ((random.randint(1, 5)) * importanciaClientes[i])

print(scorei)
print(custoTotal)
