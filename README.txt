Step-1: Install Dependencies (python ^3.10)
pip install Tensorflow
pip install Numpy
pip install matplotlib
pip install scikit-learn
pip install pillow
pip install Streamlit

Step 2: Prepare the Dataset
Collect the dataset of CT Scan image in Real Time datasets and Label the images based on the positive or negative of lung cancer.

Step 3: Image Preprocessing
Use image processing techniques to clean and prepare your image data.
Resize images to a consistent size.
Normalize pixel values.
Augment data if necessary (e.g., rotation, flipping).

Step 4: Build the Detection Model
Use a convolutional neural network (CNN) architecture to build your lung cancer detection model.

Step 5: Train the Model
Train your model using the preprocessed image data and the corresponding labels.

Step 6: Evaluate and Deploy
After training, evaluate your model on a separate test set

Step 7: Intergration
Intergrate the Trained model with the web appilcation of Streamlit UI library  

Step 8: To run the application
streamlit run app.py
