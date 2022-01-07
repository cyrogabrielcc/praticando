import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(x):

    if x in data:
        return data[x]

    elif x.title() in data:
        return data[x.title()]

    elif x.upper() in data:
        return data[x.upper()]

    elif len(get_close_matches(x, data.keys()))> 0 :
        print("Você quis dizer: %s ?" %get_close_matches(x, data.keys())[0])
        decide = input("A palavra é esta? s ou n? ")

        if decide == "s":
            return data[get_close_matches(x, data.keys())[0]]

        elif decide == "n":
            return ("Ops, acho que me enganei! ")

        else:
            return ("É só sim (s) ou não (n)... ")
    else:
        return "### Desculpe! Não pude encontrar! ###"

x = input("Fala que o dicionário escuta: ")
output = translate(x)

if type(output) == list:
    for i in output: 
        print(i)
else:
    print(output)
    
