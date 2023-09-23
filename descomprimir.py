import os
import sys
import time
class color:
    morado = '\033[95m'
    blanco = '\033[97m'
    cyan = '\033[96m'
    azul  = '\033[94m'
    verde = '\033[92m'
    amarillo = '\033[93m'
    rojo = '\033[91m'
    fin = '\033[0m'

def banner():
 os.system("clear")
 print(f"""{color.cyan}
██████╗ ██╗ █████╗ ████████╗███╗   ███╗██╗   ██╗██╗  ██╗
██╔══██╗██║██╔══██╗╚══██╔══╝████╗ ████║██║   ██║╚██╗██╔╝
██║  ██║██║██║  ╚═╝   ██║   ██╔████╔██║██║   ██║ ╚███╔╝
██║  ██║██║██║  ██╗   ██║   ██║╚██╔╝██║██║   ██║ ██╔██╗
██████╔╝██║╚█████╔╝   ██║   ██║ ╚═╝ ██║╚██████╔╝██╔╝╚██╗
╚═════╝ ╚═╝ ╚════╝    ╚═╝   ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝{color.fin}""")


def version():
 texto =f"""{color.morado}
 |=======================================================|
 | Script by              : #FENRIR-00                   |
 | Version                : Version  2.2                 |
 | Follow me on Github    : https://github.com/Fenrir-00 |
 | Contact me on Telegram : @Ritorito1990                |
 ========================================================= """ 
 print(texto)
banner()
version()

print(f"{color.verde}")
palabra = "DESCOMPRIMIENDO........"
time.sleep(0.5)
for letra in palabra:
 sys.stdout.write(letra)
 sys.stdout.flush()
 time.sleep(0.5)
print(f"{color.fin}")

lista = ["apache-user-enum-1.0.txt.gz","apache-user-enum-2.0.txt.gz","big.txt.gz","catala.txt.gz","common.txt.gz","directory-list-1.0.txt.gz","directory-list-2.3-medium.txt.gz","directory-list-2.3-small.txt.gz","directory-list-lowercase-2.3-medium.txt.gz","directory-list-lowercase-2.3-small.txt.gz","euskera.txt.gz","extensions_common.txt.gz","indexes.txt.gz","mutations_common.txt.gz","small.txt.gz","spanish.txt.gz"]
for i in lista:
 os.system(f'gunzip {i}')
print(f"{color.azul}[✓] DESCOMPRESION FINALIZADA")
print(f"{color.verde}")
palabra = "DESCARGANDO ROCKYOU.TXT"
time.sleep(0.5)
for letra in palabra:
 sys.stdout.write(letra)
 sys.stdout.flush()
 time.sleep(0.5)
print(f"{color.fin}")
os.system("wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt")
banner()
version()
print(f"{color.azul}[✓] DESCOMPRESION FINALIZADA")
print(f"{color.azul}[✓] DESCARGA  FINALIZADA")
os.system("rm descomprimir.py")
