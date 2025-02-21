import numpy as np
import tensorflow as tf
import os
# class PredictClass:
#     def __init__(self, image):
#         self.image = image
#         self.model  = tf.keras.models.load_model(os.path.join(os.path.dirname(__file__), '../ml_model/model.h5'))
#     def preprocessImage(image):
#         image = image.resize((224, 224))  # Resize to match model input
#         image = np.array(image) / 255.0  # Normalize pixel values
#         image = np.expand_dims(image, axis=0)  # Add batch dimension
#         return image
    
#     def predictClass(self,image):
#         try:
#             prediction = self.model.predict(image)
#             predicted_class = np.argmax(prediction)
#             return predicted_class
#         except Exception as e:
#             return e

class PredictClass:
    model = tf.keras.models.load_model(os.path.join(os.path.dirname(__file__), '../ml_model/densenet_model.h5'))  

    @staticmethod
    def preprocessImage(image):
        if image.mode != "RGB":
            image = image.convert("RGB")

        image = image.resize((224, 224))  # Resize to match model input
        image = np.array(image) / 255.0  # Normalize pixel values
        image = np.expand_dims(image, axis=0)  # Add batch dimension
        return image

    @staticmethod
    def predictClass(image):
        try:
            prediction = PredictClass.model.predict(image)
            predicted_class = np.argmax(prediction)
            return int(predicted_class) 
        except Exception as e:
            return str(e)
