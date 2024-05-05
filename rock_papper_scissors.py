import tkinter as tk
from PIL import Image, ImageTk
import random

class RockPaperScissors:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Rock, Paper, Scissors")
        self.root.geometry("300x200")

        self.user_score = 0
        self.computer_score = 0

        self.result_label = tk.Label(self.root, text="Let's Play!", font=("Arial", 12))
        self.result_label.pack()

        choices = ["Rock", "Paper", "Scissors"]

        self.rock_button = tk.Button(self.root, text="Rock", command=lambda: self.play("Rock", choices))
        self.rock_button.pack(side=tk.LEFT)

        self.paper_button = tk.Button(self.root, text="Paper", command=lambda: self.play("Paper", choices))
        self.paper_button.pack(side=tk.LEFT)

        self.scissors_button = tk.Button(self.root, text="Scissors", command=lambda: self.play("Scissors", choices))
        self.scissors_button.pack(side=tk.LEFT)

        self.result_label.pack()

        self.root.mainloop()

    def play(self, user_choice, choices):
        computer_choice = random.choice(choices)

        result = ""
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Scissors" and computer_choice == "Paper") or \
             (user_choice == "Paper" and computer_choice == "Rock"):
            result = "You win this round!"
            self.user_score += 1
        else:
            result = "You lose this round."
            self.computer_score += 1

        self.result_label.config(text=f"User's Choice: {user_choice}\nComputer's Choice: {computer_choice}\nResult: {result}\nScore - You: {self.user_score}, Computer: {self.computer_score}")

if __name__ == "__main__":
    RockPaperScissors()