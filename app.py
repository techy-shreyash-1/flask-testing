from flask import Flask
import time
app = Flask(__name__)

@app.route('/')
def hello_world():
        return '<p> hello king</p>'
@app.route('/home')
def home():
      for i in range(5):
        return i

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)