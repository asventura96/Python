nome=input ("Digite o nome: ")
idade=int (input ("Digite a idade: "))
doenca_infectocontagiosa=input ("Suspeita de doença infectocontagiosa? ").upper()
if idade>=65:
    print ("O paciente " + nome + " POSSUI atendimento prioritário.")
elif doenca_infectocontagiosa=="SIM":
    print ("O paciente " + nome + " deve ser direcionado para a sala de espera reservada.")
else:
    print ("O paciente " + nome + " NÃO possui atendimento prioritário e pode aguardar na sala de espera comum.")