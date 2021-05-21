# Enunciado deste programa está no PDF da Aula 4 sobre
# Comando Condicional
# Esta é uma solução para o Ex 2 do final do PDF
# Nesta versão, o caso quando A é maior ou igual a B é
#  tratado com a construção completa do comando if em Python
#  if - elif - else

A = int(input('Digite uma valor inteiro para A: '))
B = int(input('Digite uma valor inteiro para B: '))
if A < B:
    print('O menor é ', A)
elif A > B: # também pode ser assim B < A:
    print('O menor é ', B)
else:
    print('A é igual a B e o valor é', A)

print('\n\nFim do Programa')
