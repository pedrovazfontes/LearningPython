#Operadores Aritméticos

#Desafio 4

"""
Faça um script python que leia algo e mostre os possíveis dados
"""

thing = input("Digite algo: ")
print(thing.isnumeric())
print(thing.isalnum())
print(thing.isdecimal())
print(thing.isupper())

print("#"*20)


#Desafio 5

"""
Faça um programa que leia um numero inteiro e mostre na tela o seu sucessos e antecessor
"""

num1 = int(input("Digite um número inteiro: "))
print(f"O antecessor do nº {num1} é igual a {num1 - 1} e seu sucessor é {num1 +1}")


print("#"*20)

#Desafio 6

"""
Crie um algoritmo  que leia um numero e mostre o seu dobro, triplo e raiz quadrada
"""

num2 = int(input("Digite um número inteiro: "))
print(f"O dobro do nº {num2} é {num2 *2}, triplo {num2 * 3} e sua raiz quadrada é {(num2 * num2) / num2}")

print("#"*20)

#Desafio 7

"""
Desenolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
"""

nota1 = float(input("Digita a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2
print("A media do aluno é equivalente a {:.2}".format(media))

#Desafio 8

""""
Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
"""

value = float(input("Informe o tamnho da parede em metros: "))
print(f" A parede possui {value} metro(s)m, em centimetros possui {value * 1000} e em milimetros {value * 10000}")

#Desafio 9

"""
Faça um programa que leia um número qualquer e mostre sua tabuada
"""

#Podemos fazer com vários prints(f"{n1} x 0 = {n1 * 0}") .... bem como por laço de repetição no caso o for

num3 = int(input("Digite o nº da tabuada que quer obter: "))
for i in range(0,11):
    print(f"{num3} x {i} = {num3 * i}")


#Desafio 10

"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos doláres
ela pode comprar
"""

money = float(input("Quantos reais você possui na carteira?: "))
print("Com {:.2f} reais você pode comprar {:.2f} dolares".format(money ,  money / 5.73))

#Desafio 11

""""
Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua area e a quantidade de tintas
necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m^2

"""

larg = float(input("Digite a largura da parede: "))
alt = float(input("Digire a altura da parede: "))
area = larg * alt
tinta = area / 2
print("Para pintar a parede será necessário {:.2f} litros de tinta".format(tinta))

#Desafio 12

"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
"""

prod = float(input("Digite o valor do produto: "))
desc = prod * (5 / 100)
print("O produto com 5% de desconto é igual a {:.2f} ".format(prod - desc))


#Desafio 13

""""
Faça um programa que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento
"""

salario = float(input("Digite o valor do sario atual: "))
aumento = salario * (15 /100)
print("O seu novo salário equivale a {:.2f}".format(salario + aumento))


#Desafio 14

"""
Escreva um programa que converta uma temperatura digitada em Cº e converta em Fº
"""

tempc = float(input("Por gentileza informa a temperatura em graus celsius: "))
tempf = tempc * 1.8 + 32
print(f"Fazendo a conversão de {tempc}graus celsius para Fahrenheit equivale a {tempf}")

#Desafio 15

"""
Escreve um programa que pergunte a quantidade de km rodados por um carro alugado e a quantidade de dias
pelos quais ele foi alugado. Cacule o preco a pagar, sabendo que o carro custa 60 por dia e 0,15 por km
rodado.
"""

print("Ola sem bem-vindo a LocaAuto")
days = int(input("Informe a quantidade de dias que ficou com o carro: "))
km = float(input("Quantos km você rodou? "))
price = ((days * 60)) + (km * 0.15)
print("O total a pagar é R${price} reais")


# https://youtu.be/Vw6gLypRKmY?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6