from flask import Flask
from flask.json import jsonify
from webscr import getVideos
import json

app = Flask(__name__)

def exportar(videos):
    export = []
    for video in videos:
        export.append(video.export())
    return export


@app.route("/videos")
def videos():
    videos = {
        'videos': exportar(getVideos())
    }
    return jsonify(videos)

while __name__ == '__main__':
    app.run()