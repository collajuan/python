from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}

def flip_card():
    canvas.itemconfig(card_title, text=f"English", fill="white")
    canvas.itemconfig(card_img, image=card_back)
    canvas.itemconfig(card_text, text=f"{current_card["English"]}", fill="white")



def random_word():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text=f"French", fill="black")
    canvas.itemconfig(card_text, text=f"{current_card["French"]}", fill="black")
    canvas.itemconfig(card_img, image=card_front)
    timer = window.after(3000, flip_card)

def is_known():
    to_learn.remove(current_card)
    random_word()
    data_to_learn = pandas.DataFrame(to_learn)
    data_to_learn.to_csv("data/words_to_learn.csv", index=False)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
timer = window.after(3000, flip_card)

# Card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400,263,image=card_front)
canvas.grid(column=0,row=0, columnspan=2)

card_title = canvas.create_text(400,150,text="", font=("Arial",40, "italic"))
card_text = canvas.create_text(400,263,text="", font=("Arial",60, "bold"))

# buttons
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=random_word)
wrong_button.grid(column=0,row=1)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=1,row=1)

# print(data)
# print(french_words)


random_word()


window.mainloop()
