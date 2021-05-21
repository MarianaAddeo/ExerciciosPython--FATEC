neg = []
pos = []
cont = 0

while cont <= 0 or cont >50:
    cont = int(input("Digite o a quantidade de números que será lida (Maior que 0, menor que 50): "))

while cont > 0:
    num = float (input("Digite o valor: "))
    if num >= 0:
        pos.append(num)
    else:
        neg.append(num)
    cont = cont - 1

tamPos = len(pos)
print("Positivos: ", pos)
print (tamPos, "elementos")

tamNeg = len(neg)
print("Negativo: ", neg)
print (tamNeg, "elementos")
