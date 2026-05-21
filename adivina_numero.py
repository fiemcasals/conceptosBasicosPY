# adivina_numero.py
# Este script es un juego interactivo de consola para adivinar un número aleatorio generado por la computadora.
# Tiene como objetivo demostrar el uso de la librería 'random', la captura de entradas mediante 'input()',
# el control de flujo con condicionales 'if-elif-else', y la iteración con un bucle 'while' controlado por condiciones.

# Importa el módulo 'random' que provee funciones para generación de datos pseudoaleatorios
import random

# Genera un número entero aleatorio entre 1 y 100 inclusive y lo asigna a la variable 'numero_secreto'
numero_secreto = random.randint(1, 100)

# Define e inicializa el contador de intentos del jugador comenzando desde cero
intentos = 0

# Define la cantidad límite de intentos permitidos para el juego
max_intentos = 7

# Inicializa la bandera booleana 'adivinado' en False indicando que el número aún no ha sido descubierto
adivinado = False

# Solicita el nombre del usuario por consola y lo almacena en la variable 'nombre'
nombre = input("Ingresa tu nombre: ")

# Muestra un mensaje de bienvenida y las instrucciones del juego utilizando interpolación de cadenas
print(f"¡Hola, {nombre}! Intenta adivinar el número secreto entre 1 y 100.")

# Ejecuta el bloque mientras el número de intentos sea menor al máximo y la bandera 'adivinado' sea False
while (intentos < max_intentos) and (not adivinado):
    # Suma 1 unidad al contador de intentos en cada ciclo o ronda de juego
    intentos += 1
    
    # Captura la entrada del usuario, la convierte a un número entero y la guarda en 'intento_usuario'
    intento_usuario = int(input(f"Intento {intentos}/{max_intentos}. Ingresa tu número: "))
    
    # Compara si el número ingresado por el usuario es menor que el número secreto
    if intento_usuario < numero_secreto:
        # Imprime una pista para orientar al jugador a ingresar un número mayor
        print("El número secreto es mayor.")
    
    # Compara si el número ingresado por el usuario es mayor que el número secreto
    elif intento_usuario > numero_secreto:
        # Imprime una pista para orientar al jugador a ingresar un número menor
        print("El número secreto es menor.")
    
    # Ejecuta este bloque si el número no es ni menor ni mayor (es decir, el usuario acertó)
    else:
        # Cambia el estado de la bandera a True para finalizar la iteración en el próximo chequeo del bucle
        adivinado = True

# Evalúa si la iteración del juego terminó porque el usuario descubrió exitosamente el número secreto
if adivinado:
    # Imprime un mensaje felicitando al usuario por ganar y muestra los intentos que le tomó
    print(f"¡Felicitaciones, {nombre}! Adivinaste el número secreto en {intentos} intentos.")

# Ejecuta este bloque en caso de que el bucle terminara y el número secreto no haya sido adivinado
else:
    # Muestra un mensaje de fin de juego informando cuál era el número secreto generado
    print(f"Lo siento, {nombre}. Agotaste tus {max_intentos} intentos. El número era {numero_secreto}.")
