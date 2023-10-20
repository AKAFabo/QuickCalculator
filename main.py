from tkinter import *
from Utils.calculate import calculate

def onNumberButtonClick(num):

    currentText = entry.get()
    entry.delete(0, END)
    entry.insert(0,currentText + str(num))

def onOperatorClick(op):
    currentText = entry.get()
    entry.delete(0, END)
    entry.insert(0, currentText + op)

def onDeleteClick():
    currentText = entry.get()
    if currentText:                     #Validamos que no sea un string vacio
        updatedText = currentText[:-1]  # Elimina el último carácter
        entry.delete(0, END)
        entry.insert(0, updatedText)

def onCEClick():
    entry.delete(0, END)

def onEqualsClick():
    currentText = entry.get()
    res = calculate(currentText)
    entry.delete(0, END)
    entry.insert(0, str(res))

root = Tk()
root.geometry("320x500") #Tamaño de la calculadora de windows
root.title("Calculadora")


entry = Entry(root, font=('Arial', 20))
entry.place(x=10, y=10, width=300)

buttonFrame = Frame(root)
buttonFrame.place(x=10, y=70)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

for i, number in enumerate(numbers):
    row = i // 3
    col = i % 3
    numButton = Button(buttonFrame, text=str(number), font=('Arial', 20), width=4, command=lambda num=number: onNumberButtonClick(num))
    numButton.grid(row=row, column=col)


operators = ['*', '/', '%', '//', '**'] #Poner botones en la columna mas a la derecha

for i, operator in enumerate(operators):
    button = Button(buttonFrame, text=operator, font=('Arial', 20), width=4, command=lambda op=operator: onOperatorClick(op))
    button.grid(row=i, column=3)

# Agregar demas botones sin el uso de enumerates (Mas sencillo sin estos)
buttonPlus = Button(buttonFrame, text='+', font=('Arial', 20), width=4, command=lambda: onOperatorClick('+'))
buttonMinus = Button(buttonFrame, text='-', font=('Arial', 20), width=4, command=lambda: onOperatorClick('-'))

buttonPlus.grid(row=3, column=2)
buttonMinus.grid(row=3, column=1)

buttonDecimal = Button(buttonFrame, text='.', font=('Arial', 20), width=4, command=lambda: onOperatorClick('.'))
buttonDecimal.grid(row=4, column=2)

buttonDelete = Button(buttonFrame, text="<-", font=('Arial', 20), width=4, command=lambda: onDeleteClick())
buttonDelete.grid(row= 4, column=0)

buttonCE = Button(buttonFrame, text='CE', font=('Arial', 20), width=4, command=lambda: onCEClick())
buttonCE.grid(row=4, column=1)

buttonEquals = Button(buttonFrame, text='=', font=('Arial', 20), width=4, command=lambda: onEqualsClick())
buttonEquals.grid(row=5, column=0)

root.mainloop()
