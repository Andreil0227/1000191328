import tkinter as tk
from tkinter import messagebox
import random as rm

# --- Variables globales ---
premio_actual = [rm.choice(range(0, 9999))]  # Valor a adivinar
victorias = {"jugador1": 0, "jugador2": 0}
partidas_jugadas = [0]  # lista para mutabilidad

# --- Función para jugar una ronda ---
def jugar():
    try:
        pred_1 = int(entry_jugador1.get())
        pred_2 = int(entry_jugador2.get())
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores numéricos.")
        return

    if pred_1 <= 0 or pred_2 <= 0:
        messagebox.showwarning("Valor inválido", "Las predicciones deben ser mayores que 0.")
        return

    resultado = None
    intentos = 0
    while resultado != premio_actual[0]:
        resultado = rm.choice(range(0, 9999))
        intentos += 1

    label_resultado.config(text=f"Intentos reales: {intentos}")

    def evaluar(pred):
        if pred > intentos:
            return float('inf')
        else:
            return abs(intentos - pred)

    dif1 = evaluar(pred_1)
    dif2 = evaluar(pred_2)

    if dif1 == dif2:
        mensaje = "¡Empate!"
    elif dif1 < dif2:
        mensaje = "🎉 ¡Jugador 1 gana!"
        victorias["jugador1"] += 1
    else:
        mensaje = "🎉 ¡Jugador 2 gana!"
        victorias["jugador2"] += 1

    partidas_jugadas[0] += 1
    label_mensaje.config(text=mensaje)
    actualizar_contadores()

# --- Función para actualizar los contadores en pantalla ---
def actualizar_contadores():
    label_contadores.config(text=f"Victorias - Jugador 1: {victorias['jugador1']} | Jugador 2: {victorias['jugador2']} | Partidas jugadas: {partidas_jugadas[0]}")

# --- Función para reiniciar solo la partida (no los contadores) ---
def reiniciar():
    premio_actual[0] = rm.choice(range(0, 9999))
    label_premio.config(text=f"Número a coincidir: {premio_actual[0]}")
    entry_jugador1.delete(0, tk.END)
    entry_jugador2.delete(0, tk.END)
    label_resultado.config(text="")
    label_mensaje.config(text="")

# --- Función para reiniciar todo, incluyendo contadores ---
def reiniciar_todo():
    reiniciar()
    victorias["jugador1"] = 0
    victorias["jugador2"] = 0
    partidas_jugadas[0] = 0
    actualizar_contadores()

# --- Interfaz gráfica ---
ventana = tk.Tk()
ventana.title("Juego de Predicción")
ventana.geometry("450x420")
ventana.resizable(False, False)

# Premio
label_premio = tk.Label(ventana, text=f"Número a coincidir: {premio_actual[0]}", font=("Arial", 14, "bold"))
label_premio.pack(pady=10)

# Entradas
frame_inputs = tk.Frame(ventana)
frame_inputs.pack(pady=10)

tk.Label(frame_inputs, text="Predicción jugador 1:").grid(row=0, column=0, padx=5, pady=5)
entry_jugador1 = tk.Entry(frame_inputs)
entry_jugador1.grid(row=0, column=1)

tk.Label(frame_inputs, text="Predicción de jugador 2:").grid(row=1, column=0, padx=5, pady=5)
entry_jugador2 = tk.Entry(frame_inputs)
entry_jugador2.grid(row=1, column=1)

# Botón jugar
btn_jugar = tk.Button(ventana, text="¡Jugar!", command=jugar, bg="green", fg="white", width=20)
btn_jugar.pack(pady=10)

# Resultado
label_resultado = tk.Label(ventana, text="", font=("Arial", 12))
label_resultado.pack(pady=5)

# Mensaje
label_mensaje = tk.Label(ventana, text="", font=("Arial", 12, "bold"), fg="blue")
label_mensaje.pack(pady=5)

# Contadores
label_contadores = tk.Label(ventana, text="", font=("Arial", 11), fg="black")
label_contadores.pack(pady=10)
actualizar_contadores()

# Botones extra
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=5)

btn_reiniciar = tk.Button(frame_botones, text="Nuevo número", command=reiniciar, bg="orange", width=20)
btn_reiniciar.grid(row=0, column=0, padx=10)

btn_reiniciar_todo = tk.Button(frame_botones, text="Nueva partida", command=reiniciar_todo, bg="red", fg="white", width=20)
btn_reiniciar_todo.grid(row=0, column=1, padx=10)

# Ejecutar
ventana.mainloop()
