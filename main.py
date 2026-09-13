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
        fila_espera.append((f"{cpf} | {risco}\n"))

def chamar_proximo( ):
    if not fila_espera:
        return "Fila vazia."
    
    if in fila_espera

def desistir(cpf):
    for i in range(len(fila_espera)):
        if fila_espera[i]["cpf"] == cpf:
            fila_espera.pop(i)
            return True
    return false

def tamanho_final():
    pass

def relatorio_do_dia():
    pass

def main():
    pass

if __name__ == "__main__":
    main()
