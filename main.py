# Bibliotecas

fila_espera = [] 
atendidos = []
cadastros = []

contador_eventos = 0  # Contador interno de eventos do sistema para o R7
ordem_chegada = 0


def buscar_cadastro(cpf):           # R2: basicamente varre a lista de cadastros, se encontrar uma
    for paciente in cadastros:      # correspondência, ele retorna o nome do paciente
        if paciente[0] == cpf:
            return paciente
    return None


def cadastrar(cpf, nome, nascimento):
    if buscar_cadastro(cpf) is not None:               #Verificando se o CPF já foi cadastrado
        print("O CPF digitado já possui cadastro.")
        return False

    novo_paciente = [cpf, nome, nascimento]        #Cadastra o novo paicente
    cadastros.append(novo_paciente)
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
    
    # Guarda o registo completo do atendimento para o R7
    atendidos.append([cpf, risco, ordem_chegada, tempo_espera])

    ultimo_paciente = fila_espera.pop()
    # Heappop - Remoção da Fila de Prioridade

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
    for i in range(len(fila_espera)):
        if fila_espera[i][0] == cpf:
            fila_espera.pop(i)
            return True
    return "CPF não cadastrado ou não está na fila."


def tamanho_fila():
    return len(fila_espera)


# R7 - Relatório do dia (ordenação por Merge Sort)


def _intercalar(v, aux, inicio, meio, fim):
    # Intercala v[inicio:meio] e v[meio:fim], ambas já ordenadas (decrescente)
    i = inicio
    j = meio
    k = inicio
    while i < meio and j < fim:
        # >= mantém a ordem original nos empates (ordenação estável)
        if v[i][3] >= v[j][3]:
            aux[k] = v[i]
            i += 1
        else:
            aux[k] = v[j]
            j += 1
        k += 1
    while i < meio:
        aux[k] = v[i]
        i += 1
        k += 1
    while j < fim:
        aux[k] = v[j]
        j += 1
        k += 1
    for k in range(inicio, fim):
        v[k] = aux[k]


def _merge_sort_rec(v, aux, inicio, fim):
    if fim - inicio <= 1:
        return
    meio = (inicio + fim) // 2
    _merge_sort_rec(v, aux, inicio, meio)
    _merge_sort_rec(v, aux, meio, fim)
    _intercalar(v, aux, inicio, meio, fim)


def merge_sort_relatorio(lista): 
    aux = [None] * len(lista)
    _merge_sort_rec(lista, aux, 0, len(lista))
    return lista


def relatorio_do_dia():

    if not atendidos:
        print("Nenhum atendimento realizado hoje.")
        return []

    return merge_sort_relatorio(atendidos)

def main():
    pass

if __name__ == "__main__":
    main()
