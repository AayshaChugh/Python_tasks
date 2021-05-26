from flask import Flask
from werkzeug.wrappers import request

app = Flask(__name__)
string=""


@app.route("/concat/<concate_string>",methods=['POST', 'GET'])
def concate_string(concate_string):
    global string
    string=string+" "+concate_string
    return string

if __name__=='__main__':
    app.run(debug=True)
   