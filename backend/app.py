from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Secure Finance Capstone is running!"

if __name__ == "__main__":
    app.run(debug=True)
