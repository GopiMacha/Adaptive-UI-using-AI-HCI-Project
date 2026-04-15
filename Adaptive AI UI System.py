# A Gaussian Naive Bayes was used to create an adaptive quiz system in which the difficulty of questions is adjusted according to the score and errors. 
# When the interface was used, predict_level would use performance values to determine the difficulty, update_ui would dynamically change the interface colors and level display, next_question would select and display questions, check_answer would validate the response and update the score, and confirm_quit would exit confirmation.

import tkinter as tk
from tkinter import messagebox
import random
import numpy as np
from sklearn.naive_bayes import GaussianNB

# creating training data for performance and mistakes
X = [
    [0, 0], [1, 0], [2, 0],
    [2, 1], [3, 1], [4, 1],
    [4, 2], [5, 2], [6, 3]
]

# defining output levels for difficulty
y = [0, 0, 0, 1, 1, 1, 2, 2, 2]

# training model using gaussian naive bayes
model = GaussianNB()
model.fit(X, y)

# creating question sets for each level
questions = {
    0: [
        ("2 + 2 = ?", "4"),
        ("5 - 1 = ?", "4"),
        ("3 + 3 = ?", "6")
    ],
    1: [
        ("12 * 2 = ?", "24"),
        ("15 - 7 = ?", "8"),
        ("18 / 3 = ?", "6")
    ],
    2: [
        ("(12 * 5) - 10 = ?", "50"),
        ("144 / 12 = ?", "12"),
        ("25 * 6 = ?", "150")
    ]
}

# defining labels and colors for levels
levels = ["EASY", "MEDIUM", "HARD"]
colors = ["#90EE90", "#FFD580", "#FF7F7F"]

# creating main class for quiz interface
class AdaptiveQuizUI:

    # initializing window and variables
    def __init__(self, root):
        self.root = root
        self.root.title("Adaptive AI Quiz System")
        self.root.geometry("400x320")

        self.score = 0
        self.mistakes = 0
        self.current_answer = ""

        # creating label for level display
        self.level_label = tk.Label(root, text="Level: EASY", font=("Arial", 14))
        self.level_label.pack(pady=10)

        # creating label for question display
        self.question_label = tk.Label(root, text="Click Start", font=("Arial", 16))
        self.question_label.pack(pady=10)

        # creating input box for answer
        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=10)

        # creating button for submitting answer
        self.submit_btn = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_btn.pack(pady=5)

        # creating button for next question
        self.next_btn = tk.Button(root, text="Next Question", command=self.next_question)
        self.next_btn.pack(pady=5)

        # creating label for score and mistakes
        self.score_label = tk.Label(root, text="Score: 0 | Mistakes: 0")
        self.score_label.pack(pady=10)

        # creating start button
        self.start_btn = tk.Button(root, text="Start Quiz", command=self.next_question)
        self.start_btn.pack(pady=5)

        # creating quit button with confirmation
        self.quit_btn = tk.Button(root, text="Quit", command=self.confirm_quit)
        self.quit_btn.pack(pady=5)

    # predicting difficulty level using model
    def predict_level(self):
        features = np.array([[self.score, self.mistakes]])
        return int(model.predict(features)[0])

    # updating interface color and level text
    def update_ui(self, level):
        self.root.configure(bg=colors[level])
        self.level_label.config(text="Level: " + levels[level], bg=colors[level])
        self.question_label.config(bg=colors[level])
        self.score_label.config(bg=colors[level])

    # selecting and showing next question
    def next_question(self):
        level = self.predict_level()
        self.update_ui(level)

        q, ans = random.choice(questions[level])
        self.current_answer = ans

        self.question_label.config(text=q)
        self.entry.delete(0, tk.END)

    # checking answer and updating score
    def check_answer(self):
        user_answer = self.entry.get().strip()

        if user_answer == self.current_answer:
            self.score += 1
            messagebox.showinfo("Result", "Correct")
        else:
            self.mistakes += 1
            messagebox.showerror("Result", "Wrong answer shown")

        self.score_label.config(text="Score: " + str(self.score) + " | Mistakes: " + str(self.mistakes))

    # confirming before quitting application
    def confirm_quit(self):
        response = messagebox.askyesno("Exit", "Do you want to quit?")
        if response:
            self.root.destroy()

# running main application
if __name__ == "__main__":
    root = tk.Tk()
    app = AdaptiveQuizUI(root)
    root.mainloop()