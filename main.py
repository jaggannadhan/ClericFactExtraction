from flask import Flask, render_template
from src.handlers.ClericHandler import cleric

app = Flask(__name__)
app.register_blueprint(cleric)

@app.route("/")
def default():
    return render_template("LandingPage.html")

# run the app
if __name__ == "__main__":
    app.host = "0.0.0.0"
    app.port = 5000
    app.debug = True
    app.run()