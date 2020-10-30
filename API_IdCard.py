from flask import Flask

app = Flask(__name__)

@app.route("/images", methods=["GET"])
def get_images():
    pass

@app.route("/images/add", methods=["POST"])
def insert_images():
    pass
if __name__ == "__main__":
    app.run()
