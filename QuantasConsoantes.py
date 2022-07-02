'''Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.'''

nome = input('Digite uma palavra (minúscula) contendo apenas letras\n')
consoante = []
for i in range(len(nome)):
   if nome[i] == 'a' or nome[i]== 'e' or nome[i]== 'i' or nome[i]== 'o' or nome[i]== 'u':
        continue
   else:
       consoante.append(nome[i])

print(f'O número de consoantes encontradas foi: {len(consoante)}\nSão elas : {consoante}')