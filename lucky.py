from flask import Flask, render_template
import pymysql
from flask_uploads import UploadSet, IMAGES, configure_uploads, ALL
from flask import request, Flask, redirect, url_for, render_template
import os

db = pymysql.connect("127.0.0.1", "root", "root", "lucky", charset='utf8')

app = Flask(__name__)
app.config['UPLOADED_PHOTO_DEST'] = os.path.dirname(os.path.abspath(__file__)) + "/static/images/"
app.config['UPLOADED_PHOTO_ALLOW'] = IMAGES


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return 'tset111'


@app.route('/test', methods=['GET', 'POST'])
def test():
    return 'test'


@app.route('/lucky', methods=['GET', 'POST'])
def lucky():
    cursor = db.cursor()
    sql = "SELECT name FROM images"
    cursor.execute(sql)
    # results = cursor.fetchall()
    test = 'test'
    return render_template('lucky.html', test=test)


photos = UploadSet('PHOTO')
configure_uploads(app, photos)


@app.route('/upload', methods=['GET', 'POST'])
def upload_img():
    path = os.path.dirname(os.path.abspath(__file__)) + "/static/images/"
    if request.method == 'POST':
        uploaded_files = request.files.getlist("photo[]")
        for img in uploaded_files:
            photos.save(img)
            cursor = db.cursor()
            sql = "INSERT INTO images(name, path) values (%s, %s)"
            cursor.execute(sql, (img.filename, path + img.filename))
            db.commit()
        db.close()
        return "ttt"
        # return redirect(url_for('lucky', name=filename))
    return render_template('upload_img.html')


if __name__ == '__main__':
    app.run()
