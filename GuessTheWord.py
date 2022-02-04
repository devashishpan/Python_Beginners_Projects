import math
import random
import sys
import urllib.request


def won_the_game():
    print("\n\nCongratulations for winning the game!!!!! "
          "Hope You Liked The Game. Please Play it again!!!")
    sys.exit()


def rules():
    print('''
        RULES OF THE GAME ARE SIMPLE :-
        1 -> YOU WILL BE GIVEN A NUMBER OF CHANCES ACCORDING TO THE LENGTH AND DIFFICULTY OF THE WORD.
        2 -> YOU WILL ONLY NEED TO GUESS THE ALPHABETS CONTAINED IN THE WORD.
        3 -> AS SOON AS YOU GUESS THE CORRECT ALPHABET, IT WILL GET DISPLAYED ON ITS POSITION IN THE WORD.
        4 -> COMPLETE THE WORD BY GUESSING ALL CORRECT ALPHABETS AND COMPLETE THE WORD TO WIN THE GAME!!!!
    ''')


class WordGuessingGame:
    def __init__(self):
        self.response = urllib.request.urlopen(
            'http://random-word-api.herokuapp.com/word?number=10&swear=0'
        ).read().decode("utf-8")
        self.word_db = list(map(lambda x: x.strip('""'), self.response.strip('][').split(',')))
        self.word = self.word_db[random.randint(1, 10)]
        self.tries = []
        self.set_word = set(self.word)
        self.chances = len(self.set_word) + round(math.log2(len(self.word))) + 3

    def start_game(self):
        rules()
        i = 0
        while i <= self.chances-1:
            print(f'\nWORD -> {"".join(list(map(lambda x: f" {x} " if x in self.tries else " _ ", self.word)))}')
            print(f'You have {self.chances - i} Chances left!!!!!')
            guess = input('Guess a character that is present in the Word : ')
            if guess in self.word:
                self.tries.append(guess)
            if set(self.tries) == self.set_word:
                print(f"YOU GUESS IT CORRECTLY.  THE WORD IS {self.word}")
                won_the_game()
            i += 1
        print("OOh!! No!!! You have used all of your tries!!"
              "\nYOU LOST\n"
              f"The word is {self.word}")

