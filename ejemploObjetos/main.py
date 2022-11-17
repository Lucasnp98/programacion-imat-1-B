from objetos.Coche import Coche
from excepciones.MatriculaError import MatriculaError

if __name__ == "__main__":

    coches = []
    menu = """

    --------------------------------------------
    Opción 1: Cargar coches por defecto.
    Opción 2: Añadir coches manualmente.
    Opción 3: Mostrar información de los coches.
    Opción 4: Salir.
    --------------------------------------------

    """
    opc = 1
    while opc != 4:
        print(menu)
        bucle = True
        while bucle:
            try:

                opc = int(input("Introduce una opción:"))
                bucle = False

            except ValueError as error:
                print(error)

        if opc == 1:
            coche1 = Coche("Mercedes CLA", "Negro", "1234GGG", 100000)
            coche2 = Coche("Audi A1", "Negro", "5678GGG", 1000)
            coche3 = Coche("Seat Ibiza", "Negro", "9999GGG", 2000)

            coches.append(coche1)
            coches.append(coche2)
            coches.append(coche3)

        elif opc == 2:
            bucle = True
            while bucle:
                try:
                    num_coches = int(input("Introduce el número de coches: "))
                    bucle = False
                except ValueError as error:
                    print(error)

            for i in range(num_coches):
                print("-"*50)
                print(f"Introduzca los datos del coche número {i+1}")
                print("-"*50)
            
                matricula = input("Matrícula: ")
                color = input("Color: ")
                modelo = input("Modelo: ")
                km = int(input("Kilometraje: "))

                try:
                    c = Coche(modelo, color, matricula, km)
                    coches.append(c)
                except MatriculaError as error:  # Si este except captura el raise, no añadimos el coche a la lista
                    print(error)

        elif opc == 3:
            contador = 1
            for coche in coches:
                print("-"*50)
                print(f"[*] Mostrando datos del coche número:  {contador} [*]")
                print("-"*50)
                print(coche)
                contador += 1

    print("Programa finalizado")
