from tkinter import *
import pandas
import random
import os

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# File paths for the CSV files
words_to_learn_file = "words_to_learn.csv"
unknown_words_file = "unknown_words.csv"
original_file = "data/french_words.csv"

# Clear previous CSV files at the start of the program
def clear_files():
    if os.path.exists(words_to_learn_file):
        os.remove(words_to_learn_file)  # Delete the words_to_learn.csv file if it exists
    if os.path.exists(unknown_words_file):
        os.remove(unknown_words_file)  # Delete the unknown_words.csv file if it exists

clear_files()  # Clear the CSV files at the start

# Create the window
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Load the original French words dataset
original_data = pandas.read_csv(original_file)
to_learn = original_data.to_dict(orient="records")

# Function to show the next card
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)  # Cancel the previous flip timer
    
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    
    flip_timer = window.after(3000, flip_card)  # Flip the card after 3 seconds

# Function to flip the card to show English and mark as unknown
def flip_card():
    global current_card
    # Mark the word as "unknown" (since it wasn't marked as known)
    data = pandas.DataFrame([current_card])
    data.to_csv(unknown_words_file, mode="a", header=False, index=False)  # Append the current card to the unknown words CSV

    # Change the card to show the English word
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

# Function when the user knows the word
def is_known():
    to_learn.remove(current_card)  # Remove the current card from the list of words to learn
    data = pandas.DataFrame(to_learn)
    data.to_csv(words_to_learn_file, index=False)  # Save the updated list to the CSV file
    next_card()

# Canvas for the card
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="C:/Users/madhu/Downloads/flash-card-project-start/images/card_front.png")
card_back_img = PhotoImage(file="C:/Users/madhu/Downloads/flash-card-project-start/images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=1, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

# Text for title and word
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 253, text="", font=("Arial", 60, "bold"))

# Cross image button (unknown)
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, command=next_card)
unknown_button.grid(row=2, column=0)

# Right image button (known)
right_image = PhotoImage(file="images/right.png")
known_button = Button(image=right_image, command=is_known)
known_button.grid(row=2, column=1)

# Timer to flip the card
flip_timer = window.after(3000, flip_card)

# Start with the first card
next_card()

# Start the main loop
window.mainloop()
