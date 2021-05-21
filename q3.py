productsList = [
    [16, 14.35, 12.93, 50],
    [23, 35.12, 29.85, 100],
    [27, 19.35, 16.76, 70],
    [34, 63.40, 58.25, 40]
]

# soma dos vendas varejo
sumRetail = 0
# soma dos vendas atacados
sumWholesale = 0
# soma total da venda
sumTotal = 0

#número de vendas realizadas
salesNumber = int(input("Digite o número de vendas realizadas: "))

#valida se o número de vendas é maior que zero
if (salesNumber <= 0 ): 
    print("Error: O número de vendas deve ser maior q zero!")
    exit()

# Função para procurar o produto na lista
def searchProduct(cod):
    searchedProduct = None

    for product in productsList:
        if (product[0] == int(cod)):
            searchedProduct = product
            break

    return searchedProduct

# Função para formatar o decimal para moeda
def formatMoney(value):
    return "R${:,.2f}".format(value)

while (salesNumber > 0 ):
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
    
    salesNumber -= 1


print("Total de vendas do Grupo Varejo: " + formatMoney(sumRetail))
print("Total de vendas do Grupo Atacado: " + formatMoney(sumWholesale))

sumTotal = sumRetail + sumWholesale

print("Vendas Totais: " + formatMoney(sumTotal))