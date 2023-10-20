from tkinter import messagebox as MessageBox

#Calcula un string de operandos y operadores

def calculate(opStr):
    try:
        if opStr == "":
            MessageBox.showerror("Error", "No hay datos para calcular")
            return ""

        # Evalúa la expresión
        result = eval(opStr)

        return result
    except ZeroDivisionError:
        MessageBox.showerror("Error", "División por cero no permitida")
        return ""
    
    except SyntaxError:
        MessageBox.showerror("Error", "Formato incorrecto de la operación")
        return ""

