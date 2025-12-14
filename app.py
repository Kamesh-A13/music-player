from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/songs"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("song")
        if file and file.filename.endswith(".mp3"):
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], file.filename))
        return redirect(url_for("index"))

    songs = os.listdir(UPLOAD_FOLDER)
    return render_template("index.html", songs=songs)

@app.route("/songs/<filename>")
def play_song(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

if __name__ == "__main__":
    app.run(debug=True)
