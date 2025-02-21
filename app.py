from flask import request, Flask, jsonify
from utils.ResponseBuilder import ResponseBuilder
from utils.PredictClass import PredictClass
from PIL import Image
import io
app = Flask(__name__)

@app.route('/test', methods=["GET"])
def testApp():
    try:
        res = ResponseBuilder.success(None,"server is working")
    except Exception as e:
        res = ResponseBuilder.error("Server Connection failed", str(e), 500)
    return jsonify(res)

@app.route("/predict", methods=["POST"])
def predict_image():
    try:
        data = request.files.get("image")
        
        if data :
            image = Image.open(io.BytesIO(data.read()))
            processedImage = PredictClass.preprocessImage(image)
            predClass = PredictClass.predictClass(processedImage)
            if not predClass:
                res = ResponseBuilder.error("Class Prediction Failed", None, 204)
            res = ResponseBuilder.success({"class": predClass}, "Class Predicted Success")
        else:
            res = ResponseBuilder.error("File not found!", None, 404)

    except Exception as e:
        res = ResponseBuilder.error("something went wrong", str(e), 500)
    return jsonify(res)
    

if __name__ == "__main__":
    app.run(debug=True, port=5050)