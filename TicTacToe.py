from random import randint


def Welcome_Message():

    name = input("Hello! Please enter your name: ")
    print("Welcome to TicTacToe {}!".format(name))
    game_choice = input("1 for SinglePlayer \n2 for TwoPlayer \nEnter: ")
    while int(game_choice) < 1 or int(game_choice) > 2:
        print("Invalid choice!")
        game_choice = input("1 for SinglePlayer \n2 for TwoPlayer \n")


if __name__ == "__main__":
    Welcome_Message()
