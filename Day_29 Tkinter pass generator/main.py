from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
# window.minsize(width=400,height=400)


# Background img 
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)

#Labels
web_label = Label(text="Website")
web_label.grid(column=0,row=1)

email_label = Label(text="Email/Username")
email_label.grid(column=0,row=2)

pass_label = Label(text="Password")
pass_label.grid(column=0,row=3)

# Entrys
web_input = Entry(width=45)
web_input.grid(column=1,row=1, columnspan=2)

email_input = Entry(width=45)
email_input.grid(column=1,row=2, columnspan=2)

pass_input = Entry(width=31)
pass_input.grid(column=1,row=3)

# Buttons
pass_button = Button(text="Generate Password")
pass_button.grid(column=2,row=3)

add_button = Button(text="Add", width=36)
add_button.grid(column=1,row=4, columnspan=2)

window.mainloop()