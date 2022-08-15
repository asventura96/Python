from cap4_dicionarios_tuplas.funcoes import *

usuarios = {}
opcao = perguntar ()
while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        inserir (usuarios)
    opcao = perguntar ()