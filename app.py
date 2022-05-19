# importing necessary frameworks and libraries 
import os
from datetime import date
from flask import Flask, flash, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from helpers import *

UPLOAD_FOLDER = "/Users/arijigarjian/Documents/GitHub/NIST-Scanner/static/input_output_files"

# Configure application & set upload folder for .docx file to be uploaded to
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'iPhone1000comingSoon'

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Create route for logic behind home page. Fills list "rows" with rows from general table, and renders index.html template with "rows" as input
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':

        if request.files:
            docx_file = request.files['docx_file']

            if docx_file.filename == '':
                flash("Document must have a filename.", "warning")
                return redirect(request.url)
            
            if not allowed_file(docx_file.filename):
                flash("That file extension is not allowed.", "warning")
                return redirect(request.url)
            
            else:
                filename = secure_filename(docx_file.filename)
                docx_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            flash("File uploaded.", "success")
            return redirect(request.url)

    return render_template("upload.html")










    #     # check if the post request has the file part
    #     if 'docx_file' not in request.files:
    #         flash('No file part')
    #         return redirect(request.url)
    #     file = request.files['docx_file']
    #     # If the user does not select a file, the browser submits an
    #     # empty file without a filename.
    #     if file.filename == '':
    #         flash('No selected file')
    #         return redirect(request.url)
    #     if file and allowed_file(file.filename):
    #         filename = secure_filename(file.filename)
    #         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #         return redirect(url_for('download_file', name=filename))
    # return render_template("upload.html")

#syntax to run app.py
if __name__ == "__main__":
    app.run(debug=True)