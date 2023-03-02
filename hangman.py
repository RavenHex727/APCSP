import nltk
nltk.download('words')
from nltk.corpus import words
word_list = words.words()
import random


def get_unknown_word(guessed_letters, word):
    unknown_word = ""

    for letter in word:
        if letter.lower() in guessed_letters or letter.upper() in guessed_letters:
            unknown_word += " " + letter + " "

        else:
            unknown_word += " _ "

    return unknown_word


def print_guessed_letters(guessed_letters):
    if len(guessed_letters) == 0:
        return "You have no guessed any letters yet"

    elif len(guessed_letters) == 1:
        return f"You have guessed the letter {guessed_letters[0]}"

    else:
        return_string = "You have guessed letters "

        for letter in guessed_letters:
            if letter != guessed_letters[-1]:
                return_string += letter + ", "

            else:
                return_string += "and " + letter

        return return_string


num_lives = 5 #int(input("How many wrong answers do you want to give yourself? "))
word = random.choice(word_list)
guessed_letters = []

while num_lives >= 0 and "_" in get_unknown_word(guessed_letters, word):
    print(get_unknown_word(guessed_letters, word))
    print(print_guessed_letters(guessed_letters))
    print(f"You can guess {num_lives} words incorrectly")
    guessed_letter = input(f"What letter do you think is in the word?")

    while guessed_letter in guessed_letters:
        guessed_letter = input(f"You already geussed that letter. Choose another letter to guess ")

    guessed_letters.append(guessed_letter)

    if guessed_letter in word:
        print(f"The letter {guessed_letter} was in the hidden word!\n")

    else:
        print(f"The letter {guessed_letter} was not in the word\n")
        num_lives -= 1


if num_lives >= 0 and "_" not in get_unknown_word(guessed_letters, word):
    print("Congratulations! You guessed the word correctly!")

else:
    print(f"Unfortunately, you didn't guess the word correctly. The word was {word}. Better luck next time!")
