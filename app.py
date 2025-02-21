from flask import request, Flask, jsonify
from utils.ResponseBuilder import ResponseBuilder
from utils.PredictClass import PredictClass
from PIL import Image
import io
app = Flask(__name__)

@app.route('/test', methods=["GET"])
def testApp():
    res = ResponseBuilder.success(None,"server is working")
    return jsonify(res)

@app.route("/predict", methods=["POST"])
def predict_image():
    try:
        data = request.files.get("image")
        
        if data :
            image = Image.open(io.BytesIO(data.read()))
            print("data", str(image))
            processedImage = PredictClass.preprocessImage(image)
            predClass = PredictClass.predictClass(processedImage)
            print("pred", predClass)
            res = ResponseBuilder.success({"class": predClass}, "Class Predicted")
        else:
            res = ResponseBuilder.error("File not found!")

    except Exception as e:
        res = ResponseBuilder.error("something went wrong", e)
    return jsonify(res)
    

if __name__ == "__main__":
    app.run(debug=True, port=5050)