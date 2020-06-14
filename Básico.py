#Area em quadrado

vertical = float(input("Entre com X: "))
horizontal = float(input("Entre com y: "))
area = vertical * horizontal
print("A área é de",area,"metros")

#Desconto no Produto

preço = float(input("Qual o preço do produto: "))
desconto = float(input("Qual o desconto em %: "))
final = preço - (preço*(desconto*0.01))
# %.2f faz para limitar o numero de casas decimais em 2
print("O preço final é R$%.2f" % final)

#ordenando 3 numeros

a = int(input("Primeiro numero: "))
b = int(input("Segundo numero: "))
c = int(input("Terceiro numero: "))
mn = min(a,b,c)
mx = max(a,b,c)
md = a + b + c - mn - mx
print("os numeros são em ordem:")
print(" ",mn,md,mx)

#preço do pao velho

pao = .50
des = 0.01
nume = int(input("Numero de paes: "))
tot = nume * pao
destot = tot * des
total = tot - destot
print("Preço: %5.2f" %nume)
print("Desconto: %5.2f" %destot)
print("Preço: %5.2f" %total)
# %5.2f  o 5 serve para espaçar

#