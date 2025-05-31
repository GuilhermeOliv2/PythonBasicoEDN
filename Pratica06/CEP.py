import requests

def consulta_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        if "erro" in dados:
            return "cep não encontrado"
        return f"""
        CEP: {dados['cep']}
        Logradouro: {dados['logradouro']}
        Bairro: {dados['bairro']}
        Cidade: {dados['localidade']}
        Estado: {dados['uf']}
        """
    except requests.RequestException as e:
        return f"erro na consulta: {e}"
def main():
    cep = input("digite um cep valido para consulta (apenas números): ")
    print ("Consultando seu CEP")
    resultado = consulta_cep(cep)
    print (resultado)

if __name__ == "__main__":
    main()