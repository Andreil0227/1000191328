import tkinter as tk
from tkinter import messagebox
import base64

def cifrar_base64():
    mensaje = entrada_cifrar.get("1.0", tk.END).strip()
    if not mensaje:
        messagebox.showwarning("Advertencia", "Ingrese un mensaje para cifrar.")
        return

    try:
        mensaje_bytes = mensaje.encode('utf-8')
        mensaje_base64 = base64.b64encode(mensaje_bytes).decode('utf-8')
        salida_cifrada.delete("1.0", tk.END)
        salida_cifrada.insert(tk.END, mensaje_base64)
    except Exception as e:
        messagebox.showerror("Error", f"Error al cifrar: {str(e)}")

def descifrar_base64():
    mensaje_cifrado = entrada_descifrar.get("1.0", tk.END).strip()
    if not mensaje_cifrado:
        messagebox.showwarning("Advertencia", "Ingrese un mensaje Base64 para descifrar.")
        return

    try:
        mensaje_bytes = base64.b64decode(mensaje_cifrado.encode('utf-8'))
        mensaje_descifrado = mensaje_bytes.decode('utf-8')
        salida_descifrada.delete("1.0", tk.END)
        salida_descifrada.insert(tk.END, mensaje_descifrado)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo decodificar. Verifique que sea Base64 válido.\n\n{str(e)}")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Cifrado y Descifrado Base64")
ventana.geometry("600x600")
ventana.config(bg="#f2f2f2")

# ----- Sección de Cifrado -----
tk.Label(ventana, text="Texto para cifrar", bg="#f2f2f2", font=('Arial', 12, 'bold')).pack(pady=5)
entrada_cifrar = tk.Text(ventana, height=5, width=70)
entrada_cifrar.pack()

tk.Button(ventana, text="Cifrar a Base64", command=cifrar_base64, bg="#4CAF50", fg="white", font=('Arial', 10, 'bold')).pack(pady=5)

tk.Label(ventana, text="Texto cifrado en Base64", bg="#f2f2f2", font=('Arial', 12, 'bold')).pack()
salida_cifrada = tk.Text(ventana, height=3, width=70, bg="#e8e8e8")
salida_cifrada.pack()

# ----- Separador -----
tk.Label(ventana, text="").pack(pady=10)

# ----- Sección de Descifrado -----
tk.Label(ventana, text="Texto Base64 para descifrar", bg="#f2f2f2", font=('Arial', 12, 'bold')).pack()
entrada_descifrar = tk.Text(ventana, height=5, width=70)
entrada_descifrar.pack()

tk.Button(ventana, text="Descifrar Base64", command=descifrar_base64, bg="#2196F3", fg="white", font=('Arial', 10, 'bold')).pack(pady=5)

tk.Label(ventana, text="Texto descifrado", bg="#f2f2f2", font=('Arial', 12, 'bold')).pack()
salida_descifrada = tk.Text(ventana, height=3, width=70, bg="#e8e8e8")
salida_descifrada.pack()

# Ejecutar la ventana
ventana.mainloop()
