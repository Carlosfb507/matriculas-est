import tkinter as tk
from tkinter import ttk, messagebox
from funcionalidades import validar_funcion, metodo_biseccion, metodo_newton_raphson

def validar_funcion_interfaz():
    """
    Verifica si la función ingresada es válida y da retroalimentación visual.
    """
    funcion = entrada_funcion.get()
    if validar_funcion(funcion):
        entrada_funcion.configure(bg="lightgreen")
        messagebox.showinfo("Validación", "La función ingresada es válida.")
    else:
        entrada_funcion.configure(bg="red")
        messagebox.showerror("Error", "La función ingresada no es válida.")


def calcular():
    """
    Realiza el cálculo según la selección del usuario.
    """
    funcion = entrada_funcion.get()
    metodo = metodo_seleccionado.get()

    if not validar_funcion(funcion):
        messagebox.showerror("Error", "La función ingresada no es válida.")
        return

    try:
        tolerancia = float(entrada_tolerancia.get())
        iteraciones = int(entrada_iteraciones.get())
        resultados = []

        if metodo == "Cerrado (Bisección)" or metodo == "Ambos métodos":
            a = float(entrada_a.get())
            b = float(entrada_b.get())
            resultado = metodo_biseccion(funcion, a, b, tolerancia, iteraciones)
            resultados.append(f"Método Bisección:\n{resultado}")
        
        if metodo == "Abierto (Newton-Raphson)" or metodo == "Ambos métodos":
            x0 = float(entrada_x0.get())
            resultado = metodo_newton_raphson(funcion, x0, tolerancia, iteraciones)
            resultados.append(f"Método Newton-Raphson:\n{resultado}")
        
        salida_resultados.configure(state="normal")
        salida_resultados.delete("1.0", tk.END)
        salida_resultados.insert(tk.END, "\n\n".join(resultados))
        salida_resultados.configure(state="disabled")
    except Exception as e:
        messagebox.showerror("Error", f"Error al calcular: {e}")


# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Métodos Numéricos")
ventana.geometry("600x600")

# Entradas
tk.Label(ventana, text="Ingrese la función f(x):").grid(row=0, column=0, padx=10, pady=5)
entrada_funcion = tk.Entry(ventana, width=40)
entrada_funcion.grid(row=0, column=1, padx=10, pady=5)

boton_validar = tk.Button(ventana, text="Validar Función", command=validar_funcion_interfaz)
boton_validar.grid(row=0, column=2, padx=10, pady=5)

tk.Label(ventana, text="Seleccione el método:").grid(row=1, column=0, padx=10, pady=5)
metodo_seleccionado = ttk.Combobox(ventana, values=["Cerrado (Bisección)", "Abierto (Newton-Raphson)", "Ambos métodos"])
metodo_seleccionado.grid(row=1, column=1, padx=10, pady=5)

tk.Label(ventana, text="Tolerancia:").grid(row=2, column=0, padx=10, pady=5)
entrada_tolerancia = tk.Entry(ventana, width=10)
entrada_tolerancia.grid(row=2, column=1, padx=10, pady=5)

tk.Label(ventana, text="Iteraciones máximas:").grid(row=3, column=0, padx=10, pady=5)
entrada_iteraciones = tk.Entry(ventana, width=10)
entrada_iteraciones.grid(row=3, column=1, padx=10, pady=5)

tk.Label(ventana, text="Intervalo [a, b]:").grid(row=4, column=0, padx=10, pady=5)
entrada_a = tk.Entry(ventana, width=10)
entrada_a.grid(row=4, column=1, padx=10, pady=5)
entrada_b = tk.Entry(ventana, width=10)
entrada_b.grid(row=4, column=2, padx=10, pady=5)

tk.Label(ventana, text="Punto inicial (x0):").grid(row=5, column=0, padx=10, pady=5)
entrada_x0 = tk.Entry(ventana, width=10)
entrada_x0.grid(row=5, column=1, padx=10, pady=5)

boton_calcular = tk.Button(ventana, text="Calcular", command=calcular)
boton_calcular.grid(row=6, column=1, padx=10, pady=10)

tk.Label(ventana, text="Resultados:").grid(row=7, column=0, padx=10, pady=5)
salida_resultados = tk.Text(ventana, width=70, height=20, state="disabled")
salida_resultados.grid(row=7, column=1, columnspan=2, padx=10, pady=5)

ventana.mainloop()





