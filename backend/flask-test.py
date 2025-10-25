from flask import Flask

app = Flask(__name__)

@app.route("/")
def cheap_bananas():
    return "<p>cheap bananas project</p>"