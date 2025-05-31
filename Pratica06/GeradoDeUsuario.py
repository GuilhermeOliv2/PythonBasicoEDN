import requests

def obter_usuario_aleatorio():
    url="https://randomuser.me/api"

    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()['results'][0]
        nome = f"{dados['name']['first']} {dados['name']['last']}"
        email = dados['email']
        pais = dados['location']['country']
        return f"nome: {nome} \nemail: {email} \npaís: {pais}"
    except requests.RequestException as e:
        return f"erro ao obter usuario aleatorio: {e}"
    
def main():
    print("gerando usuario...")
    usuario = obter_usuario_aleatorio()
    print (usuario)

if __name__ == "__main__":
    main()
