import json

def ler_json(nome_arquivo):
    try:
        with open (nome_arquivo, 'r', newline='', encoding='utf-8') as arquivo_json:
            dados = json.load(arquivo_json)
            print(dados)
    except FileNotFoundError:
        print("arquivo não encontrado")

def escrever_json(nome_arquivo, dados):
    try:
        with open (nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_json:
            json.dump(dados, arquivo_json, ensure_ascii=False, indent=4)
            print(f"dados salvos em: {nome_arquivo}")
    except FileNotFoundError:
        print("Erro ao salvar o arquivo")

dados1 = {
    "nome": 'ana',
    "idade": "30",
    "cidade": "São Paulo"
}

if __name__ == "__main__":
    nome_arquivo = input("digite o nome do arquivo JSON: ").strip()
    escrever_json(nome_arquivo, dados1)
    ler_json(nome_arquivo)