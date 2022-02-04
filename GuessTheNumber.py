import math
import random
import sys


def won_the_game():
    print("\n\nCongratulations for winning the game!!!!! "
          "Hope You Liked The Game. Please Play it again!!!")
    sys.exit()


class NumberGuessGame:
    def __init__(self):
        self.lower = int(input("Enter the lower Bound : "))
        self.upper = int(input("Enter the Upper Bound : "))
        self.number = random.randint(self.lower, self.upper)
        self.number_of_tries = round(math.log(self.upper - self.lower + 1, 2))

    def start_game(self):
        print(f"You have only {self.number_of_tries} tries to guess the number !!!!!"
              f"\nTry your best to guess  the number !!!!! \n\n")
        input("Press Enter to Start The GAME !!!\n\n\n")
        for i in range(1, self.number_of_tries + 1):
            guess = int(input("Enter your guess : "))
            if guess == self.number:
                print("Congratulations !!!! \nYou have guessed it right !!"
                      f"The number is {self.number}")
                won_the_game()
            else:
                print("Woh !! No !! Your guess is wrong !!")
                if guess > self.number:
                    print("Your Guess is too high!!")
                if guess < self.number:
                    print("Your Guess is too small!!")
                print(f"You have only {self.number_of_tries - i} tries left.")
            print("\n\n")
        print("OOh!! No!!! You have used all of your tries!!"
              "YOU LOST"
              f"The number is {self.number}")
