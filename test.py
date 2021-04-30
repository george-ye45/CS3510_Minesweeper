    def subtract_board(self, boardState):
        board_state_copy = boardState.copy()
        for row in range(self.numRows):
            for col in range(self.numCols):
                if board_state_copy[row][col] != 9 and board_state_copy[row][col] > 0:
                    if row + 1 < self.numRows and board_state_copy[row + 1][col] == 9 and board_state_copy[row][col] > 0:
                        board_state_copy[row][col] -= 1
                    if row - 1 > 0 and board_state_copy[row - 1][col] == 9 and board_state_copy[row][col] > 0:
                        board_state_copy[row][col] -= 1
                    if col + 1 < self.numCols and board_state_copy[row][col + 1] == 9 and board_state_copy[row][col] > 0:
                        board_state_copy[row][col] -= 1
                    if col - 1 > 0 and board_state_copy[row][col - 1] == 9 and board_state_copy[row][col] > 0:
                        board_state_copy[row][col] -= 1
                    if row + 1 < self.numRows and col + 1 < self.numCols and board_state_copy[row + 1][col + 1] == 9 and board_state_copy[row][col] > 0:
                        board_state_copy[row][col] -= 1
                    if row + 1 < self.numRows and col - 1 > 0 and board_state_copy[row + 1][col - 1] == 9 and board_state_copy[row][col] > 0:
                        board_state_copy[row][col] -= 1
                    if row - 1 > 0 and col - 1 > 0 and board_state_copy[row - 1][col - 1] == 9 and board_state_copy[row][col] > 0:
                        board_state_copy[row][col] -= 1
                    if row - 1 > 0 and col + 1 < self.numCols and board_state_copy[row - 1][col + 1] == 9 and board_state_copy[row][col] > 0:
                        board_state_copy[row][col] -= 1
        return board_state_copy