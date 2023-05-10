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

def imprimir_nombres():
    print("------------------------------------\nLista de nombres: ")
    print(*nombres, sep=", ", end=".")

def imprimir_todos():
    print("\n------------------------------------\nLista de magos: ")
    print(*magos,sep=", ", end=".")
    print("\n------------------------------------\nLista de cientificos: ")
    print(*cientificos,sep=", ", end=".")
    print("\n------------------------------------\nLista de otros: ")
    print(*otros,sep=", ", end=".")
    print("\n------------------------------------\nLista de grandes magos: ")
    hacer_grandioso()
    print("\n------------------------------------")

imprimir_nombres()
imprimir_todos()