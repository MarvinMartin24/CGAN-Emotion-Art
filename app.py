from flask import Flask, request, render_template, send_from_directory, redirect, send_file
import os
import generator_64

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=['POST'])
def upload():
    style = request.form.get("style")
    emotion = request.form.get("emotion")
    nb_img = request.form.get("nb_img")
    return render_template("main.html", selected_emotion=emotion, selected_style=style, nb_img=nb_img)

@app.route('/main/<selected_emotion>/<selected_style>/<nb_img>')
def send_processed_image(selected_emotion, selected_style, nb_img):
    generator_64.generate(selected_emotion, selected_style, nb_img)
    return send_from_directory("images", "fake.png")

if __name__ == '__main__':
    app.run()
