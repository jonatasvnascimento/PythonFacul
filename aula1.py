nome = 'joao'
idade = 29

print(nome, idade)
nome = input('Digite seu nome: ')
print(nome, idade)

if idade > 20:
    print(idade)
elif idade < 10:
    print(idade-50)

for i in range(0, 10):
    print(i, end="")

print('\n')

cont = 0
while cont < 10:
    cont += 1
    print(cont, end="")


print('\n')

n1 = input('Digite a nota 1: ')
n2 = input('Digite a nota 2: ')

media = (float(n1) + float(n2)) / 2

if media >= 7:
    print('aluno aprovado')
else:
    print('aluno reprovado')
print(media)
