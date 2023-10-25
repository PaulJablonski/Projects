**Handwritten Text Project Description**

The project contained within this folder displays an implementation of recognizing handwritten text. This is achieved through training a linear SVM model on training data convoluted 
with various identifying kernels. The kernels are utilized to detect edges and lines within the 28x28 text images fed to the model. 

Following convolution and training, various functions are implemented in order to make sure that new input data may be preprocessed, convolved in two dimensions, and classified by the
model. Finally, a user interface was created using a front end library PyQT, which enabled the user to input their own drawn text, which was then tested through the model and classified 
with an accuracy higher than 85%. 

Note: The svmModel.pkl file that contains the trained model was not included in this directory as it was too large of a file to upload to GitHub's services. This should not 
impact the performance of the testable application, and may also be generated locally through simply running the PythonImplementation.py file in a local environment.

**Instructions for Running**

1. 
