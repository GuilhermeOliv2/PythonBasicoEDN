import csv

def escrever_csv(nome_arquivo, dados):
    with open (nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
        escrito = csv.writer(arquivo_csv)
        escrito.writerow(['nome', 'idade', 'cidade'])
        escrito.writerows(dados)
    print (f"dados salvos em {nome_arquivo}")

dados = [
    ['Ana', 28, 'Rio de Janeiro'],
    ['Pedro', 25, 'Salvador'],
    ['Julia', 22, 'Belo Horizonte']
]

if __name__ == "__main__":
    nome_arquivo = input("digite o nome do arquivo CSV: ").strip()
    escrever_csv(nome_arquivo, dados)