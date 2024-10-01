from tkinter import *
import pandas
import random
import time
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Pandas Data
data = pandas.read_csv("data/french_words.csv")
data_to_dict = data.to_dict(orient ="records")
print(data_to_dict)

def next_card():
    global current_card
    canvas.itemconfig(card_background, image= card_front_img)
    current_card = random.choice(data_to_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word,text=current_card["French"], fill="black")
    window.after(3000, flip_card)
def flip_card():
    canvas.itemconfig(card_title, text="English", fill= "white")
    canvas.itemconfig(card_word,text=current_card["English"], fill= "white") 
    canvas.itemconfig(card_background, image= card_back_img)
def is_known():
    
# Canvas for the card
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file=r"C:/Users/madhu/Downloads/flash-card-project-start/images/card_front.png")
card_back_img = PhotoImage(file= r"images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)  # Changed 'img' to 'image'
canvas.grid(row=1, column=1)
canvas.config( bg=BACKGROUND_COLOR, highlightthickness=0)

# Text for title and word
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 253, text="", font=("Arial", 60, "bold"))

# Cross image button (unknown)
cross_image = PhotoImage(file=r"images/wrong.png")  # Use raw string to handle backslashes
unknown_button = Button(image= cross_image, command=next_card)  # Add highlightthickness for button appearance
unknown_button.grid(row=2, column=0)

# image button (known)
right_image = PhotoImage(file=r"images/right.png")  # Use raw string to handle backslashes
known_button = Button(image= right_image, command=next_card)  # Add highlightthickness for button appearance
known_button.grid(row=2, column=2)

next_card()

# Start the main loop
window.mainloop()
