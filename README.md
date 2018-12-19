# SolveSudoku

Extract and solv sudoku from image.

## Getting Started

How to use: 
----------
    git clone https://github.com/aakashjhawar/SolveSudoku.git
    cd SolveSudoku
    python3 sudoku.py <path/to/input_image>
    
### Prerequisites

- Python 3.5
- OpenCV
```
sudo apt-get install python-opencv
```
### Algorithm

### Working 
Working:
-------
Input image of Sudoku
![Input image of sudoku](https://github.com/aakashjhawar/SolveSudoku/blob/master/images/sudoku.jpg)

Image of Sudoku after thresholding
![Threshold image of sudoku](https://github.com/aakashjhawar/SolveSudoku/blob/master/images/threshold.jpg)

Contour corners of Sudoku
![Contour of sudoku](https://github.com/aakashjhawar/SolveSudoku/blob/master/images/contour.jpg)
<br>
Final output of ExtractSudoku 
![Final image of sudoku](https://github.com/aakashjhawar/SolveSudoku/blob/master/images/final.jpg)
