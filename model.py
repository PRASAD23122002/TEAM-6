from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

np.set_printoptions(suppress=True)

model = load_model(r"C:\Users\Shakthivel\Desktop\Main Project\keras_Model.h5", compile=False)

class_names = open(r"C:\Users\Shakthivel\Desktop\Main Project\labels.txt", "r").readlines()


def process_image(image):
    print('process')
    size = (224, 224)

    image = image.convert("RGB")

    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1


    data = np.expand_dims(normalized_image_array, axis=0)
    prediction = model.predict(data)
    index = np.argmax(prediction)

    class_name = class_names[index]
    confidence_score = prediction[0][index]

    return class_name[2:],confidence_score





