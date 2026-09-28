import csv
import time
import os

from main import buscar_cadastro, cadastrar, dar_entrada, chamar_proximo, desistir, tamanho_fila, relatorio_do_dia

def carregar_CSV(caminho_csv):
    operacoes = []
    with open(caminho_csv, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for linha in reader:
            operacoes.append(linha)
    return operacoes

def salvar_relatorio_csv(relatorio, caminho_saida="relatorio_atendimentos.csv"):

    with open(caminho_saida, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        writer.writerow(["CPF", "Prioridade", "Tempo_Espera"])
        
        for item in relatorio:
            if isinstance(item, (list, tuple)):
                writer.writerow(item)
            else:
                writer.writerow([item])
                
    print(f"Lista do relatório salva com sucesso em: {caminho_saida}")

def executar_e_gerar_logs(operacoes):
    
    metricas = {
        "CADASTRAR": [0.0, 0],
        "BUSCAR": [0.0, 0],
        "ENTRADA": [0.0, 0],
        "CHAMAR": [0.0, 0],
        "DESISTIR": [0.0, 0],
        "TAMANHO": [0.0, 0],
        "RELATORIO": [0.0, 0],
    }

    lista_relatorio_final = []

    inicio_geral = time.perf_counter()

    for op in operacoes:
        comando = op[0]
        
        inicio_op = time.perf_counter()

        if comando == "CADASTRAR":
            cadastrar(op[1], op[2], op[3])
        elif comando == "BUSCAR":
            buscar_cadastro(op[1])
        elif comando == "ENTRADA":
            dar_entrada(op[1], int(op[2]))
        elif comando == "CHAMAR":
            chamar_proximo()
        elif comando == "DESISTIR":
            desistir(op[1])
        elif comando == "TAMANHO":
            tamanho_fila()
        elif comando == "RELATORIO":
            lista_relatorio_final = relatorio_do_dia()

        fim_op = time.perf_counter()
        duracao = fim_op - inicio_op

        if comando in metricas:
            metricas[comando][0] += duracao
            metricas[comando][1] += 1

    fim_geral = time.perf_counter()
    tempo_total_geral = fim_geral - inicio_geral

  
    exibir_log_desempenho(metricas, tempo_total_geral, len(operacoes))


    pasta_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_relatorio = os.path.join(pasta_atual, "relatorio_atendimentos.csv")
    salvar_relatorio_csv(lista_relatorio_final, caminho_relatorio)

def exibir_log_desempenho(metricas, tempo_total_geral, qtd_operacoes):
    print("\n" + "=" * 65)
    print(f" LOG DE DESEMPENHO - TOTAL DE OPERAÇÕES: {qtd_operacoes}")
    print("=" * 65)
    print(f"{'Operação':<12} | {'Chamadas':<10} | {'Tempo Total (s)':<16} | {'Média/Op (s)':<15}")
    print("-" * 65)

    for op_nome, (tempo_total, qtd) in metricas.items():
        if qtd > 0:
            media = tempo_total / qtd
            print(f"{op_nome:<12} | {qtd:<10} | {tempo_total:<16.6f} | {media:<15.8f}")
        else:
            print(f"{op_nome:<12} | {qtd:<10} | {0.0:<16.6f} | {0.0:<15.8f}")

    print("-" * 65)
    print(f"Tempo Total de Execução da Bateria: {tempo_total_geral:.4f} segundos")
    print("=" * 65 + "\n")

if __name__ == "__main__":
    pasta_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_csv = os.path.join(pasta_atual, "carga_100k.csv")

    if os.path.exists(caminho_csv):
        print(f"Carregando {caminho_csv}...")
        operacoes = carregar_CSV(caminho_csv)
        executar_e_gerar_logs(operacoes)
    else:
        print(f"Arquivo não encontrado: {caminho_csv}")