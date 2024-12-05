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

    # Validar función antes de continuar
    if not validar_funcion(funcion):
        messagebox.showerror("Error", "La función ingresada no es válida. Valídela antes de continuar.")
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
        
        # Mostrar resultados
        salida_resultados.configure(state="normal")
        salida_resultados.delete("1.0", tk.END)
        salida_resultados.insert(tk.END, "\n\n".join(resultados))
        salida_resultados.configure(state="disabled")
        salida_resultados.tag_configure("success", foreground="green")
        salida_resultados.tag_add("success", "1.0", "end")
    
    except Exception as e:
        messagebox.showerror("Error", f"Error al calcular: {e}")
        salida_resultados.configure(state="normal")
        salida_resultados.insert(tk.END, f"\nError: {e}", "error")
        salida_resultados.configure(state="disabled")
        salida_resultados.tag_configure("error", foreground="red")
        salida_resultados.tag_add("error", "1.0", "end")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Métodos Numéricos")
ventana.geometry("600x550")
ventana.configure(bg="#d3d3d3")  # Fondo gris claro

# Estilo de botones y etiquetas
estilo_botones = {"bg": "#404040", "fg": "white", "font": ("Arial", 10)}
estilo_etiquetas = {"bg": "#d3d3d3", "fg": "black", "font": ("Arial", 10)}

# Entrada de la función
tk.Label(ventana, text="Ingrese la función f(x):", **estilo_etiquetas).grid(row=0, column=0, padx=10, pady=5, sticky="w")
entrada_funcion = tk.Entry(ventana, width=30)
entrada_funcion.grid(row=0, column=1, padx=10, pady=5)
boton_validar_funcion = tk.Button(ventana, text="Validar Función", command=validar_funcion_interfaz, **estilo_botones)
boton_validar_funcion.grid(row=0, column=2, padx=10, pady=5)

# Selección del método
tk.Label(ventana, text="Seleccione el método:", **estilo_etiquetas).grid(row=1, column=0, padx=10, pady=5, sticky="w")
metodo_seleccionado = ttk.Combobox(ventana, values=["Cerrado (Bisección)", "Abierto (Newton-Raphson)", "Ambos métodos"])
metodo_seleccionado.grid(row=1, column=1, padx=10, pady=5)

# Parámetros comunes
tk.Label(ventana, text="Tolerancia:", **estilo_etiquetas).grid(row=2, column=0, padx=10, pady=5, sticky="w")
entrada_tolerancia = tk.Entry(ventana, width=10)
entrada_tolerancia.grid(row=2, column=1, padx=10, pady=5, sticky="w")

tk.Label(ventana, text="Iteraciones:", **estilo_etiquetas).grid(row=3, column=0, padx=10, pady=5, sticky="w")
entrada_iteraciones = tk.Entry(ventana, width=10)
entrada_iteraciones.grid(row=3, column=1, padx=10, pady=5, sticky="w")

# Parámetros específicos
tk.Label(ventana, text="Intervalo [a, b]:", **estilo_etiquetas).grid(row=4, column=0, padx=10, pady=5, sticky="w")
entrada_a = tk.Entry(ventana, width=10)
entrada_a.grid(row=4, column=1, padx=10, pady=5, sticky="w")
entrada_b = tk.Entry(ventana, width=10)
entrada_b.grid(row=4, column=2, padx=10, pady=5, sticky="w")

tk.Label(ventana, text="Punto inicial x0:", **estilo_etiquetas).grid(row=5, column=0, padx=10, pady=5, sticky="w")
entrada_x0 = tk.Entry(ventana, width=10)
entrada_x0.grid(row=5, column=1, padx=10, pady=5, sticky="w")

# Botón para calcular
boton_calcular = tk.Button(ventana, text="Calcular", command=calcular, **estilo_botones)
boton_calcular.grid(row=6, column=1, pady=10)

# Salida de resultados
tk.Label(ventana, text="Resultados:", **estilo_etiquetas).grid(row=7, column=0, padx=10, pady=5, sticky="nw")
salida_resultados = tk.Text(ventana, width=70, height=10, state="disabled", bg="#f5f5f5")
salida_resultados.grid(row=7, column=1, columnspan=2, padx=10, pady=5)

ventana.mainloop()


