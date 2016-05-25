from __future__ import unicode_literals
import youtube_dl
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template("main.html")

@app.route('/', methods=['POST'])
def download_video():
    ydl_opts = {
        'format': '[ext=mp4]',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([request.form['video-link']])

    return render_template("response.html")

if __name__ == '__main__':
    app.run()

