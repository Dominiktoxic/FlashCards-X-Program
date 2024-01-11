import os

class Flashcards:
    def __init__(self):
        self.flashfile = "flashcards.card"
        self.flashcards = {"Lubisz to?": "Do you like it?"}
        if self.flashfile in os.listdir():
            with open(self.flashfile, "r") as f:
                for line in f.readlines():
                    original, translation = line.split("|")
                    translation, x = translation.split("\n")
                    self.flashcards[original] = translation
        else:
            with open(self.flashfile, "x") as f:
                pass
    
    def add_flashcard(self, name, card):
        self.flashcards[name] = card