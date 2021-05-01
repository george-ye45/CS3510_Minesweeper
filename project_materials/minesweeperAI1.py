import numpy as np
import random

class AI1():

    def __init__(self, numRows, numCols, numBombs, safeSquare):   
        self.numRows = numRows
        self.numCols = numCols
        self.numBombs = numBombs
        self.safeSquare = safeSquare

    def open_square_format(self, squareToOpen):
        return ("open_square", squareToOpen)

    def submit_final_answer_format(self, listOfBombs):
        return ("final_answer", listOfBombs)

    def subtract_board(self, boardState):
        board_state_copy = boardState.copy()
        for row in range(self.numRows):
            for col in range(self.numCols):
                if board_state_copy[row][col] != 9 and board_state_copy[row][col] > 0:
                    if row + 1 < self.numRows and board_state_copy[row + 1][col] == 9 and board_state_copy[row][col] > 0:
                        board_state_copy[row][col] -= 1
                    if row - 1 >= 0 and board_state_copy[row - 1][col] == 9 and board_state_copy[row][col] > 0:
                        board_state_copy[row][col] -= 1
                    if col + 1 < self.numCols and board_state_copy[row][col + 1] == 9 and board_state_copy[row][col] > 0:
                        board_state_copy[row][col] -= 1
                    if col - 1 >= 0 and board_state_copy[row][col - 1] == 9 and board_state_copy[row][col] > 0:
                        board_state_copy[row][col] -= 1
                    if row + 1 < self.numRows and col + 1 < self.numCols and board_state_copy[row + 1][col + 1] == 9 and board_state_copy[row][col] > 0:
                        board_state_copy[row][col] -= 1
                    if row + 1 < self.numRows and col - 1 >= 0 and board_state_copy[row + 1][col - 1] == 9 and board_state_copy[row][col] > 0:
                        board_state_copy[row][col] -= 1
                    if row - 1 >= 0 and col - 1 >= 0 and board_state_copy[row - 1][col - 1] == 9 and board_state_copy[row][col] > 0:
                        board_state_copy[row][col] -= 1
                    if row - 1 >= 0 and col + 1 < self.numCols and board_state_copy[row - 1][col + 1] == 9 and board_state_copy[row][col] > 0:
                        board_state_copy[row][col] -= 1
        return board_state_copy
    # return the square (r, c) you want to open based on the given boardState
    # the boardState will contain the value (0-8 inclusive) of the square, or -1 if that square is unopened
    # an AI example that returns a random square (r, c) that you want to open

    # TODO: implement a better algorithm
    def performAI(self, boardState):
            # find all the unopened squares
            unopenedSquares = []
            distribution = boardState.copy()
            bombs_found = []
            boardState = self.subtract_board(boardState)
            for row in range(self.numRows):
                for col in range(self.numCols):
                    if boardState[row][col] == 9:
                        bombs_found.append((row, col))
                        distribution[row][col] = 0
                        continue
                    if boardState[row][col] != -1:
                        distribution[row][col] = 0
                        continue
                    if boardState[row][col] == -1:
                        unopenedSquares.append((row, col))
                    total = 0
                    if row + 1 < self.numRows and boardState[row + 1][col] != 9 and boardState[row + 1][col] > 0:
                        total += boardState[row + 1][col]
                    if row - 1 >= 0 and boardState[row - 1][col] != 9 and boardState[row - 1][col] > 0:
                        total += boardState[row - 1][col]
                    if col + 1 < self.numCols and boardState[row][col + 1] != 9 and boardState[row][col + 1] > 0:
                        total += boardState[row][col + 1]
                    if col - 1 >= 0 and boardState[row][col - 1] != 9 and boardState[row][col - 1] > 0:
                        total += boardState[row][col - 1]
                    if row + 1 < self.numRows and col + 1 < self.numCols and boardState[row + 1][col + 1] != 9 and boardState[row + 1][col + 1] > 0:
                        total += boardState[row + 1][col + 1]
                    if row + 1 < self.numRows and col - 1 >= 0 and boardState[row + 1][col - 1] != 9 and boardState[row + 1][col - 1] > 0:
                        total += boardState[row + 1][col - 1]
                    if row - 1 >= 0 and col - 1 >= 0 and boardState[row - 1][col - 1] != 9 and boardState[row - 1][col - 1] > 0:
                        total += boardState[row - 1][col - 1]
                    if row - 1 >= 0 and col + 1 < self.numCols and boardState[row - 1][col + 1] != 9 and boardState[row - 1][col + 1] > 0:
                        total += boardState[row - 1][col + 1]
                    distribution[row][col] = total
            distribution = np.array(distribution)
        
            if len(bombs_found) == self.numBombs:
                # If the number of unopened squares is equal to the number of bombs, all squares must be bombs, and we can submit our answer
                print(f"List of bombs is {bombs_found}")
                return self.submit_final_answer_format(bombs_found)
            else:
                squareToOpen = None
                flat_distribution = distribution.flatten().tolist()
                if sum(flat_distribution) == 0:
                    squareToOpen = random.choice(unopenedSquares)
                else:   
                    normalized_distribution = [ i /sum(flat_distribution) for i in flat_distribution]
                    max_index = np.random.choice(a = len(normalized_distribution), p = normalized_distribution)
                    adjusted_index = np.unravel_index(max_index, distribution.shape)
                    squareToOpen = adjusted_index
            #print(f"Square to open is {squareToOpen}")
            return self.open_square_format(squareToOpen)
