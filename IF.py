def impar_par():
    num = int(input("Qual número: "))
    if num % 2 == 1:
        print(num, "é impar")
    else:
        print(num,"é par")

def vog_cons():
    letra = input("Qual a letra: ")
    letralist = ["a","e","i","o","u"]
    if letra in letralist:
       print("é uma vogal")
    else:
       print("é uma consoante")

def formas():
    figuras = {3:"triângulo",
               4:"quadrado",
               5:"pentagrama",
               6:"hexágono"}
    forma = int(input("Quantos lados?(max 6): "))
    #if (3 < forma < 6):
    try:
        print(figuras[forma])
    except:
        print("nao tem")

escolha =int(input("1 - par ou impar\n2 - vogal ou consoante\n"
                   "3 - Lados de figuras\nQual programa: "))
if escolha == 1:
    impar_par()
elif escolha == 2:
    vog_cons()
elif escolha ==3:
    formas()
else:
    print("nao tem")





