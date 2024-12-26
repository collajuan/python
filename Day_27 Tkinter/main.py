from tkinter import *

# Event listener
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My first GUI program")
window.minsize(width=500,height=300)


my_label = Label(text="Label", font=("Arial", 24, "bold"))
my_label.config(text="new text")
my_label.grid(column=0,row=0)

button = Button(text="click", command=button_clicked)
button.grid(column=1,row=1)

new_button = Button(text="click", command=button_clicked)
new_button.grid(column=2,row=0)

input = Entry(width=10)
input.grid(column=3,row=3)


window.mainloop()
