import pandas as pd

def processar_logs_treinamento(arquivo):
    try:
        df = pd.read_csv(arquivo)
        media_tempo = df['tempo_execucao'].mean()
        desvio_padrão_tempo = df['tempo_execucao'].std()
        print(f"a media de execução é: {media_tempo:.2f}")
        print(f"o desvio padrão é: {desvio_padrão_tempo:.2f}")
    except FileNotFoundError:
        print("arquivo não encontrado")
    except Exception as e:
        print(f"erro ao processar: {e}")

nome_arquivo = input("Digite o nome do arquivo de log: ")

processar_logs_treinamento(nome_arquivo)
