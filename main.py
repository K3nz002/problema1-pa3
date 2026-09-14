# Bibliotecas

fila_espera = []

def cadastrar(cpf, nome, nascimento):
    pass

def buscar_cadastro(cpf):
    pass

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
        if fila_espera[i]["cpf"] == cpf:
            fila_espera.pop(i)
            return True
    return False

def tamanho_final():
    pass

def relatorio_do_dia():
    pass

def main():
    pass

if __name__ == "__main__":
    main()
