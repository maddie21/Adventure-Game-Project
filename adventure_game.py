import random
import time


def displayIntro():
    print("It is the end of a long year of battling space criminals!")
    print("you come to crossroads on your trip home, one path leads home")
    print("where you will be handsomly rewarded for a job well done")
    print("and the other leads through a infinity loop into time continuum")
    print()


def choosePath():
    path = ""
    while path != "1" and path != "2":  # input validation
        path = input("Which path will you choose? (1 or 2): ")
    return path


def checkPath(chosenPath):
    print("You head down the path")
    time.sleep(2)
    print("there's an planet nearby that looks familiar, must be a good sign")
    time.sleep(2)
    print("But your radar picks up some transmission...")
    print()
    time.sleep(2)

    correctPath = random.randint(1, 2)

    if chosenPath == str(correctPath):
        print("That transmission was from the comms of your defence network!")
        print("Welcome home!")
    else:
        print("An extremely powerful singularity loop draws you into it")
        print("causing all of the ondoard comuputers to fail")
        print("and your are sent into the continuum.")


def playAgain():
    answer = "yes"
    while answer == "yes" or answer == "y":
        displayIntro()
        choice = choosePath()
        checkPath(choice)  # choice is equal to "1" or "2"
        answer = input("Do you want to play again? (yes or y to continue): ")
playAgain()