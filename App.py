from tkinter import *
import math

root = Tk()
root.title("Calculator")

display = Entry(root)
display.grid(row=0, column=0, columnspan=4, pady=5)
display.focus_set()  # Colocar el foco en la entrada al iniciar la calculadora

# Función para agregar números o operadores al campo de entrada
def add_to_display(value):
    display.insert(END, value)

# Función para eliminar el último carácter del campo de entrada
def undo():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        display.delete(0, END)
        display.insert(0, display_new_state)

# Función para limpiar el campo de entrada
def clear_display():
    display.delete(0, END)

# Función para calcular el resultado de la expresión en el campo de entrada
def calculate():
    try:
        display_state = display.get()
        result = eval(display_state)
        clear_display()
        display.insert(END, result)
    except Exception as e:
        clear_display()
        display.insert(END, 'Error')

# Lista de botones para los dígitos y operadores
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Crear y posicionar los botones en la ventana
row_num = 1
col_num = 0
for button_text in buttons:
    Button(root, text=button_text, width=5, height=2,
           command=lambda value=button_text: add_to_display(value)).grid(row=row_num, column=col_num)
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

# Botón para borrar el último carácter del campo de entrada
Button(root, text="⟵", width=5, height=2, command=undo).grid(row=5, column=0, columnspan=2)

# Botón para limpiar el campo de entrada
Button(root, text="AC", width=5, height=2, command=clear_display).grid(row=5, column=2, columnspan=2)

# Botón para calcular el resultado de la expresión en el campo de entrada
Button(root, text="=", width=5, height=2, command=calculate).grid(row=6, column=0, columnspan=4)

root.mainloop()
