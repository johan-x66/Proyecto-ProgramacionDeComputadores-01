import numpy as np
import os, time


def main_menu():
    clear()
    print("╔" + "═" * 34 + "╗")
    print("║     🚗  SISTEMA DE PARQUEADERO   ║")
    print("╚" + "═" * 34 + "╝")
    print("""
📋 MENÚ PRINCIPAL
──────────────────────────────
1️⃣  Ver precios del parqueadero
2️⃣  Ver puestos disponibles
3️⃣  Elegir puesto
4️⃣  Pago del servicio
5️⃣  Salir
──────────────────────────────
""")
    
def precio_menu():
    clear()
    print("📋 Precios del parqueadero:\n")
    print("""
- Moto:        1000 pesos/hora | 4000 pesos/día
- Carro:       2000 pesos/hora | 8000 pesos/día
- Bicicleta:    500 pesos/hora | 2000 pesos/día
""")
    pausa()


    
def ver_puestos():
    clear()
    print("A continuación podrá contemplar los puestos disponibles en el parqueadero")
    while True:
        print("1. Puestos carros \n2. Puestos motos \n3. Puestos para otro tipo de vehiculo \n4. Volver al menú principal ")
        try:
            option = int(input("Seleccione una opción: "))
            print("\n")
        except ValueError:
            print("⚠️  Ingrese un número válido.")
            continue
        match option:
            case 1:
                puestos_carros()
                input("Digite ENTER para volver: ")
                clear()
            case 2:
                puestos_motos()
                input("Digite ENTER para volver: ")
                clear()
            case 3:
                puestos_otros()
                input("Digite ENTER para volver: ")
                clear()
            case 4:
                print("Gracias por usar el servicio.")
                break
            case _:
                print("Error en los datos ingresados")
    pausa()

def elegir_puesto():
    clear()
    print("A continuación podrá elegir un puesto en el parqueadero")
    while True:
        print("1. Puestos carros \n2. Puestos motos \n3. Puestos para otro tipo de vehiculo \n4. Volver al menú principal ") 
        try:
            option = int(input("Seleccione una opción: "))
            print("\n")
        except ValueError:
            print("⚠️  Ingrese un número válido.")
            continue
        match option:
            case 1:
                puestos_carros()
                while True:
                    try:
                        opcion_fila = int(input("Por favor elija el numero de la fila: "))
                        opcion_columna = int(input("Por favor elija el numero de la columna: "))
                        if parqueadero_carros[opcion_fila][opcion_columna] == "LIBRE":
                            parqueadero_carros[opcion_fila][opcion_columna] = "OCUPADO"
                            break
                        else:
                            print("Esta ocupado, intente otra vez...")
                    except (ValueError, IndexError):
                        print("⚠️  Opción fuera de rango.")
                break
            case 2:
                puestos_motos()
                while True:
                    try:
                        opcion_fila = int(input("Por favor elija el numero de la fila: "))
                        opcion_columna = int(input("Por favor elija el numero de la columna: "))
                        if parqueadero_motos[opcion_fila][opcion_columna] == "LIBRE":
                            parqueadero_motos[opcion_fila][opcion_columna] = "OCUPADO"
                            break
                        else:
                            print("Esta ocupado, intente otra vez...")
                    except (ValueError, IndexError):
                        print("⚠️  Opción fuera de rango.")
                input("Digite ENTER para volver: ")
                break
            case 3:
                puestos_otros()
                while True:
                    try:
                        opcion_fila = int(input("Por favor elija el numero de la fila: "))
                        opcion_columna = int(input("Por favor elija el numero de la columna: "))
                        if parqueadero_otros[opcion_fila][opcion_columna] == "LIBRE":
                            parqueadero_otros[opcion_fila][opcion_columna] = "OCUPADO"
                            break
                        else:
                            print("Esta ocupado, intente otra vez...")
                    except (ValueError, IndexError):
                        print("⚠️  Opción fuera de rango.")
                break
            case 4:
                print("Gracias por usar el servicio, hasta luego.")
                break
            case _:
                print("Error en los datos ingresados")
    pausa()

def pagar_servicio():
    clear()
    print("💰 Pago del servicio de parqueadero:\n")
    tipo_vehiculo = int(input("""- Tipos de vehículos
    1. Moto
    2. Carro
    3. Vehículo ligero
Por favor elija el tipo de vehículo que guardo en el parqueadero: """))
    while True:
        print("""- Tipo de servicio
    1. Servicio por hora
    2. Servicio por día""")
        option1 = int(input("Por favor elija alguna opcion: "))
        match option1:
            case 1:
                hora = int(input("Por favor digite cuantas horas estuvo el vehículo en el parqueadero: "))
                if tipo_vehiculo == 1:
                    total = 1000 * hora
                elif tipo_vehiculo == 2:
                    total = 2000 * hora
                elif tipo_vehiculo == 3:
                    total = 500 * hora
                else:
                    print("Error en los datos")
                break
            case 2:
                dia = int(input("Por favor digite cuantas dias estuvo el vehículo en el parqueadero: "))
                if tipo_vehiculo == 1:
                    total = 4000 * dia
                elif tipo_vehiculo == 2:
                    total = 8000 * dia
                elif tipo_vehiculo == 3:
                    total = 2000 * dia
                else:
                    print("Error en los datos")
                break
            case _:
                print("Error en los datos")
    print(f"\n💵 Total a pagar: {total:,} pesos")
    pausa()

def puestos_carros():
    print("- Puestos Carros")
    for fila in range(filas_carros):
        for columna in range(columnas_carros):
            print(f"[{parqueadero_carros[fila][columna]:^7}]", end=" ")
        print()
    print()
def puestos_motos():
    print("- Puestos motos")
    for fila in range(filas_motos):
        for columna in range(columnas_motos):
            print(f"[{parqueadero_motos[fila][columna]:^7}]", end=" ")
        print()
    print()

def puestos_otros():
    print("- Puestos Otros")
    for fila in range(filas_otros):
        for columna in range(columnas_otros):
            print(f"[{parqueadero_otros[fila][columna]:^7}]", end=" ")
        print()
    print()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausa():
    input("\nPresione ENTER para continuar...")


filas_carros = 4
columnas_carros = 16
parqueadero_carros = [["LIBRE" for _ in range(columnas_carros)] for _ in range(filas_carros)]

filas_motos = 4
columnas_motos = 8
parqueadero_motos = [["LIBRE" for _ in range(columnas_motos)] for _ in range(filas_motos)]

filas_otros = 2
columnas_otros = 6
parqueadero_otros = [["LIBRE" for _ in range(columnas_otros)] for _ in range(filas_otros)]


  
while True:
    main_menu()
    try:
        option = int(input("Seleccione una opción: "))
        print("\n")
    except ValueError:
        print("Ingrese un número válido.")
        continue
    match option:
        case 1:
            precio_menu()
            clear()
        case 2:
            ver_puestos()
            clear()
        case 3:
            elegir_puesto()
            clear()
        case 4:
            pagar_servicio()
            input("Digite ENTER para volver al menú: ")
            clear()
        case 5:
            print("\n👋 Gracias por usar el sistema de parqueadero.")
            time.sleep(1.5)
            clear()
            break
        case _:
            print("Error en los datos ingresados")
            clear()
    