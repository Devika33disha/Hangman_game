import random

class Hangman:
    def __init__(self):
        self.words = ["python", "leetcode", "college", "project", "object", "program"]
        self.word = random.choice(self.words)
        self.display = ["_"] * len(self.word)
        self.lives = 6
        self.guessed_letters = set()

    def show_state(self):
        print("\nWord: ", " ".join(self.display))
        print("Lives left:", self.lives)
        print("Guessed letters:", ", ".join(sorted(self.guessed_letters)) if self.guessed_letters else "None")

    def guess_letter(self, letter):
        if letter in self.guessed_letters:
            print("You already guessed that letter.")
            return

        self.guessed_letters.add(letter)

        if letter in self.word:
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.display[i] = letter
            print("Correct guess!")
        else:
            self.lives -= 1
            print("Wrong guess!")

    def is_won(self):
        return "_" not in self.display

    def is_lost(self):
        return self.lives == 0

    def play(self):
        print("Welcome to Hangman!")
        while not self.is_won() and not self.is_lost():
            self.show_state()
            letter = input("Enter a letter: ").lower()

            if len(letter) != 1 or not letter.isalpha():
                print("Please enter only one valid letter.")
                continue

            self.guess_letter(letter)

        self.show_state()

        if self.is_won():
            print("\nYou won! The word was:", self.word)
        else:
            print("\nYou lost! The word was:", self.word)


game = Hangman()
game.play()