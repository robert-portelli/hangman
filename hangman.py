# hangman.py
"""
A simple hangman cli game
"""

import random
import pathlib
import tomllib


WORDS_n_STATES_PATH = pathlib.Path(__file__).parent / "HANGMAN.toml"


def main():
    word = pre_process(WORDS_n_STATES_PATH)

    main_process(word)


def pre_process(path):
    """
    return a random word from the list as a string
    """
    words = tomllib.loads(path.read_text())["words"]["word_list"]
    return random.sample(words, k=1)[0]  # take the string out of the list

def main_process(word):
    guessed_letters = []
    attempts_remaining = 6
