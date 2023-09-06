def letraV(letra):
    return letra.lower() in ['a', 'e', 'i', 'o', 'u']

let = input("Pon una letra del abecedario: ")

if letraV(let):
    print(let," es vocal.")
else:
    print(let," es consonante.")
