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
        decide = input("That's it? y ou n.")

        if decide == "y":
            return data[get_close_matches(x, data.keys())[0]]

        elif decide == "n":
            return ("pugger yur paw steps on wrong keys ")

        else:
            return ("just n or y ")
    else:
        return "### Pugger yur paw steps on wrong keys ###"

x = input("Enter the word you want to search: ")
output = translate(x)

if type(output) == list:
    for i in output: 
        print(i)
else:
    print(output)
    
