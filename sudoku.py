import cv2
import sys
from SudokuExtractor import extract_sudoku
from NumberExtractor import extract_number
from SolveSudoku import sudoku_solver

def main(image_path):
    image = extract_sudoku(image_path)
    try:
        cv2.imshow('Sudoku', image)
    except:
        print('ERROR')
    grid = extract_number(image)
    print(grid)
    solution = sudoku_solver(grid)
    solution = solution.astype(int) 
    print('Solution')
    print(solution)    
    
    
    
if __name__ == '__main__':
#    image_path = 'images/sudoku2.jpg'
#    main(image_path)
    try:
        main(image_path = sys.argv[1])
    except:             #    except IndexError:
        fmt = 'usage: {} image_path'
        print(fmt.format(__file__.split('/')[-1]))
        print('[ERROR]: Image not found')
