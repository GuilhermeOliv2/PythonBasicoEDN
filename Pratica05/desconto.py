def calcular_desconto(preco, percentual_desconto):
    desconto = preco * (percentual_desconto/100)
    preco_final = preco - desconto
    return preco_final


preço_original = float(input("digite o preço do produto em reais: "))
desconto = float(input("digite o percentual de descoto: "))

preco_com_desconto = calcular_desconto(preço_original, desconto)
print (f"O preço final com {desconto}% de desconto é: R${preco_com_desconto:.2f}")