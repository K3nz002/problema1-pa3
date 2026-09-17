# Bibliotecas

fila_espera = []
cadastros = []

def buscar_cadastro(cpf):           # R2: basicamente varre a lista de cadastros, se encontrar uma  
    for paciente in cadastros:      # correspondência, ele retorna o nome do paciente
        if paciente["cpf"] == cpf:
            return paciente
    return None
    
def cadastrar(cpf, nome, nascimento):
    if buscar_cadastro(cpf) is not None:               #Verificando se o CPF já foi cadastrado
        print(f"O CPF digitado já possui cadastro.")
        return False
        
    novo_paciente = {        #Cadastra o novo paicente
        "cpf": cpf,
        "nome": nome,
        "nascimento": nascimento
    }

    cadastros.append(novo_paciente)
    print(f"Cadastro efetuado!")
    return True



def dar_entrada(cpf, risco):
    if not buscar_cadastro(cpf):
        print("Paciente não cadastrado.")
        cadastrar(cpf, nome, nascimento)
    else:
        if risco.lower() == "emergencia":
            risco = 1
        elif risco.lower() == "muito urgente":
            risco = 2
        elif risco.lower() == "urgente":
            risco = 3
        elif risco.lower() == "pouco urgente":
            risco = 4
        elif risco.lower() == "nao urgente":
            risco = 5
        fila_espera.append([cpf, risco])

def chamar_proximo( ):
    if not fila_espera:
        return "Fila vazia."
    
    for i in range(len(fila_espera)):
        if fila_espera[i][1] == 1:
            return "Chamado: " + fila_espera[i][0] + "Risco: Emergência"
            fila_espera.pop(i)
            return True
        elif fila_espera[i][1] == 2:
            return "Chamado: " + fila_espera[i][0] + "Risco: Muito urgente"
            fila_espera.pop(i)
            return True
        elif fila_espera[i][1] == 3:
            return "Chamado: " + fila_espera[i][0] + "Risco: Urgente"
            fila_espera.pop(i)
            return True
        elif fila_espera[i][1] == 4:
            return "Chamado: " + fila_espera[i][0] + "Risco: Pouco urgente"
            fila_espera.pop(i)
            return True
        elif fila_espera[i][1] == 5:
            return "Chamado: " + fila_espera[i][0] + "Risco: Não urgente"
            fila_espera.pop(i)
            return True
        

def desistir(cpf):
    for i in range(len(fila_espera)):
        if fila_espera[i][0] == cpf:
            fila_espera.pop(i)
            return True
    return False

def tamanho_fila():
    return len(fila_espera)

def relatorio_do_dia():
    pass

def main():
    pass

if __name__ == "__main__":
    main()
