#Analice Souto dos Santos
#Mariana Patrícia de Souza


#Escreva um programa que leia um número inteiro que representa a quantidade
#de segundos que foram consumidos para realizar 
#uma determinada tarefa. Em seguida mostre esse tempo na tela no formato:
# x horas , y minutos, z segundos

z = int(input( 'Digite o valor de entrada: '))
y = int(z / 60)
z  -= (y * 60)
x = int(y / 60)
y -= (x * 60))
print('  é {}, {} minutos, {} segundos' .format (x , y, z))

