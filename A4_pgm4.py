# Escreva um programa que contenha duas variáveis A e B inteiras
# que serão lidas do teclado.
# O programa deve exibir na tela quatro resultados:
#  soma A + B,
#  subtração A – B,
#  multiplicação A * B e 
#  divisão real A / B
# Caso o valor fornecido para B seja zero, o cálculo de divisão
#  não deve ocorrer, e o programa deve apresentar uma mensagem
#  a respeito

A = int(input('Digite uma valor para A: '))
B = int(input('Digite uma valor para B: '))
R = A + B
print('Soma = ', R)
R = A - B
print('Subtração = ', R)
R = A * B
print('Multiplicação = ', R)
if B == 0:
    print('Não é possível calcular a divisão, pois B é zero')
else:
    R = A / B
    print('Divisão = ', R)


print('\n\nFim do Programa')
