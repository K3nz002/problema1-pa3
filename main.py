# Bibliotecas

fila_espera = [] 
atendidos = []
cadastros = []

contador_eventos = 0  # Contador interno de eventos do sistema para o R7



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
    global contador_eventos

    if not buscar_cadastro(cpf):
        print("Paciente não cadastrado.")
        return False

    for i in range(len(fila_espera)):
        if cpf == fila_espera[i][0]:
            print("Paciente já está na fila.")
            return False

    # A entrada de risco tem que ser em inteiro se não teria muitas variáveis como acentuação e número de espaços
    if risco >= 1 and risco <= 5:
        contador_eventos += 1
        # Guarda [cpf, risco, evento_entrada]
        fila_espera.append([cpf, risco, contador_eventos])
        print(f"Paciente com CPF {cpf} entrou na fila com Risco {risco}.")
        return True
    else:
        print("Risco inválido.")
        return False


def chamar_proximo():
    global contador_eventos

    if not fila_espera:
        print("Fila vazia.")
        return False

    # Lógica de Triagem
    for nivel in range(1, 6):
        for i in range(len(fila_espera)):
            if fila_espera[i][1] == nivel:
                contador_eventos += 1
                cpf = fila_espera[i][0]
                risco = fila_espera[i][1]
                evento_entrada = fila_espera[i][2]

                # Cálculo do tempo de espera em número de eventos
                tempo_espera = contador_eventos - evento_entrada

                # Guarda o registo completo do atendimento para o R7
                atendidos.append([cpf, risco, evento_entrada, contador_eventos, tempo_espera])
                fila_espera.pop(i)
                print(f"Chamado: {cpf} | Risco: {nivel} | Tempo de Espera: {tempo_espera} eventos")
                return True
            break
    return False


def desistir(cpf):
    for i in range(len(fila_espera)):
        if fila_espera[i][0] == cpf:
            fila_espera.pop(i)
            return True
    return "CPF não cadastrado ou não está na fila."


def tamanho_fila():
    return len(fila_espera)


def relatorio_do_dia():

    if not atendidos:
        print("Nenhum atendimento realizado hoje.")
        return []

    # Cópia manual da lista de atendidos
    relatorio = []
    for item in atendidos:
        relatorio.append(item)

    # Insertion Sort — Ordenação Decrescente pelo tempo de espera (índice 4)
    n = len(relatorio)
    for i in range(1, n):
        chave = relatorio[i]
        j = i - 1
        while j >= 0 and relatorio[j][4] < chave[4]:
            relatorio[j + 1] = relatorio[j]
            j -= 1
            
        relatorio[j + 1] = chave
        print(f"Paciente{j}")

    print("\n--- RELATÓRIO DO DIA (Ordenado por Tempo de Espera) ---")
    for item in relatorio:
        print(f"CPF: {item[0]} | Nome: {item[1]} | Espera: {item[4]:.2f}s")
    
    return relatorio

def main():
    pass

if __name__ == "__main__":
    main()
