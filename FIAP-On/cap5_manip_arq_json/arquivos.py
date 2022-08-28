base_dados = []

with open("Python\/FIAP-On\/cap5_manip_arq_json\/iris.data", "r") as arquivo:
    for registro in arquivo.readlines():
        base_dados.append(registro.split(","))

print(base_dados)

print(base_dados[0] [0])