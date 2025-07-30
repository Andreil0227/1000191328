import base58

def cifrar_base58(mensaje: str) -> str:
    """
    Codifica un mensaje en Base64.

    :param mensaje: Texto original a codificar.
    :return: Mensaje codificado en Base64.
    """
    # Convertimos el mensaje a bytes
    mensaje_bytes = mensaje.encode('utf-8')
    # Codificamos a base64
    mensaje_base58 = base58.b58encode(mensaje_bytes)
    # Devolvemos como string
    return mensaje_base58.decode('utf-8')


def descifrar_base58(mensaje_cifrado: str) -> str:
    """
    Decodifica un mensaje codificado en Base64.

    :param mensaje_cifrado: Texto codificado en Base64.
    :return: Texto original descifrado.
    """
    try:
        # Convertimos a bytes
        mensaje_cifrado_bytes = mensaje_cifrado.encode('utf-8')
        # Decodificamos
        mensaje_descifrado = base58.b58decode(mensaje_cifrado_bytes)
        return mensaje_descifrado.decode('utf-8')
    except Exception as e:
        return f"❌ Error al decodificar: {str(e)}"

# Ejemplo de uso
if __name__ == "__main__":

    Eleccion= input("Desea cifrar o descifrar?"+"\n 1 para cifrar o 2 para descifrar ")

    if Eleccion == '1':
        texto_original = input ("ingrese el mensaje que desea cifrar: ")
        cifrado = cifrar_base58(texto_original)
        print("Cifrado Base64:", cifrado)

    elif Eleccion == '2':
        texto_descifrar = input ("ingrese el mensaje que desea descifrar ")
        descifrado = descifrar_base58(texto_descifrar)
        print("Texto descifrado:", descifrado)
    
    else:
        print("Ya nada por loca")
