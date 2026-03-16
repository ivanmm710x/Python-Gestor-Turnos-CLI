def decorador(funcion):
        print("Buenas")
        funcion()
        print("Espera y seras atendido")

def perfumeria():
    x = 0
    while x > -1:
        x += 1
        yield f'P-{x}'

def farmacia():
    x = 0
    while x > -1:
        x += 1
        yield f'F-{x}'

def cosmetica():
    x = 0
    while x > -1:
        x += 1
        yield f'C-{x}'

p = perfumeria()
f = farmacia()
c = cosmetica()

def decorador(opcion):
    print("\n" + "*" * 23)
    print("Su turno es:")
    if opcion == 'P':
        print(next(p))
    elif opcion == 'F':
        print(next(f))
    else:
        print(next(c))
    print("Espera y seras atendido")
    print("\n" + "*" * 23)





