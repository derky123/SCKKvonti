from flask import Flask, render_template, request, redirect, url_for
import os
import mimetypes

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fájl feltöltése
        file = request.files['file']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

        # Keresett szöveg megkeresése a fájlban
        search = request.form['search']
        with open(os.path.join(app.config['UPLOAD_FOLDER'], file.filename), 'r') as f:
            content = f.read()
            search_result = content.count(search)

        return render_template('index.html', search_result=search_result)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)