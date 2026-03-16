import numeros

def preguntar():

    print("Bienvenido/a a La Farmacia del Barrio")

    while True:
        print("[P] - Perfumería\n[F] - Farmacia\n[C] - Cosmútica")
        try:
            opcion = input("Elija su opcion: ").upper()
            ["P", "F", "C"].index(opcion)
        except ValueError:
            print("Esa no es una opción válida")
        else:
            break

    numeros.decorador(opcion)


def inicio():

    while True:
        preguntar()
        try:
            otro_turno = input("Quieres sacar otro turno? [S] [N]: ").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("Esa no es una opción válida")
        else:
            if otro_turno == "N":
                print("Gracias por su visita")
                break

inicio()
