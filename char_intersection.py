frase1 = input()
frase2 = input()
words = ""
list_palavra1 = frase1.split(" ")
list_palavra2 = frase2.split(" ")
set = set()

for i in list_palavra1:
    if i in list_palavra2:
        set.add(i)

for i in set:
    words = words + " " +(i)

print(words.replace(" ", "", 1))