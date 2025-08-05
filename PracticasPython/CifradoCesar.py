def cifrar(texto, desplazamiento):
    resultado=""
    for letra in texto:
        if letra.isalpha():
            base = ord('A') if letra.isupper() else ord('a')
            resultado += chr((ord(letra) - base + desplazamiento) % 26 + base)

        else:
            resultado += letra
    return resultado

def descifrar(texto, desplazamiento):
    return cifrar(texto, -desplazamiento)

Mensaje = input("Por favor ingrese el número que desea cifrar: ")
desplazamiento = 3

mensaje_cifrado= cifrar(Mensaje, desplazamiento)
descifrar_mensaje = descifrar(mensaje_cifrado, desplazamiento)

print(f"El mensaje es:   {Mensaje}")
print(f"El cifrado es:   {mensaje_cifrado}")
print(f"El descifrado es:   {descifrar_mensaje}")