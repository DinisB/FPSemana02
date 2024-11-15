frase1 = input()
frase2 = input()
words = ""
list_palavra1 = frase1.split(" ")
list_palavra2 = frase2.split(" ")
list = set()

for i in list_palavra1:
    if i in list_palavra2:
        list.add(i)

for i in list:
    words = words + " " +(i)

print(words.replace(" ", "", 1))