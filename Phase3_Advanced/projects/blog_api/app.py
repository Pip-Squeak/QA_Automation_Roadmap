# Mini Project: Blog API
from flask import Flask, jsonify

app = Flask(__name__)

posts = [
    {"id": 1, "title": "Hello World", "content": "My first post"}
]

@app.route("/posts", methods=["GET"])
def get_posts():
    return jsonify(posts)

if __name__ == "__main__":
    app.run(debug=True)
