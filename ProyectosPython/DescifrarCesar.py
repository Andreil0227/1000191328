def descifrar(texto, desplazamiento):
    resultado=""
    for letra in texto:
        if letra.isalpha():
            base = ord('A') if letra.isupper() else ord('a')
            resultado += chr((ord(letra) - base + desplazamiento) %26 + base)

        else:
            resultado += letra

    return resultado

Mensaje = "Khoor Grq FkdwJ37, orv whqhv txh vhu hvwlrv dvxvwhv!"
desplazamiento = -3

mensaje_descifrar = descifrar(Mensaje, desplazamiento)

print(f"Mensaje descifrado:  {mensaje_descifrar}")