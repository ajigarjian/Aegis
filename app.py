# importing necessary frameworks and libraries 
import os
from datetime import date
from flask import Flask, flash, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from scan import *
from helpers import *


# setting global variable of path to folder for .docx files uploaded to go to on upload page
UPLOAD_FOLDER = "/Users/arijigarjian/Documents/GitHub/NIST-Scanner/static/input_output_files/"

# Configure application & set upload folder for .docx file to be uploaded to, as well as secret key
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'iPhone1000comingSoon'

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Route for logic behind home page. Returns content from index.html
@app.route("/")
def index():
    return render_template("index.html")

#Route for logic behind upload page. 
@app.route("/upload", methods = ['GET', 'POST'])
def upload_file():

    #If a POST request is incoming, that means the user is attempting to upload a file -> follow the logic below
    if request.method == 'POST':

        #if there is a file "docx_file" in the temporary storage, check that it has a name and that it is a docx file (using helper function from helpers.py)
        if request.files:
            docx_file = request.files['docx_file']

            if docx_file.filename == '':
                flash("Document must have a filename.", "warning")
                return redirect(request.url)
            
            if not allowed_file(docx_file.filename):
                flash("That file extension is not allowed.", "warning")
                return redirect(request.url)
            
            #if it is a valid file, secure it and save it to the folder as described in the global "UPLOAD_FOLDER" variable near top of app.py
            else:
                action = int(request.form.get("scan_action"))
                author = request.form.get("author_name")

                filename = secure_filename(docx_file.filename)
                
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                docx_file.save(filepath)

                doc = intakeDocx(filepath)

                # flash("File uploaded and scanned.", "success") -- Not working at the right time right now so commenting out
                scan(doc, filename, action, author)
                return redirect(url_for('download_file', name=filename))

        return redirect(request.url)

    return render_template("upload.html")

@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)

#syntax to run app.py
if __name__ == "__main__":
    app.run(debug=True)