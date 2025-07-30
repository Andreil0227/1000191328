from fastapi import FastAPI
import base64

app: FastAPI = FastAPI(

    title="TalentoTech - API Cifrado Base64",
    description="API Cifrado Base64"
)

@app.get(
    "/CifradoBase64",
    summary="Base64",
    description="Cifrado Base64",
    tags=["Base64"]
)

async def cifrar_base64(mensaje: str) -> str:
    # Convertimos el mensaje a bytes
    mensaje_bytes = mensaje.encode('utf-8')
    # Codificamos a base64
    mensaje_base64 = base64.b64encode(mensaje_bytes)
    # Devolvemos como string
    return mensaje_base64.decode('utf-8')

@app.get(
    "/DescifradoBase64",
    summary="Base64",
    description="Descifrado Base64",
    tags=["Base64"]
)

async def descifrar_base64(mensaje_cifrado: str) -> str:
    """
    Decodifica un mensaje codificado en Base64.

    :param mensaje_cifrado: Texto codificado en Base64.
    :return: Texto original descifrado.
    """
    try:
        # Convertimos a bytes
        mensaje_cifrado_bytes = mensaje_cifrado.encode('utf-8')
        # Decodificamos
        mensaje_descifrado = base64.b64decode(mensaje_cifrado_bytes)
        return mensaje_descifrado.decode('utf-8')
    except Exception as e:
        return f"❌ Error al decodificar: {str(e)}"

