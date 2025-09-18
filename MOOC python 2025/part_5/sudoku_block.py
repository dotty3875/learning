"""Please write a function named block_correct(sudoku: list, row_no: int, column_no: int), which takes a two-dimensional array representing a sudoku grid, and two integers referring to the row and column indexes of a single square, as its arguments. Rows and columns are indexed from 0.

The function should return True or False depending on whether the 3 by 3 block to the right and down from the given indexes is filled in correctly. That is, whether the block contains each of the numbers 1 to 9 at most once.

Notice that this function does not strictly follow the rules of sudoku. In a real game of sudoku there are only 9 blocks to check, and these are located at indexes (0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3) and (6, 6). Such restrictions on indexes should not be implemented here."""

def block_correct(sudoku: list, row_no: int, column_no: int):
    checkerList = []
    for row in range(3): # loops 3 times for the sake of the rows
        for column in range(3): # loops 3 times for the sake of the columns
            if sudoku[row_no + row][column_no + column] != 0: # sudoku[row_no + row] starts it at the specified row_no parameter and then adds + 1 for each of the 3 loops - which effectively lets us start at the specified row and then + 2 sequental rows required to create the first part of the block. the sudoku[column_no + column] does the same thing but for each column of each specified row (running 9 times to create a full block)
                checkerList.append(sudoku[row_no + row][column_no + column]) # appends each non-0 index to a checkerList 
    checkerSet = set(checkerList) # creates a set out of the checkerList to check for unique integers
    if len(checkerList) == len(checkerSet): # checks if the len of checkerList is the same as checkerSet - which would tell us if there were any duplicated numbers in that block which would invalidate the sudoku grid and returns false
        return True
    else:
        return False


if __name__ == "__main__":
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(block_correct(sudoku, 1, 2))