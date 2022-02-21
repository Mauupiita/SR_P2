op=0

while op != 3:
    alfabetoMinus = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
     'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alfabetoMayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
     'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    print("1. Cifrar una frase")
    print("2. Desifrar")
    print("3.- Salir")
    op = int(input("Introduce el numero de la opcion: "))

    if op == 1:
        Palabra = input("Introduce tu frase: ")
        Clave = ''
        Tope = len(alfabetoMayus)
        Posicion = 0
        Avance=3
        for letra in Palabra:
            for i in range(Tope):
                if (i + Avance < Tope):
                    Posicion = i + Avance
                else:
                    Posicion = abs((Tope - i) - Avance)
                if letra == alfabetoMinus[i]:
                    Clave = Clave + alfabetoMinus[Posicion]
                elif letra == alfabetoMayus[i]:
                    Clave = Clave + alfabetoMayus[Posicion]

        print("Su cifrado es: ",Clave)


    if op == 2:
        Palabra = input("Introduce tu frase: ")
        Clave = ''
        Tope = len(alfabetoMayus)
        Posicion = 0
        Avance=-3
        for letra in Palabra:
            for i in range(Tope):
                if (i + Avance < Tope):
                    Posicion = i + Avance
                else:
                    Posicion = abs((Tope - i) - Avance)
                if letra == alfabetoMinus[i]:
                    Clave = Clave + alfabetoMinus[Posicion]
                elif letra == alfabetoMayus[i]:
                    Clave = Clave + alfabetoMayus[Posicion]

        print("Su cifrado es: ",Clave)



    
        
