# Gaussian Naive Bayes was used to create an adaptive quiz system that varies the difficulty level according to the user performance. 
# The system also dynamically picked easy, medium and hard questions based on score and error patterns, to provide personalized learning.

import random
import numpy as np
from sklearn.naive_bayes import GaussianNB

# importing required libraries for random selection, array handling, and classification
# creating dataset for training difficulty prediction model
X = [
    [0, 0], [1, 0], [2, 0],
    [2, 1], [3, 1], [4, 1],
    [4, 2], [5, 2], [6, 3]
]

# defining target labels for difficulty levels
y = [0, 0, 0, 1, 1, 1, 2, 2, 2]

# initializing Gaussian Naive Bayes model
model = GaussianNB()

# fitting model with training data
model.fit(X, y)

# creating question bank for different difficulty levels
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

# defining readable labels for difficulty levels
levels = ["EASY", "MEDIUM", "HARD"]

# creating adaptive quiz system class
class AdaptiveQuiz:

    # initializing score and mistake counters
    def __init__(self):
        self.score = 0
        self.mistakes = 0

    # predicting difficulty level based on performance
    def predict_level(self):
        features = np.array([[self.score, self.mistakes]])
        return int(model.predict(features)[0])

    # selecting and displaying question based on predicted level
    def ask_question(self):
        level = self.predict_level()
        q, ans = random.choice(questions[level])

        print(f"\n[{levels[level]}] {q}")
        user_answer = input("answer: ").strip()

        # checking correctness of answer
        if user_answer == ans:
            self.score += 1
            print("Correct")
        else:
            self.mistakes += 1
            print(f"Wrong Correct answer is {ans}")

    # running quiz until user stops
    def start(self):
        print("Adaptive AI Quiz Naive Bayes")
        print("Type exit anytime to quit")

        # looping through questions continuously
        while True:
            self.ask_question()

            cont = input("Continue y or n: ").lower()
            if cont != 'y':
                break

        # displaying final results
        print("Final Score:", self.score)
        print("Final Mistakes:", self.mistakes)

# running main program
if __name__ == "__main__":
    quiz = AdaptiveQuiz()
    quiz.start()