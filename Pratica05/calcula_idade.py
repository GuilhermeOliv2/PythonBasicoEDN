import datetime

def calcula_idade_em_dias (ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365
    return idade_dias

ano_nasc = int (input("digite ano do nascimento: "))
idade_em_dias = calcula_idade_em_dias (ano_nasc)
print (f"sua idade aproximada é: {idade_em_dias} dias")