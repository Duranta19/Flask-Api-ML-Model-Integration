import numpy as np
import tensorflow as tf
import os

class PredictClass:
    model = tf.keras.models.load_model(os.path.join(os.path.dirname(__file__), '../ml_model/densenet_model.h5'))  
    @staticmethod
    def preprocessImage(image):
        if image.mode != "RGB":
            image = image.convert("RGB")

        image = image.resize((224, 224)) 
        image = np.array(image) / 255.0  
        image = np.expand_dims(image, axis=0) 
        return image

    @staticmethod
    def predictClass(image):
        class_labels = ['initial-melasma', 'melasma', 'null and other diseases']
        try:
            prediction = PredictClass.model.predict(image)
            predicted_class = np.argmax(prediction)
            return class_labels[int(predicted_class)]
        except Exception as e:
            return str(e)
