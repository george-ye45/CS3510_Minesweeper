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

    def check_high_prob(self, boardState):
        board_state_copy = boardState.copy()
        highest_prob = 0
        highest_prob_list = []
        for row in range(self.numRows):
            for col in range(self.numCols):
                if (boardState[row][col] > 0 and boardState[row][col] < 9):
                    unopened_list = []
                    if row + 1 < self.numRows and boardState[row + 1][col] == -1:
                        unopened_list.append((row + 1, col))
                    if row - 1 >= 0 and boardState[row - 1][col] == -1:
                        unopened_list.append((row - 1, col))
                    if col + 1 < self.numCols and boardState[row][col + 1] == -1:
                        unopened_list.append((row, col + 1))
                    if col - 1 >= 0 and boardState[row][col - 1] == -1:
                        unopened_list.append((row, col - 1))
                    if row + 1 < self.numRows and col + 1 < self.numCols and boardState[row + 1][col + 1] == -1:
                        unopened_list.append((row + 1, col + 1))
                    if row + 1 < self.numRows and col - 1 >= 0 and boardState[row + 1][col - 1] == -1:
                        unopened_list.append((row + 1, col - 1))
                    if row - 1 >= 0 and col - 1 >= 0 and boardState[row - 1][col - 1] == -1:
                        unopened_list.append((row - 1, col - 1))
                    if row - 1 >= 0 and col + 1 < self.numCols and boardState[row - 1][col + 1] == -1:
                        unopened_list.append((row - 1, col + 1))
                    if len(unopened_list) != 0:
                        curr_prob = boardState[row][col]/len(unopened_list)
                    else:
                        curr_prob = 0.0
                    if curr_prob >= .50 and curr_prob > highest_prob and curr_prob < 1:
                        highest_prob = curr_prob
                        highest_prob_list = unopened_list

        if highest_prob >= .50:
            return True, highest_prob_list
        else:
            return False, highest_prob_list

    def guarantee_bombs(self, boardState, bombsfound):
        board_state_copy = boardState.copy()
        found = False
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
                        if board_state_copy[i[0]][i[1]] != 9 and (i[0], i[1]) not in bombsfound:
                            found = True
                            bombsfound.append(i)
                            if i[0] + 1 < self.numRows and 0 < boardState[i[0] + 1][i[1]] < 9:
                                board_state_copy[i[0] + 1][i[1]] -= 1
                            if i[0] - 1 >= 0 and 0 < boardState[i[0] - 1][i[1]] < 9:
                                board_state_copy[i[0] - 1][i[1]] -= 1
                            if i[1] + 1 < self.numCols and 0 < boardState[i[0]][i[1] + 1] < 9:
                                board_state_copy[i[0]][i[1] + 1] -= 1
                            if i[1] - 1 >= 0 and 0 < boardState[i[0]][i[1] - 1] < 9:
                                board_state_copy[i[0]][i[1] - 1] -= 1
                            if i[0] + 1 < self.numRows and i[1] + 1 < self.numCols and 0 < boardState[i[0] + 1][i[1] + 1] < 9:
                                board_state_copy[i[0] + 1][i[1] + 1] -= 1
                            if i[0] + 1 < self.numRows and i[1] - 1 >= 0 and 0 < boardState[i[0] + 1][i[1] - 1] < 9:
                                board_state_copy[i[0] + 1][i[1] - 1] -= 1
                            if i[0] - 1 >= 0 and i[1] - 1 >= 0 and 0 < boardState[i[0] - 1][i[1] - 1] < 9:
                                board_state_copy[i[0] - 1][i[1] - 1] -= 1
                            if i[0] - 1 >= 0 and i[1] + 1 < self.numCols and 0 < boardState[i[0] - 1][i[1] + 1] < 9:
                                board_state_copy[i[0] - 1][i[1] + 1] -= 1
                            board_state_copy[i[0]][i[1]] = 9
                            print("guarantee found")
        return board_state_copy, found, bombsfound
                

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
        if row - 1 >= 0:
            nearby.append(boardState[row - 1][col])
        if col + 1 < self.numCols:
            nearby.append(boardState[row][col + 1])
        if col - 1 >= 0:
            nearby.append(boardState[row][col - 1])
        if row + 1 < self.numRows and col + 1 < self.numCols:
            nearby.append(boardState[row + 1][col + 1])
        if row + 1 < self.numRows and col - 1 >= 0:
            nearby.append(boardState[row + 1][col - 1])
        if row - 1 >= 0 and col - 1 >= 0:
            nearby.append(boardState[row - 1][col - 1])
        if row - 1 >= 0 and col + 1 < self.numCols:
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
        for row in range(self.numRows):
            for col in range(self.numCols):
                if boardState[row][col] == 9:
                    bombs_found.append((row, col))
                    distribution[row][col] = 0
        found = True
        boardState = self.subtract_board(boardState)
        while found:
            boardState, found, bombs_found = self.guarantee_bombs(boardState, bombs_found)
        all_negative = []

        for row in range(self.numRows):
            for col in range(self.numCols):
                if boardState[row][col] != -1:
                    distribution[row][col] = 0
                    continue
                if boardState[row][col] == -1:
                    nearby = self.check_nearby_squares(boardState, row, col)
                    if 0 in nearby:
                        distribution[row][col] = 0
                        continue
                    unopenedSquares.append((row, col))
                    is_neg = True
                    for i in nearby:
                        if i != -1:
                            is_neg = False
                            break
                    if is_neg:
                        all_negative.append((row, col))
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
            flat_distribution = distribution.flatten().tolist()
            squareToOpen = None
            highProb, list_to_choose = self.check_high_prob(boardState)
            if highProb:
                #print("HIGH PROB")
                squareToOpen = random.choice(list_to_choose)
            elif sum(flat_distribution) != 0:
                #print("POLICY")
                max_index = flat_distribution.index(max(flat_distribution))
                adjusted_index = np.unravel_index(max_index, distribution.shape)
                squareToOpen = adjusted_index
            else:
                self.count += 1
                print("ALL ZERO: ", self.count)
                if len(all_negative) != 0:
                    print("HERE in neg")
                    squareToOpen = random.choice(all_negative)
                else:
                    bad = self.removeAroundZero(boardState)
                    squareToOpen = random.choice(list(set(unopenedSquares) - set(bad)))
            print(f"Square to open is {squareToOpen}")
            return self.open_square_format(squareToOpen)






    