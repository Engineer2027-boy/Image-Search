from flask import render_template, Flask, request, jsonify
import base64
from PIL import Image
from io import BytesIO
import numpy as np
import cv2
from skimage.metrics import structural_similarity as ssim

app = Flask(__name__)


def compare_image(img1, img2):
    arr1 = np.array(img1.convert("L"))
    arr2 = np.array(img2.convert("L"))

    if arr1.shape != arr2.shape:
        arr2 = cv2.resize(arr2, (arr1.shape[1], arr1.shape[0]))

    score, _, = ssim(arr1, arr2, full=True)
    return round(score*100, 2)


def decode_image(img_str):
    img_str = img_str.split(',')[1:]
    img_str = base64.b64decode(img_str)
    img = Image.open(BytesIO(img_str)).convert("RGB")
    return img


@app.route("/", methods=["GET"])
def main_page():
    return render_template("matchimage.html")


@app.route('/compare', methods=["POST"])
def compare():
    data = request.get_json()
    img1 = decode_image(data["image1"])
    img2 = decode_image(data["image2"])
    similarity = compare_image(img1, img2)
    return jsonify({"similarity" : similarity})


if __name__ == "__main__":
    app.run(debug=True)

