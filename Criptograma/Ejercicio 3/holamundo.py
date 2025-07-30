# Codigo para que el usuario ingrese sus nombres y apellidos

def holamundo(): #Fucnión para pedir e imprimir los datos
    nombres = input("Por favor ingrese su nombre: ") #Variable que pide y guarda el nombre
    apellidos = input("\nPor favor ingrese su apellido: ")

    print(f"Hola mundo, {nombres + ' ' + apellidos}")
    return None

if __name__ == '__main__':
    holamundo()