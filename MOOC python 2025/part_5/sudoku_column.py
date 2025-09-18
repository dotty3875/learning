"""Please write a function named column_correct(sudoku: list, column_no: int), which takes a two-dimensional array representing a sudoku grid, and an integer referring to a single column, 
as its arguments. Columns are indexed from 0.

The function should return True or False, depending on whether the column is filled in correctly, that is, whether it contains each of the numbers 1 to 9 at most once."""

def column_correct(sudoku: list, column_no: int):
    checkerList = []
    for row in sudoku: # iterates through each row
        if row[column_no] != 0: # as it goes through each row, checks if the same index of each row (effectively checking column) is 0, and if so disregards it 
            checkerList.append(row[column_no]) # adds valid numbers to a list used to check later
    checkerSet = set(checkerList) # creates set from the checkerList, which removes all non-unique integers
    if len(checkerList) == len(checkerSet): # checks if there are any duplicates in the specified row, and if so it's invalid and returns False
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

    print(column_correct(sudoku, 0))