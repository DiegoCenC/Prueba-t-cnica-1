# Límite máximo de casos de prueba y valores de N y M
T_MAX = 5000
NM_MAX = 10**9

# Validación para el número de casos de prueba
while True:
    try:
        T = int(input("Ingresa el número de casos de prueba (entre 1 y 5000): "))
        if T <= 0 or T > T_MAX:
            print(f"El número de casos debe estar entre 1 y {T_MAX}.")
            continue
        break
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

respuestas = []

# Validación para cada par N y M
for i in range(T):
    while True:
        try:
            entrada = input(f"Ingresa N y M separados por un espacio (caso {i + 1}): ")
            numeros = entrada.split()
            
            # Verificamos que se hayan ingresado exactamente dos números
            if len(numeros) != 2:
                print("Por favor, ingresa exactamente dos números separados por un espacio.")
                continue
            
            N, M = map(int, numeros)
            
            # Verificamos que N y M estén en el rango permitido
            if N <= 0 or N > NM_MAX or M <= 0 or M > NM_MAX:
                print(f"N y M deben estar entre 1 y {NM_MAX}.")
                continue
            break
        except ValueError:
            print("Por favor, ingresa dos números enteros válidos.")

    # Determinamos la dirección final según la paridad de N y M
    if N % 2 == 1 and M % 2 == 1:
        respuestas.append("R")  # Derecha
    elif N % 2 == 1:
        respuestas.append("L")  # Izquierda
    elif M % 2 == 1:
        respuestas.append("D")  # Abajo
    else:
        respuestas.append("U")  # Arriba

# Imprimimos todas las respuestas, una por línea
print("\nLas direcciones finales son:")
for respuesta in respuestas:
    print(respuesta)
