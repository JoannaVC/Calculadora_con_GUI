from sumar import suma
from resta import resta
from multiplicacion import multiplicar
from dividir import dividir
from sumatoria import suma_avanzada
from porcentaje import porcentaje
import tkinter as tk

# Ventana principal
root = tk.Tk()
root.title("Calculadora")
root.geometry("600x400")
root.minsize(300, 200)
root.maxsize(800, 600)
root.resizable(True, False)

# Frame superior: Título
frame_superior = tk.Frame(root)
frame_superior.pack(fill="x", padx=10, pady=10)
label = tk.Label(frame_superior, text="Calculadora", font=("Arial", 14))
label.pack()

# Frame central: Operación + Entrada + Botones
frame_central = tk.Frame(root)
frame_central.pack(expand=True, padx=10, pady=10)
label1 = tk.Label(frame_central, text="Operación:", font=("Arial", 12))
label1.pack(pady=5)
entrada = tk.Entry(frame_central)
entrada.pack(fill="x", pady=5)

# Label de resultado
resultado_label = tk.Label(frame_central, text="Resultado: ", font=("Arial", 12), fg="green")
resultado_label.pack(pady=5)

# Frame de botones
frame_botones = tk.Frame(frame_central)
frame_botones.pack(pady=10)

# Función principal
def operacion(op):
    valores = entrada.get().split()  # separar por espacio
    try:
        if op == "Σ":
            # Suma avanzada acepta cualquier cantidad de números
            if not valores:
                raise ValueError("Ingresa al menos un número")
            numeros = []
            for v in valores:
                try:
                    numeros.append(float(v))
                except ValueError:
                    raise ValueError("Todos los valores deben ser números válidos separados por espacio")
            res = suma_avanzada(numeros)
        else:
            # Operaciones binarias requieren exactamente 2 números
            if len(valores) != 2:
                raise ValueError("Ingresa exactamente 2 números separados por espacio")
            try:
                a = float(valores[0])
                b = float(valores[1])
            except ValueError:
                raise ValueError("Todos los valores deben ser números válidos")
            funciones = {
                "+": suma,
                "-": resta,
                "*": multiplicar,
                "/": dividir,
                "%": porcentaje
            }
            if op not in funciones:
                raise ValueError("Símbolo no válido para esta operación")
            res = funciones[op](a, b)

        resultado_label.config(text=f"Resultado: {res}")
    except ValueError as ve:
        resultado_label.config(text=f"Error: {ve}")
    except Exception:
        resultado_label.config(text="Error: Entrada inválida")

# Botones
botones_info = [("+", "+"), ("-", "-"), ("*", "*"), ("/", "/"), ("%", "%"), ("Σ", "Σ")]
for texto_btn, simbolo in botones_info:
    tk.Button(frame_botones, text=texto_btn, width=4, command=lambda s=simbolo: operacion(s)).pack(side="left", padx=2)

# Frame inferior: Instrucciones
frame_inferior = tk.Frame(root)
frame_inferior.pack(fill="x", padx=10, pady=10)
texto = tk.Text(frame_inferior, wrap="word", height=5, width=60,
                font=("Arial", 8), fg="gray", bg=root.cget("bg"), relief="flat")
texto.insert("1.0", "INSTRUCCIONES: ")
texto.insert("end", "Ingresa los números separados por espacio (solo puede tomar 2 entradas a excepción de suma avanzada), da click en el botón de la operación que quieres realizar y obtendrás el resultado.")
texto.tag_add("resaltado", "1.0", "1.13")
texto.tag_config("resaltado", foreground="blue", font=("Arial", 8, "bold"))
texto.config(state="disabled")
texto.pack()

root.mainloop()