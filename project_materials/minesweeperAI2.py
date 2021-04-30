import numpy as np
import random

class AI2():

    # Define settings upon initialization. Here you can specify
    def __init__(self, numRows, numCols, numBombs, safeSquare):   

        # game variables that can be accessed in any method in the class. For example, to access the number of rows, use "self.numRows" 
        self.numRows = numRows
        self.numCols = numCols
        self.numBombs = numBombs
        self.safeSquare = safeSquare
        self.count = 0
        
    def guarantee_bombs(self, boardState):
        board_state_copy = boardState.copy()
        for row in range(self.numRows):
            for col in range(self.numCols):
                squares = []
                if row + 1 < self.numRows and boardState[row + 1][col] == -1:
                    squares.append((row + 1, col))
                if row - 1 >= 0 and boardState[row - 1][col] == -1:
                    squares.append((row - 1, col))
                if col + 1 < self.numCols and boardState[row][col + 1] == -1:
                    squares.append((row, col + 1))
                if col - 1 >= 0 and boardState[row][col - 1] == -1:
                    squares.append((row, col - 1))
                if row + 1 < self.numRows and col + 1 < self.numCols and boardState[row + 1][col + 1] == -1:
                    squares.append((row + 1, col + 1))
                if row + 1 < self.numRows and col - 1 >= 0 and boardState[row + 1][col - 1] == -1:
                    squares.append((row + 1, col - 1))
                if row - 1 >= 0 and col - 1 >= 0 and boardState[row - 1][col - 1] == -1:
                    squares.append((row - 1, col - 1))
                if row - 1 >= 0 and col + 1 < self.numCols and boardState[row - 1][col + 1] == -1:
                    squares.append((row - 1, col + 1))
                

                if len(squares) == board_state_copy[row][col] and board_state_copy[row][col] != 0:
                    for i in squares:
                        board_state_copy[i[0]][i[1]] = 9
        
        return board_state_copy
                

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

    def removeAroundZero(self, boardState):
        remove = []
        for row in range(self.numRows):
            for col in range(self.numCols):
                if boardState[row][col] == -1:
                    if row + 1 < self.numRows and boardState[row + 1][col] == 0:
                        remove.append((row, col))
                    if row - 1 >=0 and boardState[row - 1][col] == 0:
                        remove.append((row, col))
                    if col + 1 < self.numCols and boardState[row][col + 1] == 0:
                        remove.append((row, col))
                    if col - 1 >=0 and boardState[row][col - 1] == 0:
                        remove.append((row, col))
                    if row + 1 < self.numRows and col + 1 < self.numCols and boardState[row + 1][col + 1] == 0:
                        remove.append((row, col))
                    if row + 1 < self.numRows and col - 1 >=0  and boardState[row + 1][col - 1] == 0:
                        remove.append((row, col))
                    if row - 1 >= 0 and col - 1 >= 0 and boardState[row - 1][col - 1] == 0:
                        remove.append((row, col))
                    if row - 1 >= 0 and col + 1 < self.numCols and boardState[row - 1][col + 1] == 0:
                        remove.append((row, col))
        return remove


    def open_square_format(self, squareToOpen):
        return ("open_square", squareToOpen)

    def submit_final_answer_format(self, listOfBombs):
        return ("final_answer", listOfBombs)
    
    def check_nearby_squares(self, boardState, row, col):
        nearby = []
        if row + 1 < self.numRows:
            nearby.append(boardState[row + 1][col])
        if row - 1 > 0:
            nearby.append(boardState[row - 1][col])
        if col + 1 < self.numCols:
            nearby.append(boardState[row][col + 1])
        if col - 1 > 0:
            nearby.append(boardState[row][col - 1])
        if row + 1 < self.numRows and col + 1 < self.numCols:
            nearby.append(boardState[row + 1][col + 1])
        if row + 1 < self.numRows and col - 1 > 0:
            nearby.append(boardState[row + 1][col - 1])
        if row - 1 > 0 and col - 1 > 0:
            nearby.append(boardState[row - 1][col - 1])
        if row - 1 > 0 and col + 1 < self.numCols:
            nearby.append(boardState[row - 1][col + 1])
        
        return nearby



    # return the square (r, c) you want to open based on the given boardState
    # the boardState will contain the value (0-8 inclusive) of the square, or -1 if that square is unopened
    # an AI example that returns a random square (r, c) that you want to open
    # TODO: implement a better algorithm
    def performAI(self, boardState):
        print(boardState)
        # find all the unopened squares
        unopenedSquares = []
        distribution = boardState.copy()
        bombs_found = []
        found = True
        boardState = self.subtract_board(boardState)
        boardState = self.guarantee_bombs(boardState)


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
            # Otherwise, pick a random square and open it    
            flat_distribution = distribution.flatten()  
            squareToOpen = None
            if sum(flat_distribution) != 0:
                normalized_distribution = [ i /sum(flat_distribution) for i in flat_distribution]
                #max_index = np.random.choice(a = len(normalized_distribution), p = normalized_distribution)
                max_index = normalized_distribution.index(max(normalized_distribution))
                adjusted_index = np.unravel_index(max_index, distribution.shape)
            # squareToOpen = random.choice(unopenedSquares)
                squareToOpen = adjusted_index
            else:
                self.count += 1
                print("ALL ZERO: ", self.count)
                print("BEFORE")
                print(boardState)
                bad = self.removeAroundZero(boardState)
                print("BAD: ", bad)
                #squareToOpen = random.choice(unopenedSquares)
                squareToOpen = random.choice(list(set(unopenedSquares) - set(bad)))
            print(f"Square to open is {squareToOpen}")
            return self.open_square_format(squareToOpen)






    