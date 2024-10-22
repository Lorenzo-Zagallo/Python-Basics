import tkinter as tk
from tkinter import messagebox, ttk

def div_numeros():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 / num2
        messagebox.showinfo("Resultado", f"O quociente é igual à {resultado}")
    except ValueError:
        messagebox.showerror("Erro: Insira um número válido.")
    except ZeroDivisionError:
        messagebox.showerror("Erro: Não existe divisão por zero.")

screen = tk.Tk()
screen.title("Calculdora de Divisão")

frame = ttk.Frame(screen, padding=10)
frame.grid()

tk.Label(screen, text="Dividendo:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_num1 = tk.Entry(screen)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(screen, text="Divisor:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_num2 = tk.Entry(screen)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

tk.Button(screen, text="Dividir", command=div_numeros).grid(row=2, columnspan=2, padx=100, pady=50)

screen.mainloop()