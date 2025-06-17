from scanResume import respond
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload():
    if "resume" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["resume"]
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400
    
    file_path = UPLOAD_FOLDER + "/" + file.filename
    file.save(file_path)
    try:
        res = respond(file_path)
        return jsonify({"message": "Resume processed", "response": res}), 200
    except Exception as e:
        return jsonify({"error":f"{e}"}), 500


if __name__ == "__main__":
    app.run(debug=True)