#Hangman in python
words = ("Marina", "Mariner", "Marionette", "Marketplace", "Marksman", "Marmalade", "Maroon", "Marquee", "Marquis", "Marrow", "Marsh", "Marshal", "Martyr", "Participate", "Partition", "Partner", "Pass", "Paste", "Pasture", "Pat", "Patch", "Patent", "Patrol", "Patronize", "Patter", "Pattern", "Pause", "Pave", "Pawn", "Pay", "Peak", "Peal", "Peck", "Pedal", "Peddle", "Peek", "Peel", "Peep", "Peer", "Peg", "Pelt", "Pen", "Penalize", "Penetrate", "Penitence", "Penlight", "Pension", "People", "Pepper", "Perceive", "Perch", "Percolate", "Perforate", "Fast", "Fatal", "Favorable", "Fearful", "Fearless", "Feasible", "Feathered", "Featureless", "Febrile", "Fecund", "Feeble", "Feisty", "Felicitous", "Feline", "Felonious", "Female", "Feral", "Ferocious", "Fervent", "Festive", "Marvel", "Mascot", "Mash", "Mask", "Mason", "Masquerade", "Mass", "Massacre", "Massage", "Mast", "Masterpiece", "Mastery", "Mastication", "Mat", "Match", "Material", "Maternal", "Mathematician", "Matinee", "Matriarch", "Matrimony", "Matrix", "Matting", "Mattress", "Maturity", "Mausoleum", "Maverick", "Maxilla", "Maximum", "Mayhem", "Mayor", "Maze", "Meadow", "Meal", "Meander", "Meaning", "Meanness", "Meantime", "Measles", "Measurement", "Perform", "Perfume", "Perish", "Perjure", "Permeate", "Permit", "Perpetrate", "Perpetuate", "Perplex", "Persecute", "Persevere", "Persist", "Persuade", "Pertain", "Perturb", "Peruse", "Pester", "Petition", "Petrify", "Phase", "Phone", "Photograph", "Phrase", "Pick", "Pickax", "Pickle", "Picture", "Pierce", "Piggyback", "Pile", "Pilfer", "Pilgrim", "Pill", "Pillage", "Pillar", "Pilot", "Pin", "Pinch", "Pine", "Pioneer", "Fetid", "Feudal", "Feverish", "Few", "Fickle", "Fictional", "Fictitious", "Fierce", "Fiery", "Filthy", "Final", "Financial", "Fine", "Finicky", "Finite", "Firm", "First", "Fiscal", "Fit", "Fixed"))
import random

#dictionary of key:()
hangman_art = { 0: ("   ",
                    "   ",
                    "   ",),
                1: (" o ",
                    "   ",
                    "   ",),
                2: (" o ",
                    " | ",
                    "   ",),
                3: (" o ",
                    "/| ",
                    "   ",),
                4: (" o ",
                    "/|\\ ",
                    "   ",),
                5: (" o ",
                    "/|\\ ",
                    "/  ",),
                6: (" o ",
                    "/|\\ ",
                    "/ \\",)}



def display_man(wrong_guesses):
    print("**********")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("**********")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"]  *  len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ")

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} already guessed")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOOSE!")
            is_running = False

if __name__ == "__main__":
    main()
