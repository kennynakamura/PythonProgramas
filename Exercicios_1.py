"""
Peça ao usuario para digitar tres valores inteiros
e imprima a soma deles

valor1 = int(input('Qual primeiro valor?'))
valor2 = int(input('Qual segundo valor?'))
valor3 = int(input('Qual terceiro valor?'))
soma = valor1 + valor2 + valor3
print(f'O resultado da soma dos 3 valores é {soma}')

Leia um valor de área em metros quadrados m^2 e
apresente-o convertido em acres.
A = M * 0,000247, sendo M a área em metros quadrados
e A a área em acres

metros = int(input('Qual a area em metros?'))
conversao = metros * 0.000247
print(f'Sao {conversao} acres')

Faça um programa que leia o valor de um produto
e imprima o valor com desconto, tendo em vista
que o desconto foi de 12%

preço = int(input('Qual preço do produto?'))
desconto = preço - (preço * 0.12)
print(f'O preço com desconto é de {desconto}')

Faça um algoritmo que calcule o IMC de uma pessoa
e mostre sua classe de acordo com a tabela
IMC = peso(kg)/altura(m)^2

peso = int(input('Qual seu peso?'))
altura = float(input('Qual sua altura?'))
imc = peso/altura**2
if imc < 18.5:
    print('Abaixo do peso')
elif 18.6 < imc < 24.9:
    print('Saudável')
elif 25 < imc < 29.9:
    print('Peso em excesso')
elif 30 < imc < 34.9:
    print('Obesidade Grau 1')
elif 35 < imc < 39.9:
    print('Obesidade Grau severa')
elif imc > 40:
    print('Obesidade Grau mórbida')
print(f'O seu IMC é de {imc}')

Faça um programa que determine e mostre os cinco primeiros
múltiplos de 3, considerando números maiores que 0.

for num in range(3,16,3):
    print(num)

Faca um programa que calcule e mostre a soma dos 10
primeiros numeros pares

s = 0
for a in range(0, 10, 2):         0, 2, 4, 6, 8.
    if a % 2 == 0:               verifica se o numero é par
        s += a                   caso for soma-se ao s
print('Soma:', s)                apos atingir o numero 10, print
print('FIM')

Dados um número inteiro n, n > 0, e uma sequência com n números inteiros,
determinar quantos números da sequência são pares e quantos são ímpares.

n = int(input("Digite o tam da seq: ")) # atribuição multipla

cont = conta_par = conta_impar = 0
while cont < n:
    num = int(input("Digite um num da seq: "))
    cont = cont + 1
    if num % 2 == 0:  # se num é múltiplo de 2, ou seja, é par
        conta_par = conta_par + 1
    else:
        conta_impar = conta_impar + 1

print(conta_par,   "numeros pares")
print(conta_impar, "numeros impares")

"""
