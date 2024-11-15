frase1 = input()
frase2 = input()
list_palavra1 = frase1.split(" ")
list_palavra2 = frase2.split(" ")
set = set()

for i in list_palavra1:
    if i in list_palavra2:
        set.add(i)

set = str(set)
set = set.replace("{","")
set = set.replace("}","")
set = set.replace("'","")
print(set)