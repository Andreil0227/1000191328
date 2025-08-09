import numpy as np
import random as rm




Valor_1 = int()
Valor_2 = int()
Premio = rm.choice(range(0 , 1111))

print(f"El valor a coincidir es: {Premio}")
Valor_1 = int(input("Por favor ingrese la cantidad de intentos que cree que tomará igualar "))
Valor_2 = int(input("Por favor ingrese la cantidad de intentos que cree que tomará igualar "))


Resultado = int(0)

Intentos = int(0)
print (Premio)
while Resultado != Premio:
    Resultado = rm.choice(range(0, 1111))
    Intentos += 1

def evaluar_jugador(nombre, prediccion):
    if prediccion > Intentos:
        print(f"{nombre} se pasó. ¡Pierde automáticamente!")
        return float('inf')  # Representa una pérdida
    else:
        return abs(Intentos - prediccion)

dif1 = evaluar_jugador("Jugador 1", Valor_1)
dif2 = evaluar_jugador("Jugador 2", Valor_2)

# Determinar el ganador
if dif1 == dif2:
    print("¡Empate!")
elif dif1 < dif2:
    print("¡Jugador 1 gana!")
else:
    print("¡Jugador 2 gana!")
