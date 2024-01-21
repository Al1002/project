from flask import Flask
from flask import request
from flask import send_file
import os

app = Flask(__name__)

root = './'

@app.post('/upload')
def upload_file():
    file = request.files['file']
    user = request.form['user']
    user += '/' # to dir
    if not os.path.exists(user):
        os.makedirs(root + user)
    file.save(root + user + file.filename)
    return 'OK', 200

@app.get('/download')
def download_file():
    requested_file = request.form['file']
    user = request.form['user']
    user += '/' # to dir
    if not os.path.exists(root + user + requested_file):
        return "Error: File or user does not exist", 404
    return send_file(root + user + requested_file, as_attachment=True), 200

@app.get('/delete')
def delete_file():
    return "Feature dont work", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0")