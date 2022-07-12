from flask import Flask, render_template, request
from chat import get_response
import os
print(os.getcwd())


app = Flask(__name__, template_folder=r'templates')

@app.route("/", methods=['GET'])
def index_get():
    return render_template("index.html")

@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    return str(get_response(userText))



if __name__ == '__main__':
    app.run(debug = False)
    
  
