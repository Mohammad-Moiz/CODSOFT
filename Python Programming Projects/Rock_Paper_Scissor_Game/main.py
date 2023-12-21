import tkinter as tk
from tkinter import messagebox
import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_choice = user_choice_var.get().lower()
    computer_choice = get_computer_choice()

    result = determine_winner(user_choice, computer_choice)
    
    # Update result label
    result_label.config(text=f"{result}\nYou chose {user_choice}.\nThe computer chose {computer_choice}.")

def start_new_game():
    user_choice_var.set("rock")
    result_label.config(text="")

if __name__ == "__main__":
    # GUI setup
    root = tk.Tk()
    root.title("Rock-Paper-Scissors Game")
    root.geometry("400x300")  # Set a larger window size

    # Set background color
    root.configure(bg="#FFFFCC")

    # User choice dropdown
    user_choice_var = tk.StringVar(root)
    user_choice_var.set("rock")  # default choice
    user_choice_label = tk.Label(root, text="Choose:", font=("Arial", 14), bg="#FFFFCC")
    user_choice_dropdown = tk.OptionMenu(root, user_choice_var, "rock", "paper", "scissors")

    # Play button
    play_button = tk.Button(root, text="Play", command=play_game, bg="green", fg="white", font=("Arial", 12, "bold"))

    # New Game button
    new_game_button = tk.Button(root, text="New Game", command=start_new_game, bg="orange", fg="white", font=("Arial", 12, "italic"))

    # Exit button
    exit_button = tk.Button(root, text="Exit", command=root.destroy, bg="red", fg="white", font=("Arial", 12, "underline"))

    # Result label
    result_label = tk.Label(root, text="", font=("Arial", 12, "italic"), fg="blue", bg="#FFFFCC")

    # Pack elements into the window
    user_choice_label.pack(pady=10)
    user_choice_dropdown.pack(pady=10)
    play_button.pack(pady=10)
    new_game_button.pack(pady=10)
    exit_button.pack(pady=10)
    result_label.pack()

    # Start the Tkinter event loop
    root.mainloop()
