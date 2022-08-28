import json

with open("Python\/FIAP-On\/cap5_manip_arq_json\/bd.json", "r") as arq_json:
    dicionario = json.load(arq_json)
    for chave, dados in dicionario.items():
        print(chave + " | " + str(dados))

with open("Python\/FIAP-On\/cap5_manip_arq_json\/bd1.json", "w") as json_file:
    json.dump(dicionario, json_file)