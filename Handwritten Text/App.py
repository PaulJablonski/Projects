import streamlit as st
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import io
import gzip
import numpy as np
import joblib

from PythonImplementation import kernelizeMass

# Import model from joblib
svmModel = joblib.load('svmModel.pkl')
with gzip.open('svmModel.pkl.gz', 'wb') as f:
  f.write(gzip.compress(open('svmModel.pkl', 'rb').read()))

# Preprocess image
def preprocess(image):
    grayscale = ImageOps.grayscale(image)
    resized = grayscale.resize((28,28))
    imageArray = np.array(resized)

    featuremap = kernelizeMass(imageArray)
    return featuremap

# Classify image function
def classify(image):
    processed = preprocess(image)
    pred = svmModel.predict(processed)
    return pred

# Create streamlit app from functions
