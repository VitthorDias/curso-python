from termcolor import cprint
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    cprint("O site não está funcionando.", 'red')
else:
    cprint('Eu consegui acessar o site.', 'green')
