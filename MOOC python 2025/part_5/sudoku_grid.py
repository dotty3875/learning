"""Please write a function named sudoku_grid_correct(sudoku: list), which takes a two-dimensional array representing a sudoku grid as its argument. The function should use the functions from the three previous exercises to determine whether the complete sudoku grid is filled in correctly. Copy the functions from the exercises above into your Python code file for this exercise.

The function should check each of the nine rows, columns and 3 by 3 blocks in the grid. If all contain each of the numbers 1 to 9 at most once, the function returns True. If a single one is filled in incorrectly, the function returns False.

The image of a sudoku grid above these exercises has the nine blocks within the grid indicated with thicker borders. These are the blocks the function should check, and they begin at the indexes (0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3) and (6, 6)."""

def row_correct(sudoku: list):
    checkerList = []
    validTotal = 0 # checker variable for valid rows
    for row in sudoku: # iterates through each row
        for i in row: # iterates through each index of each row
            if i != 0: # if it's 0, disregard it. adds other valid numbers to a list used to check for uniqueness of row
                checkerList.append(i) 
        if len(checkerList) == len(set(checkerList)): # checks the list against a set of itself; checks if there are any duplicates
            validTotal += 1
        checkerList = [] # resets to an empty list for the next row's check
    if validTotal == 9: # if all 9 rows are valid, returns True indicating all rows are unique and valid for sudoku
        return True
    return False

def column_correct(sudoku: list):
    checkerList = []
    validTotal = 0 # checker variable for valid columns
    for i in range(9): # creates a tracker variable for use as a column checker
        for row in sudoku:
            if row[i] != 0: # as it goes through each row, checks if the same index of each row (effectively checking column) is 0, and if so disregards it 
                checkerList.append(row[i]) # adds other valid numbers to a list used to check for uniqueness of column
        if len(checkerList) == len(set(checkerList)):
            validTotal += 1
        checkerList = [] # resets to an empty list for the next row's check
    if validTotal == 9: # if all 9 columns are valid, returns True indicating all columns are unique and valid for sudoku
        return True
    return False

def block_correct(sudoku: list):
    list = []
    for y in range(3): # y for vertical block checking
        for x in range(3): # x for horizontal block checking
            for row in range(3): 
                for column in range(3): # row and column together are used to create a 3x3 block to check for validity
                    if sudoku[row + (y * 3)][column + (x * 3)] != 0: # y & x * 2 are used to check for valid blocks beginning at the indexes (0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3) and (6, 6)
                        list.append(sudoku[row + (y * 3)][column + (x * 3)]) # appends each item to list to check for uniqueness as set in next step
                    if len(list) != len(set(list)): # if any blocks are invalid, immedaitely returns False and ends function 
                        return False
            list = [] # resets the block list to 0 after each block
    return True 

def sudoku_grid_correct(sudoku: list):
    if row_correct(sudoku) == True and column_correct(sudoku) == True and block_correct(sudoku) == True: # if all 3 functions that check for validity pass True, then the whole sudoku grid must be valid and should return True
        return True
    return False

if __name__ == "__main__":
    sudoku = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1],
  ]

    print(sudoku_grid_correct(sudoku))