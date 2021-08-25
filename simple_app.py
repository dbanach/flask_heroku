from flask import Flask, request
import os
app = Flask(__name__)


@app.route("/")
def index():

    return """<div style="background-color:black;color:green;"> <style> s10 {font-size:100;} </style><s10><b> Knock Knock, NEO </b></s10></div>"""


@app.route('/pill')
def what_pill():

    return "What pill will you take "+request.args.get('name') + '?'



if __name__ == '__main__':

    app.run(host='0.0.0.0',port=int(os.environ.get('PORT')))


