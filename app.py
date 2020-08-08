from flask import Flask, render_template, url_for
#from main import *

app = Flask(__name__)

@app.route("/")
def index():
    #return main()
    return render_template('index.html')

@app.route("/")
def search():
    return render_template('results.html')

if __name__ == "__main__":
  app.run(debug=True)