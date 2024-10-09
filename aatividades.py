# ex1
# numero1=float(input('soma de dois numeros \n digite o 1° numero:'))
# numero2=float(input('digite o 2° numero:'))
# print(numero1+numero2)

# ex2
# numero1=float(input('subtração de dois numeros \n digite o 1° numero:'))
# numero2=float(input('digite o 2° numero:'))
# print(numero1-numero2)

# ex3
# numero1=float(input('multiplicação de dois numeros \n digite o 1° numero:'))
# numero2=float(input('digite o 2° numero:'))
# print(numero1*numero2)

# ex4
# numero1=float(input('divisão de dois numeros \n digite o 1° numero:'))
# numero2=float(input('digite o 2° numero:'))
# print(numero1//numero2)

# ex5
# numero1=float(input('resto da divisão de dois numeros \n digite o 1° numero:'))
# numero2=float(input('digite o 2° numero:'))
# print(numero1/numero2)

# ex6
# numero1=float(input('potência \n digite o 1° numero:'))
# numero2=float(input('digite o expoente:'))
# print(numero1**numero2)

# ex7

# numero1=float(input('media de três numeros \n digite o 1° numero:'))
# numero2=float(input('digite o 2° numero:'))
# numero3=float(input('digite o 3° numero:'))
# soma=(numero1+numero2+numero3)
# print(soma/3)

# ex8

# celsius=float(input('celsius para fahrenheit\n digite quantos graus celsius:'))
# fahrenheit=1.8*celsius+32
# print(fahrenheit,'fahrenheit')

# ex9
# reais=float(input('De reais para dólares \n quantos reais deseja transformar em dólares:'))
# corversao=reais*0.18
# print(corversao)

# ex10
# base=float(input('base do triangulo:'))
# altura=float(input('altura do triangulo:'))
# print(base*altura/2)

# ex11
# ladodoquadrado=float(input('perimetro do quadrado \n qual o tamanho do lado do quadrado:'))
# perimetro=ladodoquadrado*4
# print('perímetro',perimetro)

# ex12

# base=float(input("base do triangulo/n insira o 1° numero"))
# altura=float(input("altura do triangulo/n insira o 2° numero"))

# print(base*altura/2)

# ex13
# PI = 3.14
# raio = float(input('Digite o raio do circulo'))

# area = PI*raio**2

# print('A area do circulo é{:.2f}'.format(area))


# ex14
# metros= float(input('Metros? '))
# centimetros= metros*100;

# print (centimetros, 'cm')

# ex15
# horas=float(input('qual a quantidade de horas trabalhadas:'))
# valorporhoras=float(input('valor por hora trabalhada:'))
# salariototal=horas*valorporhoras
# print('o salario é de ',salariototal)

# ex16
# preco_produto = float(input("Digite o preço do produto: R$ "))   
# percentual_desconto = float(input("Digite o percentual de desconto: "))
# valor_desconto = preco_produto * (percentual_desconto / 100)
# preco_final = preco_produto - valor_desconto
   
# print(f"O preço final com desconto é: R$ {preco_final:.2f}")

# ex17
# distancia=float(input("distancia[km]? "))
# tempo=float(input("tempo[hora]? "))

# velocidade_media = float(distancia)/float(tempo)

# print("velocidade_media =%.2kf km/h" % velocidade_media)

# ex18
# idade=float(input('de idade para dias \n digite a sua idade:'))
# dias=365*idade
# print('voce tem',dias,'dias de vida')

# ex19
# dias=float(input('de dias para segundos \n digite a quantidade de dias:'))
# segundos=dias*24*60*60
# print('tem',segundos)

# ex20
# pergunta_nome = input("Qual é o seu nome? " )
# nome = ("Olá" , pergunta_nome)
# idade = input (f"Qual sua idade? ")
# peso = float(input("Qual seu peso (em KG)? "))
# altura = float(input("Qual sua Altura (em metros e usando ponto)? "))

# print("Vamos calcular seu IMC")

# imc = (peso / (altura * altura))

# print(pergunta_nome , (f"seu IMC é: {imc:.2f}"))

