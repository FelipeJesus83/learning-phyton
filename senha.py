import hashlib
import requests

senha = input("Digite uma senha: ")

h = hashlib.sha1(senha.encode())
h = h.hexdigest().upper()

r = requests.get(f"https://api.pwnedpasswords.com/range/{h[:5]}")

vezes = 0

for linha in r.text.splitlines():
    fim, qtd = linha.split(":")
    
    if fim == h[5:]:
        vezes = int(qtd)

print(f"Vazou {vezes} vezes")