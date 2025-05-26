#Classificador idade

idade = int(input("digite uma idade: "))

if idade >= 60:
    print ("considerado idoso")
elif idade >= 18:
    print ("considerado adulto")
elif idade >= 12:
    print ("considerado adolescente")
elif idade >= 1:
    print ("Considerado criança")
elif idade == 0:
    print ("considerado bebê")
else:
    print ("idade invalida")

print("")
print("--------------")
print("")

#calculadora de IMC

altura = float(input("digite a altura em metros: "))
peso = float(input("digite o peso em quilos, chefe: "))
IMC = peso / altura ** 2

if IMC <= 18.5:
    print (f"Seu IMC é: {IMC:.2f} está abaixo do peso saudavel")
elif IMC <= 24.9:
    print (f"Seu IMC é: {IMC:.2f} está normal. Boa!")
elif IMC <= 29.0:
    print (f"Seu IMC é: {IMC:.2f} está com sobrepeso")
else: 
    print (f"Seu IMC é: {IMC:.2f} já é considerado obesidade")

print("")
print("--------------")
print("")

#conversor de temperatura

temperatura = float(input("digite o valor da temperatura: "))
escolha = int(input ("\n Qual conversão você quer fazer? \n1- C -> F \n2- C -> K \n3- F -> C \n4- F -> K \n5- K -> C \n6- K -> F \n"))
if escolha == 1:
    print (f"{temperatura}°C irão se tornar:")
    temperatura = (temperatura * (9/5)) + 32
    print (f"{temperatura}°F")
elif escolha == 2:
    print (f"{temperatura}°C irão se tornar")
    temperatura = temperatura + 273.15
    print (f"{temperatura:.2f}°K")
elif escolha == 3:
    print (f"{temperatura}°F irão se tornar")
    temperatura = (temperatura-32) * (5/9)
    print (f"{temperatura}°C")
elif escolha == 4:
    print (f"{temperatura}°F irão se tornar")
    temperatura = (temperatura-32) * (5/9) + 273,15
    print (f"{temperatura:.2f}°K")
elif escolha == 5:
    print (f"{temperatura}°K irão se tornar")
    temperatura = temperatura - 273,15
    print (f"{temperatura}°C")
elif temperatura == 6:
    print (f"{temperatura}°K irão se tornar")
    temperatura = (temperatura - 273,15) * (9/5) + 32
    print (f"{temperatura}°F")
else:
    print("opção invalida.")

#calculadora de ano bissexto 

ano = int (input("digite um ano: "))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print ("ano bissexto")
        else:
            print ("ano não bissexto")
    else: 
        print ("ano bissexto")
else:
    print ("ano não bissexto")