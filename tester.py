import csv
import time
import os

from main import buscar_cadastro, cadastrar, dar_entrada, chamar_proximo, desistir, tamanho_fila

def carregar_CSV(caminho_csv):
    operacoes = []
    with open(caminho_csv, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for linha in reader:
            operacoes.append(linha)
    return operacoes

if __name__ == "__main__":
    pasta_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_csv = os.path.join(pasta_atual, "carga_10k.csv")
  if os.path.exists(caminho_csv):
        print(f"Carregando {caminho_csv}...")
        operacoes = carregar_CSV(caminho_csv)
        executar_e_gerar_logs(operacoes)
  else:
      print(f"Arquivo não encontrado: {caminho_csv}")
