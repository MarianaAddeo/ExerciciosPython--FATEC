

LMin = int(input("Digite o valor inteiro menor: "))
LMax = int(input("Digite o valor inteiro maior: "))
dif = 0
A = []

if LMin > LMax:
    dif = LMin
    LMin = LMax
    LMax = dif

while cont > 0:
    val = float(input("Digite quantas entradas deseja receber: "))
    if val <= LMax and val >= LMin:
        A.append(val)
        cont = cont - 1

print("Os valores válidos digitados formam: ", A)
print("O vetor tem", len(A),"elementos")
