nombres = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]

magos = []
cientificos = []
otros = []

for items in nombres:
    if items in ["Harry Houdini", "David Blaine","Teller"]:
        magos.append(items)
    elif items in ["Newton", "Hawking","Einstein"]:
        cientificos.append(items)
    else:
        otros.append(items)

def hacer_grandioso():
    for i in range(len(magos)):
        granmagos = "El gran " + (magos[i]) 
        if i < len(magos) - 1:
            print(granmagos, end=", ")
        else:
            print(granmagos, end=".")
    return

def imprimir_nombres():
    print(*nombres, sep=", ", end=".",)
    return

print("------------------------------------\nLista de nombres: ")
imprimir_nombres()

print("\n------------------------------------")

print("Lista de magos grandiosos: ")
hacer_grandioso()

print("\n------------------------------------")

print("Lista de cientificos: ")
print(*cientificos, sep=", ", end=".")

print("\n------------------------------------")

print("Lista de otros: ")
print(*otros, sep=", ", end=".")

print("\n------------------------------------")