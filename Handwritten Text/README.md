# Handwritten Text Recognition

The project contained within this folder displays an implementation of recognizing handwritten text. This is achieved through training a linear SVM model on training data convoluted 
with various identifying kernels. The kernels are utilized to detect edges and lines within the 28x28 text images fed to the model. 

Following convolution and training, various functions are implemented in order to make sure that new input data may be preprocessed, convolved in two dimensions, and classified by the
model. Finally, a user interface was created using a front end library PyQT, which enabled the user to input their own drawn text. The user input was then tested through the model and classified 
with an accuracy higher than 85%. 

**Included Files:**

1. App.py - Contains the code for the creation of the front end app, this includes creating a UI, functions for processing the UI's input, and labelling the resulting outputs of the trained model.
2. App.spec - Created from PyInstaller in order to manage the compiling of the final executable.
3. AppUI.ui - Created with PyQT in order to manage signals for the user interface, also contains the general design itself.
4. AppUIPy.py - Contains the python version of the AppUI.ui file, includes instantiations of UI components.
5. PythonImplementation.py - Creates the training model that is used within this project. Includes functions for kernelization of data, alongside the importation of a dataset from EMNIST. The model is exported from here and imported into App.py for user interface use.
6. svmModel.pkl (not included directly) - The model file that is exported from the PythonImplementation.py file. This file must be downloaded from the drive link included below as its file size exceeds that allowed in GitHub.

**Instructions for Running:**

1. 
