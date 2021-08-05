##Importar módulo ou biblioteca OS
#(Integra os programas e recursos do S. O.)
import os

##Imprime #60 vezes
print("#" * 60)

##Criar uma variável que vai receber do usuário o IP
#-n -num de pacotes que serão 6 {}
ip_ou_host = input("Digite o IP ou Host a ser verificado: ")

##Imprime "-" 60vezes
print("-" * 60)

##Chamar system da Biblioteca OS - comando ping
os.system('ping -n 6 {}'.format(ip_ou_host))

##Imprime "-" 60vezes
print("-" * 60)
