from tkinter import *

# window = Tk()
# window.title("Meu primeiro GUI")
# window.minsize(width=500, height=300)
#
# #Label
#
# my_label = Label(text="Im a Label", font=("Arial", 24, "italic"))
# my_label.grid(column=0, row=0)
#
# my_label["text"] = "New Text"
# my_label.config(text="New Text")
#
# #Button
#
# def button_clicked():
#     str = input.get()
#     my_label.config(text=str)
#     print("I got clicked")
#
# button = Button(text="Click me", command=button_clicked)
# button.grid(column=1, row=1)
#
# button2 = Button(text="Click me2")
# button2.grid(column=2, row=0)
# #Entry
#
# input = Entry(width=10)
# input.gridbutton = Button(text="Click me", command=button_clicked)
# input.grid(column=4, row=3)

# Window
window = Tk()
window.title("Mile to Km Converter")
window.minsize()
window.config(padx=20, pady=20)
# Input
input = Entry()
input.insert(END, string="0")
input.grid(row=0, column=1)

# Labels
label1 = Label(text="Miles")
label1.grid(row=0, column=2)

label2 = Label(text="is equal to")
label2.grid(row=1, column=0)

label3 = Label(text="Km")
label3.grid(row=1, column=2)

label4 = Label(text="0")
label4.grid(row=1, column=1)
# Button

def calculate():
    miles = float(input.get())
    label4.config(text=str(1.61*miles))

button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)





window.mainloop()