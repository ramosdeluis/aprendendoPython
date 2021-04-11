import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[31mO site Pudim não está acessível no momento...')
else:
    print('\033[34mO site do Pudim está on-line prati!\033[m')
    print(site.read())