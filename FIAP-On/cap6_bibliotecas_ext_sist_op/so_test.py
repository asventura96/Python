import platform
import getpass
from datetime import datetime

print("##### MOSTRA AS INFORMAÇÕES DO SISTEMA")
print("Nome da máquina:....................", platform.node())
print("Arquitetura:........................", platform.architecture())
print("SO:.................................", platform.system())
print("Versão SO:..........................", platform.release())
print("Processador:........................", platform.processor())
print("Versão Python:......................", platform.python_version())

print("##### MOSTRA A DATA E HORA ATUAIS")
print(datetime.now())

usuario = getpass.getuser()
senha = getpass.getpass("Digite sua senha:...")

if usuario == "asven" and senha == "andre":
    print("Bem-vindo André Ventura")
else:
    print("Acesso não autorizado")