from flask import Flask, request, send_file
from pylibdmtx.pylibdmtx import encode
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route("/")
def barcode():
    text = request.args.get("text", "Hello")
    encoded = encode(text.encode("utf-8"))
    img = Image.frombytes("RGB", (encoded.width, encoded.height), encoded.pixels)

    bio = BytesIO()
    img.save(bio, format="PNG")
    bio.seek(0)

    return send_file(bio, mimetype="image/png")

app.run(host="0.0.0.0", port=5000)
