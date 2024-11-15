frase = input()

letras = {}


for letter in frase:
    if letter in letras:
        letras[letter] += 1
    else:
        letras[letter] = 1

letras.pop(' ')

print(letras)