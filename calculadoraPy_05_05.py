#conversor de moeda

valor_em_real = 100
taxa_dolar = 5.2
taxa_euro = 6.15

valor_em_dolar = valor_em_real / taxa_dolar
valor_em_euro = valor_em_real / taxa_euro

print ("o valor de 100 reais em dolar fica", round(valor_em_dolar, 2), "e em euro fica", round (valor_em_euro, 2))
print ("")

#Calculadora de desconto
produto = "Camisa"
preço_original = 50
porcentagem_desconto = preço_original * 0.2
preco_final = preço_original - porcentagem_desconto

print ("produto =", produto)
print (f"preço = R$ {preço_original:.2f}")
print ("porcentagem do desconto = 20%")
print (f"valor do desconto = 20% de R$ {preço_original:.2f} = R$ {porcentagem_desconto:.2f}")
print (f"R$ {preço_original:.2f} - R$ {porcentagem_desconto:.2f}, = R$ {preco_final:.2f}")
print (f"preço final = R$ {preco_final:.2f}")
print("")

#calculadora de media escolar
nota1 = 7.5
nota2 = 8
nota3 = 6.5
media = (nota1 + nota2 + nota3)/3 

print (f"As notas do aluno foram = {nota1} + {nota2} + {nota3} \nSomando tudo temos {media*3} \nDivindo por 3 = {media:.2f} \nPortanto a media do aluno é de {media:.2f}")
print ("")

#calculadora de consumo de combustivel

distancia_percorrida = 300
combustivel_gasto = 25
consumo_medio = distancia_percorrida/combustivel_gasto

print(f"\n O carro percorreu {distancia_percorrida} km e gastou {combustivel_gasto} litros de gasosa, logo seu consumo medio é de {consumo_medio:.2f}km/l.")