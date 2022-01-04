from flask import  Flask
app = Flask(__name__)

@app.route("/home")
def home():
    return "Welcome to GCP deployed python project"
if __name__ == '__main__':
    app.run(port=5000, debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
