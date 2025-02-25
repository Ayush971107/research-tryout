from flask import Flask, render_template, send_from_directory, url_for
import os

app = Flask(__name__)

# Define absolute paths to your image folders
GENERATED_FOLDER = os.path.join(os.getcwd(), "generated_images")
ANNOTATED_FOLDER = os.path.join(os.getcwd(), "Annotated2")

@app.route('/')
def index():
    # List image files that are common to both folders
    generated_files = set(os.listdir(GENERATED_FOLDER))
    annotated_files = set(os.listdir(ANNOTATED_FOLDER))
    common_files = sorted(generated_files.intersection(annotated_files))
    return render_template("index.html", files=common_files)

# Route to serve generated images
@app.route('/generated/<path:filename>')
def generated_image(filename):
    return send_from_directory(GENERATED_FOLDER, filename)

# Route to serve annotated images
@app.route('/annotated/<path:filename>')
def annotated_image(filename):
    return send_from_directory(ANNOTATED_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
