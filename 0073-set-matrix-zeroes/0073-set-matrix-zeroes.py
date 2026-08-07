class Solution:
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # Step 1: Check if first row has zero
        for j in range(cols):
            if matrix[0][j] == 0:
                first_row_zero = True

        # Step 1: Check if first column has zero
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col_zero = True

        # Step 2: Mark zeros in first row and first column
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0       # mark row
                    matrix[0][j] = 0       # mark column

        # Step 3: Set zeros using marks
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Step 4: Handle first row
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0

        # Step 4: Handle first column
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0