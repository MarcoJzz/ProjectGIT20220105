import tkinter as tk
from tkinter import messagebox

def sumar():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        resultado = num1 + num2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce números válidos.")

def restar():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        resultado = num1 - num2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce números válidos.")

def multiplicar():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        resultado = num1 * num2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce números válidos.")

def dividir():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 == 0:
            raise ZeroDivisionError
        resultado = num1 / num2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ZeroDivisionError:
        messagebox.showerror("Error", "No se puede dividir por cero.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce números válidos.")

# Configurar la ventana principal
root = tk.Tk()
root.title("Calculadora")

# Crear widgets
label1 = tk.Label(root, text="Número 1:")
label1.grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

label2 = tk.Label(root, text="Número 2:")
label2.grid(row=1, column=0, padx=10, pady=10)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

button_sumar = tk.Button(root, text="Sumar", command=sumar)
button_sumar.grid(row=2, column=0, padx=10, pady=10)

button_restar = tk.Button(root, text="Restar", command=restar)
button_restar.grid(row=2, column=1, padx=10, pady=10)

button_multiplicar = tk.Button(root, text="Multiplicar", command=multiplicar)
button_multiplicar.grid(row=2, column=2, padx=10, pady=10)

button_dividir = tk.Button(root, text="Dividir", command=dividir)
button_dividir.grid(row=2, column=3, padx=10, pady=10)

label_resultado = tk.Label(root, text="Resultado: ")
label_resultado.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# Iniciar el bucle de la aplicación
root.mainloop()
