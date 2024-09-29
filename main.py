BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random



# ---------------------------- WORD GENERATOR ------------------------------- #
current_card = {}


try:
    russian_wdf = pandas.read_csv("russian_flash_cards/data/russian_to_learn.csv")
except FileNotFoundError:
    russian_wdf = pandas.read_csv("russian_flash_cards/data/russian1500freq.csv")
russian_dict = russian_wdf.to_dict(orient="records")

def new_word():
    global current_card,flip_timer
    russian_dict = russian_wdf.to_dict(orient="records")
    window.after_cancel(flip_timer)
    canvas.itemconfig(main_img, image=main_foto)
    new_word = random.choice(russian_dict)
    current_card = new_word
    canvas.itemconfig(top_label, text="Russian", fill="black")
    canvas.itemconfig(bottom_label, text=new_word["russian"], fill="black")

    flip_timer = window.after(3000,show_english_version)

def correct_button():
    print(current_card)
    russian_dict.remove(current_card)
    print(len(russian_dict))
    words_to_learn = pandas.DataFrame(russian_dict)
    words_to_learn.to_csv("russian_flash_cards/data/russian_to_learn.csv", index=False)
    new_word()


    

def show_english_version():
    global current_card
    canvas.itemconfig(main_img, image=back_img)
    canvas.itemconfig(top_label, text="English", fill="white")
    canvas.itemconfig(bottom_label, text=current_card["english"], fill="white")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Let's Learn Russian !")
window.minsize(width=1000,height=700)
window.config(bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,show_english_version)


canvas = Canvas(height=800,width=1000, highlightthickness=0,bg=BACKGROUND_COLOR)
main_foto = PhotoImage(file="russian_flash_cards/images/card_front.png")
main_img = canvas.create_image(500,300, image= main_foto)
top_label = canvas.create_text(500,180, text="Russian",fill="black",font=("Arial", 40, "italic"))
bottom_label = canvas.create_text(500,300, text="test123",fill="black",font=("Arial", 60, "bold"))
canvas.place(x=0,y=0)

back_img = PhotoImage(file="russian_flash_cards/images/card_back.png")

#Buttons
correct_img = PhotoImage(file="russian_flash_cards/images/right.png")
correct_button = Button(image=correct_img, highlightthickness=0,command=correct_button)
correct_button.place(x=650,y=575)

wrong_img = PhotoImage(file="russian_flash_cards/images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0,command=new_word)
wrong_button.place(x=250,y=575)



new_word()

window.mainloop()

