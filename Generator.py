print("1 - Trójkąt Prostokątny")
print("2 - Trójkąt Równoramienny")
odpowiedz = int(input("Podaj opcję z powyższych: "))
szerokosc = int(input("Podaj szerokość: "))
if odpowiedz == 1:
    if szerokosc % 2 == 0:
        for i in range(1, szerokosc + 1, 2):
            print(i * "*")

    else:
        print("Podaj parzystą liczbę!")

elif odpowiedz == 2:
    if szerokosc % 2 == 0:
        for i in range(1, szerokosc + 1, 2):
            print((i * "*").center(szerokosc))

    else:
        print("Podaj parzystą liczbę!")
else:
    print("Podaj prawidłową opcję!")
