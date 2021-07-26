BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random
global french_starting_word

window = Tk()

try:
    words = pandas.read_csv("./data/words_to_learn.csv")

except FileNotFoundError:
    words = pandas.read_csv("./data/french_words.csv")

finally:
    list_french = words["French"].to_list()
    list_english = words["English"].to_list()



def yes_button():
    canvas_front.itemconfig(actual_language, text="French")
    canvas_front.itemconfig(canvas_image, image=front_img)
    french_word = random.choice(list_french)
    english_word = list_english[list_french.index(french_word)]
    canvas_front.itemconfig(french_text, text=french_word)
    window.update()
    window.after(3000)
    canvas_front.itemconfig(canvas_image, image=back_img)
    canvas_front.itemconfig(actual_language, text="English")
    canvas_front.itemconfig(french_text, text=english_word)
    list_french.remove(french_word)
    list_english.remove(english_word)
    list_of_words = {}
    list_of_words.update({"French": list_french})
    list_of_words.update({"English": list_english})
    dict_to_csv = pandas.DataFrame(list_of_words)
    dict_to_csv.to_csv("./data/words_to_learn.csv")


def no_button():

    french_word = random.choice(list_french)
    english_word = list_english[list_french.index(french_word)]

    canvas_front.itemconfig(actual_language, text="French")
    canvas_front.itemconfig(canvas_image, image=front_img)
    canvas_front.itemconfig(french_text, text=french_word)
    window.update()
    window.after(3000)
    canvas_front.itemconfig(canvas_image, image=back_img)
    canvas_front.itemconfig(actual_language, text="English")
    canvas_front.itemconfig(french_text, text=english_word)



# def pause_screen(b):
#     window.after(3000)
#     english_word = b
#     canvas_front.itemconfig(canvas_image, image=back_img)
#     canvas_front.itemconfig(actual_language, text="English")
#     canvas_front.itemconfig(french_text, text=english_word)


window.title("Flashy App")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas_front = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
canvas_image = canvas_front.create_image(400, 270, image=front_img)
canvas_front.grid(column=0, row=0, columnspan=2)
actual_language = canvas_front.create_text(400, 150, text="French", font=("Arial", 30, "italic"))
french_text = canvas_front.create_text(400, 280, text="French Word", font=("Arial", 40, "bold"))

button_no_img = PhotoImage(file="./images/wrong.png")
button_no = Button(image=button_no_img, highlightthickness=0, command=no_button)
button_no.grid(row=1, column=0)

button_yes_img = PhotoImage(file="./images/right.png")
button_yes = Button(image=button_yes_img, highlightthickness=0, command=yes_button)
button_yes.grid(row=1, column=1)

no_button()

window.mainloop()