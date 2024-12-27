from tkinter import *

def button_clicked():
    new_text = int(input.get()) * 1.6
    km_label.config(text=new_text)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)


input = Entry(width=10)
input.grid(column=1,row=0)
input.focus()

miles_label = Label(text="Label", font=("Arial", 24, "bold"))
miles_label.grid(column=2,row=0)
miles_label.config(text="Miles")

equal_label = Label(text="Label", font=("Arial", 24, "bold"))
equal_label.config(text="is equal to")
equal_label.grid(column=0,row=1)

km_label = Label(text="Label", font=("Arial", 20))
km_label.config(text="0")
km_label.grid(column=1,row=1)

unit_label = Label(text="Label", font=("Arial", 24, "bold"))
unit_label.config(text="Km")
unit_label.grid(column=2,row=1)

button = Button(text="Convert", command=button_clicked)
button.grid(column=1,row=2)


window.mainloop()