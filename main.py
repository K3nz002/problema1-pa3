# Bibliotecas

fila_espera = [] 
atendidos = []


TAMANHO_TABELA = 200003
tabela_hash = [None] * TAMANHO_TABELA
total_cadastrados = 0

contador_eventos = 0  # Contador interno de eventos do sistema para o R7
ordem_chegada = 0



# R1 e R2: Tabela Hash


def _funcao_hash(cpf):
    """Calcula o índice base através do resto da divisão do CPF."""
    cpf_limpo = "".join(filter(str.isdigit, str(cpf)))
    if not cpf_limpo:
        return 0
    return int(cpf_limpo) % TAMANHO_TABELA


def buscar_cadastro(cpf):           # R2: Busca O(1) na Tabela Hash com Sondagem Linear
    pos = _funcao_hash(cpf)
    inicio_pos = pos

    while tabela_hash[pos] is not None:
        if tabela_hash[pos][0] == cpf:
            return tabela_hash[pos]  # Retorna [cpf, nome, nascimento]

        # Sondagem Linear 
        pos = (pos + 1) % TAMANHO_TABELA

        if pos == inicio_pos:
            break

    return None


def cadastrar(cpf, nome, nascimento):  # R1: Cadastro O(1) na Tabela Hash
    global total_cadastrados

    if buscar_cadastro(cpf) is not None:               # Verificando se o CPF já foi cadastrado
        print("O CPF digitado já possui cadastro.")
        return False

    if total_cadastrados >= TAMANHO_TABELA:
        print("Erro: Tabela Hash cheia.")
        return False

    pos = _funcao_hash(cpf)

    # Procura a primeira posição livre (None)
    while tabela_hash[pos] is not None:
        pos = (pos + 1) % TAMANHO_TABELA

    tabela_hash[pos] = [cpf, nome, nascimento]
    total_cadastrados += 1
    print("Cadastro efetuado!")
    return True


def dar_entrada(cpf, risco):
    global contador_eventos, ordem_chegada

    if not buscar_cadastro(cpf):
        print("Paciente não cadastrado.")
        return False

    for i in range(len(fila_espera)):
        if cpf == fila_espera[i][0]:
            print("Paciente já está na fila.")
            return False

    # A entrada de risco tem que ser em inteiro se não teria muitas variáveis como acentuação e número de espaços
    if 1 <= risco <= 5:
        contador_eventos += 1
        ordem_chegada += 1

        # Guarda [cpf, risco, ordem_chegada, evento_entrada]
        fila_espera.append([cpf, risco, ordem_chegada, contador_eventos])

        print(f"Paciente com CPF {cpf} entrou na fila com Risco {risco}.")

        # Heappush - Inserção na Fila de Prioridade

        i = len(fila_espera)-1
        pai = (i-1)//2
        while i > 0 and (fila_espera[i][1] > fila_espera[pai][1] or (fila_espera[i][1] == fila_espera[pai][1] and fila_espera[i][2] < fila_espera[pai][2])):
            fila_espera[i], fila_espera[pai] = fila_espera[pai], fila_espera[i]
            i = pai
            pai = (i-1)//2
        return True
    else:
        print("Risco inválido.")
        return False


def chamar_proximo():
    global contador_eventos

    if not fila_espera:
        print("Fila vazia.")
        return False
                    
    contador_eventos += 1

    cpf = fila_espera[0][0]
    risco = fila_espera[0][1]
    ordem_chegada = fila_espera[0][2]
    evento_entrada = fila_espera[0][3]

    # Cálculo do tempo de espera em número de eventos
    tempo_espera = contador_eventos - evento_entrada

    print(f"Chamado: {cpf} | Risco: {risco} | Tempo de Espera: {tempo_espera} eventos")
    # Guarda o registro completo do atendimento para o R7
    atendidos.append([cpf, risco, ordem_chegada, tempo_espera])

    # Heappop - Remoção da Fila de Prioridade
    ultimo_paciente = fila_espera.pop()

    if fila_espera:
        fila_espera[0] = ultimo_paciente
        i = 0
        n = len(fila_espera)

        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            maior = i

            if left < n:
                risco_left, ordem_left = fila_espera[left][1], fila_espera[left][2]
                risco_maior, ordem_maior = fila_espera[maior][1], fila_espera[maior][2]
                
                if risco_left > risco_maior or (risco_left == risco_maior and ordem_left < ordem_maior):
                    maior = left

            if right < n:
                risco_right, ordem_right = fila_espera[right][1], fila_espera[right][2]
                risco_maior, ordem_maior = fila_espera[maior][1], fila_espera[maior][2]
                
                if risco_right > risco_maior or (risco_right == risco_maior and ordem_right < ordem_maior):
                    maior = right
            if maior != i:
                fila_espera[i], fila_espera[maior] = fila_espera[maior], fila_espera[i]
                i = maior
            else:
                break
    return True


def desistir(cpf):

    indice = -1
    for i in range(len(fila_espera)):
        if fila_espera[i][0] == cpf:
            indice = i
            break
    if indice == -1:
        print("CPF não cadastrado ou não está na fila.")
        return False
    if indice == len(fila_espera) - 1:
        fila_espera.pop()
        print(f"Paciente com CPF {cpf} desistiu e foi removido.")
        return True
    ultimo = fila_espera.pop()
    fila_espera[indice] = ultimo
    _reorganizar_heap_no_indice(indice)

    print(f"Paciente com CPF {cpf} desistiu e foi removido.")
    return True


def _reorganizar_heap_no_indice(i):
    n = len(fila_espera)
    
    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        maior = i
        if left < n:
            risco_left, ordem_left = fila_espera[left][1], fila_espera[left][2]
            risco_maior, ordem_maior = fila_espera[maior][1], fila_espera[maior][2]
            if risco_left > risco_maior or (risco_left == risco_maior and ordem_left < ordem_maior):
                maior = left
        if right < n:
            risco_right, ordem_right = fila_espera[right][1], fila_espera[right][2]
            risco_maior, ordem_maior = fila_espera[maior][1], fila_espera[maior][2]
            if risco_right > risco_maior or (risco_right == risco_maior and ordem_right < ordem_maior):
                maior = right
        if maior != i:
            fila_espera[i], fila_espera[maior] = fila_espera[maior], fila_espera[i]
            i = maior
        else:
            break
            
    while i > 0:
        pai = (i - 1) // 2
        risco_i, ordem_i = fila_espera[i][1], fila_espera[i][2]
        risco_pai, ordem_pai = fila_espera[pai][1], fila_espera[pai][2]
        if risco_i > risco_pai or (risco_i == risco_pai and ordem_i < ordem_pai):
            fila_espera[i], fila_espera[pai] = fila_espera[pai], fila_espera[i]
            i = pai
        else:
            break


def tamanho_fila():
    return len(fila_espera)


def relatorio_do_dia():

    if not atendidos:
        print("Nenhum atendimento realizado hoje.")
        return []

    # Insertion Sort — Ordenação Decrescente pelo tempo de espera (índice 3)
    n = len(atendidos)
    for i in range(1, n):
        chave = atendidos[i]
        j = i - 1
        while j >= 0 and atendidos[j][3] < chave[3]:
            atendidos[j + 1] = atendidos[j]
            j -= 1
            
        atendidos[j + 1] = chave
    return atendidos


def main():
    pass


if __name__ == "__main__":
    main()
