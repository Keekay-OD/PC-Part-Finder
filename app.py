from flask import Flask, render_template, url_for
#from main import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
    #return login()

if __name__ == "__main__":
  app.run(debug=True)