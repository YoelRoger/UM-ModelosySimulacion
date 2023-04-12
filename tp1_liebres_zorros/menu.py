from simulator import Simulator


class Menu:

    @staticmethod
    def show_menu():
        print("Seleccione una opción:")
        print("1. Correr simulación con valores por defecto.")
        print("2. Correr simulación con parámetros personalizados.")
        print("3. Salir.")
        option = input()

        if option == "1":
            dp = Simulator()
            liebres_array, zorros_array, tiempo_array = dp.simulation()
            dp.plot_graphs(liebres_array, zorros_array, tiempo_array)
        elif option == "2":
            # Pedir los valores por consola
            print("\nIngresa los siguientes valores para la simulación:")
            zorros_iniciales = int(input("Cantidad de zorros iniciales: "))
            tiempo_simulacion = int(input("Tiempo de simulación (en semanas): "))
            tasa_natalidad_lieb = float(input("Tasa de natalidad de las liebres: "))
            tasa_mortandad_lieb = float(input("Tasa de mortandad de las liebres: "))
            tasa_mortandad_zorr = float(input("Tasa de mortandad de los zorros: "))
            tasa_natalidad_zorr = float(input("Tasa de natalidad de los zorros: "))
            liebres_iniciales = int(input("Cantidad de liebres iniciales: "))

            variacion_tiempo = float(input("Variación de tiempo (en semanas): "))
            dp = Simulator(liebres_iniciales, zorros_iniciales, tiempo_simulacion, tasa_natalidad_lieb,
                           tasa_mortandad_lieb, tasa_mortandad_zorr, tasa_natalidad_zorr, variacion_tiempo,
                           tiempo_inicial=1)
            # Correr la simulación con los valores ingresados
            liebres_array, zorros_array, tiempo_array = dp.simulation()
            dp.plot_graphs(liebres_array, zorros_array, tiempo_array)
        elif option == "3":
            print("Saliendo del programa...")
            exit()
        else:
            print("Opción inválida. Por favor, ingresa una opción válida.")
