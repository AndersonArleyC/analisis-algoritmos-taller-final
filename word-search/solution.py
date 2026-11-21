from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """Return whether word can be formed by an orthogonal simple path."""
        rows = len(board)
        columns = len(board[0])

        def search(row: int, column: int, index: int) -> bool:
            if board[row][column] != word[index]:
                return False
            if index == len(word) - 1:
                return True

            letter = board[row][column]
            board[row][column] = "#"

            for row_step, column_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_row = row + row_step
                next_column = column + column_step
                if (
                    0 <= next_row < rows
                    and 0 <= next_column < columns
                    and search(next_row, next_column, index + 1)
                ):
                    board[row][column] = letter
                    return True

            board[row][column] = letter
            return False

        for row in range(rows):
            for column in range(columns):
                if search(row, column, 0):
                    return True

        return False
