frase = input()

letras = {}


for letter in frase:
    if letter in letras:
        letras[letter] += 1
    else:
        letras[letter] = 1

if ' ' in letras:
    letras.pop(' ')

print(letras)