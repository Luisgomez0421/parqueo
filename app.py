print("=== Parqueadero Riwi ===")

capacidad = 10
carros_parqueados = 5

while True:
    print("\nMENU")
    print("1. Agregar carro")
    print("2. Sacar carro")
    print("3. Ver estado")
    print("4. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        if carros_parqueados >= capacidad:
            print(" Parqueadero lleno. No hay cupos disponibles.")
        else:
            placa = input("Digite la placa del carro: ").strip().upper()
            
            if placa == "":
                print("La placa no puede estar vacía.")
            else:
                carros_parqueados += 1
                print(f"Carro {placa} agregado correctamente.")
                print(f"Cupos disponibles: {capacidad - carros_parqueados}").+
                                                        

    elif opcion == "2":
        if carros_parqueados <= 0:
            print(" No hay carros para retirar.")
        else:
            placa = input("Digite la placa del carro que sale: ").strip().upper()
            carros_parqueados -= 1
            print(f"Carro {placa} retirado correctamente.")
            print(f"Cupos disponibles: {capacidad - carros_parqueados}")

    elif opcion == "3":
        print(f"\nCapacidad total: {capacidad}")
        print(f"Carros parqueados: {carros_parqueados}")
        print(f"Cupos disponibles: {capacidad - carros_parqueados}")

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opcion invalida. Intente nuevamente.")
