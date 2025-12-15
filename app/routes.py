from flask import Blueprint, render_template, request, send_file, current_app
import os
from werkzeug.utils import secure_filename
from app.services.image_processing import preprocess_image
from app.services.stitch_generator import extract_contours, contours_to_stitches
from app.services.dst_writer import write_dst
import uuid

main = Blueprint("main", __name__)

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("image")

        # DEBUG: Print file info
        print(f"DEBUG: File received: {file}")
        if file:
            print(f"DEBUG: Filename: {file.filename}")
            print(f"DEBUG: Content type: {file.content_type}")
            print(f"DEBUG: Allowed file check: {allowed_file(file.filename)}")
        

        if not file or not allowed_file(file.filename):
            return "Invalid file", 400

        filename = secure_filename(file.filename)

        upload_path = os.path.join(
            current_app.config['UPLOAD_FOLDER'],
            filename
        )

        file.save(upload_path)

        # Processing pipeline
        binary = preprocess_image(upload_path)
        contours = extract_contours(binary)
        stitches = contours_to_stitches(contours, scale=1)

        output_filename = f"{uuid.uuid4().hex}.dst"
        output_path = os.path.join(
            current_app.config['UPLOAD_FOLDER'],
            output_filename
        )

        write_dst(stitches, output_path)

        return send_file(output_path, as_attachment=True)

    return render_template("index.html")
