from random import randint


def Welcome_Message():

    name = input("Hello! Please enter your name: ")
    print("Welcome to TicTacToe {}!".format(name))
    game_choice = input("1 for SinglePlayer \n2 for TwoPlayer \nEnter: ")
    while int(game_choice) < 1 or int(game_choice) > 2:
        print("Invalid choice!")
        game_choice = input("1 for SinglePlayer \n2 for TwoPlayer \n")


class GameBoard:

    def __init__(self, board):
        self.board = board

    def getLettersToNumbers(self):
        conv = {"A": 0, "B": 1, "C": 2}
        return conv

    def printBoard(self):
        print("  A B C")
        print("  +-+-+")
        rowNum = 1
        for row in self.board:
            print("%d|%s|" % (rowNum, "|".join(row)))
            rowNum += 1


class TicTacToe:
    def __init__(self, board):
        self.board = board

    def compChoice(self):
        self.x_ran = randint(0, 2)
        self.y_ran = randint(0, 2)

        while self.board[self.x_ran][self.y_ran] != " ":
            self.x_ran = randint(0, 2)
            self.y_ran = randint(0, 2)

        print(self.x_ran, self.y_ran)
        print(type(self.board[self.x_ran][self.y_ran]))
        self.board[self.x_ran][self.y_ran] = str("O")

        return self.board

    def playerOne(self, board):
        try:
            y_play1 = input("Enter column number: ")
            while y_play1 not in ["ABC"]:
                y_play1 = input("Enter column number: ")
            x_play1 = input("Enter row number: ")
            while x_play1 not in ["123"]:
                x_play1 = input("Enter row number: ")

        except KeyError or ValueError:
            print("Not a valid input")
            return self.playerOne()

        return int(x_play1) - 1, GameBoard.getLettersToNumbers()[y_play1]


test = GameBoard([" " * 3 for i in range(3)])

if __name__ == "__main__":
    # Welcome_Message()
    GameBoard.printBoard(test)
    TicTacToe.compChoice(test)
