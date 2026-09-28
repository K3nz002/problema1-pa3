import csv
import random

def gerar_cpf_falso(index):
    return f"{index:011d}"

def gerar_carga_csv(nome_arquivo="carga_10k.csv", qtd_linhas=10000):
    cpfs_cadastrados = []
    cpfs_na_fila = []
    
    nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena"]
    sobrenomes = ["Silva", "Santos", "Oliveira", "Souza", "Lima", "Ferreira", "Costa", "Rodrigues"]

    with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        for i in range(1, 101):
            cpf = gerar_cpf_falso(i)
            nome = f"{random.choice(nomes)} {random.choice(sobrenomes)}"
            data_nasc = f"{random.randint(1970, 2005)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
            writer.writerow(["CADASTRAR", cpf, nome, data_nasc])
            cpfs_cadastrados.append(cpf)

        for i in range(101, qtd_linhas + 1):
            opcao = random.choices(
                ["CADASTRAR", "BUSCAR", "ENTRADA", "CHAMAR", "DESISTIR", "TAMANHO", "RELATORIO"],
                weights=[25, 20, 25, 15, 5, 5, 5],
                k=1
            )[0]

            if opcao == "CADASTRAR":
                cpf = gerar_cpf_falso(i)
                nome = f"{random.choice(nomes)} {random.choice(sobrenomes)}"
                data_nasc = f"{random.randint(1970, 2005)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
                writer.writerow(["CADASTRAR", cpf, nome, data_nasc])
                cpfs_cadastrados.append(cpf)

            elif opcao == "BUSCAR":
                cpf = random.choice(cpfs_cadastrados) if cpfs_cadastrados else gerar_cpf_falso(1)
                writer.writerow(["BUSCAR", cpf])

            elif opcao == "ENTRADA":
                cpf = random.choice(cpfs_cadastrados) if cpfs_cadastrados else gerar_cpf_falso(1)
                prioridade = random.randint(1, 3)  # Ex: 1-Normal, 2-Prioritário, 3-Urgente
                writer.writerow(["ENTRADA", cpf, prioridade])
                cpfs_na_fila.append(cpf)

            elif opcao == "CHAMAR":
                writer.writerow(["CHAMAR"])
                if cpfs_na_fila:
                    cpfs_na_fila.pop(0)

            elif opcao == "DESISTIR":
                if cpfs_na_fila:
                    cpf = cpfs_na_fila.pop(random.randint(0, len(cpfs_na_fila) - 1))
                else:
                    cpf = random.choice(cpfs_cadastrados) if cpfs_cadastrados else gerar_cpf_falso(1)
                writer.writerow(["DESISTIR", cpf])

            elif opcao == "TAMANHO":
                writer.writerow(["TAMANHO"])

            elif opcao == "RELATORIO":
                writer.writerow(["RELATORIO"])

    print(f"Arquivo '{nome_arquivo}' com {qtd_linhas} linhas gerado com sucesso!")

if __name__ == "__main__":
    gerar_carga_csv()