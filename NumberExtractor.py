import numpy as np
import cv2
import matplotlib.pyplot as plt
import numpy as np
from keras.models import model_from_json

# Load the saved model
json_file = open('models/model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("models/model.h5")
print("Loaded saved model from disk.")
 
# evaluate loaded model on test data
def identify_number(image):
    image_resize = cv2.resize(image, (28,28))    # For plt.imshow
    image_resize_2 = image_resize.reshape(1,1,28,28)    # For input to model.predict_classes
#    cv2.imshow('number', image_test_1)
    loaded_model_pred = loaded_model.predict_classes(image_resize_2 , verbose = 0)
#    print('Prediction of loaded_model: {}'.format(loaded_model_pred[0]))
    return loaded_model_pred[0]

def extract_number(sudoku):
    sudoku = cv2.resize(sudoku, (450,450))
#    cv2.imshow('sudoku', sudoku)

    # split sudoku
    grid = np.zeros([9,9])
    for i in range(9):
        for j in range(9):
#            image = sudoku[i*50+3:(i+1)*50-3,j*50+3:(j+1)*50-3]
            image = sudoku[i*50:(i+1)*50,j*50:(j+1)*50]
#            filename = "images/sudoku/file_%d_%d.jpg"%(i, j)
#            cv2.imwrite(filename, image)
            if image.sum() > 25000:
                grid[i][j] = identify_number(image)
            else:
                grid[i][j] = 0
    return grid.astype(int)




