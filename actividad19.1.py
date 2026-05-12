
print(hello)
opcionMenu = 0

while opcionMenu != 3:
    print("Hola, buen dia, Querido usuario")

    print("===== MENÚ PRINCIPAL =====")
    print("1. Calculadora")
    print("2. Adivina el número")
    print("3. Salir")

    opcionMenu = int(input("¿Qué deseas hacer? "))

    if opcionMenu == 1:

        opcionSubM= 0

        while opcionSubM!= 5:

            print("\n-- Calculadora --")
            print("1. Sumar")
            print("2. Restar")
            print("3. Multiplicar")
            print("4. Division")
            print("5. Volver al menú principal")
            opcionSubM= int(input("¿Qué operación quieres? "))

            if opcionSubM== 1:
                a = int(input("Escribe el primer número: "))
                b = int(input("Escribe el segundo número: "))
                print("El resultado es:", a + b)

            elif opcionSubM== 2:
                a = int(input("Escribe el primer número: "))
                b = int(input("Escribe el segundo número: "))
                print("El resultado es:", a - b)

            elif opcionSubM== 3:
                a = int(input("Escribe el primer número: "))
                b = int(input("Escribe el segundo número: "))
                print("El resultado es:", a * b)

            elif opcionSubM== 4:
                a = int(input("Escriba el primer numero"))
                b = int(input("Ingrese el segundo numero"))
                print("El resultado es:", a / b)

            else:
                break   

    elif opcionMenu == 2:

        opcionSubM= 0
        NumSecre = 7

        while opcionSubM!= 3:

            print("\n-- Adivina el número --")
            print("1. Jugar")
            print("2. Ver una pista")
            print("3. Volver al menú principal")
            opcionSubM= int(input("¿Qué quieres hacer? "))

            if opcionSubM== 1:
                inte = int(input("¿Cuál crees que es el número? (del 1 al 10): "))
                if inte == NumSecre:
                    print("¡Felicitaciones, adivinaste!")
                elif inte < NumSecre:
                    print("No, el número es más grande")
                else:
                    print("No, el número es más pequeño")

            elif opcionSubM== 2:
                print("Pista: el número es impar")

            else:
                break   

    elif opcionMenu == 3:
        break   

    else:
        break   

print("\n Adios, que te vaya bien, querido usario")