# if imc < 16:
# 	print("Seu estado é de Magreza grave\nProcure um médico ou nutricionista.")
# elif imc < 17:
# 	print("Seu estado é de Magreza moderada\nPrecisa rever sua alimentação.")
# elif imc < 18.5:
# 	print("Seu estado é de Magreza leve\nPrecisa rever sua alimentação.")
# elif imc < 25:
# 	print("Você está Saudável.\nParabéns!")
# elif imc < 30:
# 	print("Seu estado é de Sobrepeso\nPrecisa rever sua alimentação.")
# elif imc < 35:
# 	print("Seu estado é de Obesidade Grau I\nProcure um médico ou nutricionista.")
# elif imc < 40:
# 	print("Seu estado é de Obesidade Grau II (severa)\nProcure um médico ou nutricionista.")
# else:
# 	print("Seu estado é de Obesidade Grau III (mórbida)\nProcure um médico ou nutricionista.")

# ex21
# num1 = float(input("Digite o primeiro número: "))
# num2 = float(input("Digite o segundo número: "))
# diferenca_absoluta = abs(num1 - num2)
# print("A diferença absoluta entre os números é:", diferenca_absoluta)
	
# ex22

# dividendo = int(input("Dividendo: "))
# divisor = int(input("Divisor: "))
# quociente = 0
# x = dividendo
# while x >= divisor:
#     x = x - divisor
#     quociente = quociente + 1
# resto = x
# print(f"O resto de {dividendo} / {divisor} é {resto}")

# ex23
# numero=int(input("informe o numero"))
# valor_absoluto= abs(numero)
# print(valor_absoluto)

# ex24

# velocidade_kmh = float(input("Digite a velocidade em km/h: "))
# velocidade_ms = velocidade_kmh / 3.6
# print(f"A velocidade em m/s é: {velocidade_ms:.2f} m/s")

# ex25
# # Função para calcular as raízes
# def calcular_raizes(a, b, c):
#     delta = b**2 - 4*a*c

# # Entrada de dados
# print("Calculadora de raízes da equação do segundo grau (ax² + bx + c = 0)")
# a = float(input("Digite o coeficiente a (diferente de 0): "))
# b = float(input("Digite o coeficiente b: "))
# c = float(input("Digite o coeficiente c: "))

# # Verifica se 'a' é diferente de zero
# if a == 0:
#     print("O coeficiente 'a' deve ser diferente de zero.")
# else:
#     # Chama a função e imprime o resultado
#     resultado = calcular_raizes(a, b, c)
#     print(resultado)

# ex26

# produto1=float(input('valor total da compra \n valor do 1° produto:'))
# produto2=float(input('valor do 2° produto:'))
# produto3=float(input('valor do 3° produto:'))
# print('O valor da compra é',produto1+produto2+produto3)

# ex27
# def converter_dias_para_semanas(dias):
#     semanas = dias // 7  # Calcula o número de semanas
#     dias_restantes = dias % 7  # Calcula os dias restantes
#     return semanas, dias_restantes

# # Solicita a entrada do usuário
# try:
#     dias_input = int(input("Digite o número de dias: "))
    
#     if dias_input < 0:
#         print("Por favor, digite um número de dias positivo.")
#     else:
#         semanas, dias_restantes = converter_dias_para_semanas(dias_input)
#         print(f"{dias_input} dias = {semanas} semanas e {dias_restantes} dias.")
# except ValueError:
#     print("Por favor, insira um número inteiro válido.")


# ex28

# # Solicita o valor da compra
# valor_compra = float(input("Digite o valor da compra: R$ "))

# # Aplica os descontos
# if valor_compra > 500:
#     desconto = 0.10  # 10% de desconto
# elif valor_compra > 100:
#     desconto = 0.05  # 5% de desconto
# else:
#     desconto = 0.0  # Sem desconto

# # Calcula o valor final
# valor_final = valor_compra * (1 - desconto)

# # Exibe o resultado
# print(f"O valor final da compra, após o desconto, é: R$ {valor_final:.2f}")



# ex29
# numero1 = float(input("Digite o primeiro número: "))
# numero2 = float(input("Digite o segundo número: "))

# # Verificar se o segundo número é diferente de zero
# if numero2 != 0:
#     resultado = numero1 / numero2
#     # Mostrar o resultado formatado com duas casas decimais
#     print(f"O resultado da divisão é: {resultado:.2f}")
# else:
#     print("Erro: Não é possível dividir por zero.")