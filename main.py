# Bibliotecas

fila_espera = []
atendidos = []
cadastros = []

def buscar_cadastro(cpf):           # R2: basicamente varre a lista de cadastros, se encontrar uma  
    for paciente in cadastros:      # correspondência, ele retorna o nome do paciente
        if paciente[0] == cpf:
            return paciente
    return None

def cadastrar(cpf, nome, nascimento):
    if buscar_cadastro(cpf) is not None:               #Verificando se o CPF já foi cadastrado
        print(f"O CPF digitado já possui cadastro.")
        return False
        
    novo_paciente = [cpf, nome, nascimento]        #Cadastra o novo paicente
    cadastros.append(novo_paciente)
    print(f"Cadastro efetuado!")
    return True

def dar_entrada(cpf, risco):
    if not buscar_cadastro(cpf):
        print("Paciente não cadastrado.")
        return False
    
    for i in range(len(fila_espera)):
        if cpf in fila_espera[i][0]:
            print("Paciente já está na fila.")
            return False

    # A entrada de risco tem que ser em inteiro se não teria muitas variáveis como acentuação e número de espaços
    if risco > 1 and risco < 5:
        fila_espera.append([cpf, risco])
    else:
        print("Risco inválido.")
        return False

def chamar_proximo( ):
    if not fila_espera:
        print("Fila vazia.")
        return False
    
    # Lógica de Triagem
    for nivel in range(1, 6):
        for i in range(len(fila_espera)):
            if fila_espera[i][1] == nivel:
                atendidos.append(fila_espera[i])
                print("Chamado: " + fila_espera[i][0] + "Risco: " + nivel)
                fila_espera.pop(i)
                return True
            break
    return False

def desistir(cpf):
    for i in range(len(fila_espera)):
        if fila_espera[i][0] == cpf:
            fila_espera.pop(i)
            return True
    return "CPF não cadastrado."

def tamanho_fila():
    return len(fila_espera)

def relatorio_do_dia():
    pass

def main():
    pass

if __name__ == "__main__":
    main()
