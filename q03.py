#Analice Souto dos Santos
#Mariana Patrícia de Souza

#Exercicio03

productsList = [
    [16, 14.35, 12.93, 50],
    [23, 35.12, 29.85, 100],
    [27, 19.35, 16.76, 70],
    [34, 63.40, 58.25, 40]
]


sumRetail = 0
sumWholesale = 0
sumTotal = 0


nv = int(input("Digite o número de vendas realizadas: "))

if (nv <= 0 ): 
    print("Error: O número de vendas deve ser maior q zero!")
    exit()


def searchProduct(cod):
    searchedProduct = None

    for product in productsList:
        if (product[0] == int(cod)):
            searchedProduct = product
            break

    return searchedProduct


def formatMoney(value):
    return "R${:,.2f}".format(value)

while (nv > 0 ):
    inputSale = input("Digite o código do produto e a Quantidade da Venda: ")
    splitSale = inputSale.split(" ")
    codProduct = int(splitSale[0])
    quantityProduct = int(splitSale[1])
    
    product = searchProduct(codProduct)
    
    if(product is None):
        print("código inválido")
        continue
    
    if(quantityProduct > product[3]):
        sumWholesale += (product[2] * quantityProduct)
    else:
        sumRetail += (product[1] * quantityProduct)
    
    nv -= 1


print("Total de vendas do Grupo Varejo: " + formatMoney(sumRetail))
print("Total de vendas do Grupo Atacado: " + formatMoney(sumWholesale))

sumTotal = sumRetail + sumWholesale

print("Vendas Totais: " + formatMoney(sumTotal))
