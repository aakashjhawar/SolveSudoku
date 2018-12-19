import cv2
import sys
from SudokuExtractor import extract_sudoku
from NumberExtractor import extract_number
from SolveSudoku import sudoku_solver

def display_sudoku(sudoku):
    for i in range(9):
        for j in range(9):
            cell = sudoku[i][j]
            if cell == 0 or isinstance(cell, set):
                output('.')
            else:
                output(cell)
            if (j + 1) % 3 == 0 and j < 8:
                output(' |')

            if j != 8:
                output('  ')
        output('\n')
        if (i + 1) % 3 == 0 and i < 8:
            output("--------+----------+---------\n")

def main(image_path):
    image = extract_sudoku(image_path)
    try:
        cv2.imshow('Sudoku', image)
    except:
        print('ERROR')
    grid = extract_number(image)
    print('Sudoku:')
    display_sudoku(grid.tolist())
    solution = sudoku_solver(grid)
    print('Solution:')
#    print(solution)  
    display_sudoku(solution.tolist())
        
if __name__ == '__main__':
#    image_path = 'images/sudoku.jpg'
#    main(image_path)
    try:
        main(image_path = sys.argv[1])
    except:             #    except IndexError:
        fmt = 'usage: {} image_path'
        print(fmt.format(__file__.split('/')[-1]))
        print('[ERROR]: Image not found')
