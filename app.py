from flask import Flask ,render_template,request,jsonify
from flask_cors import CORS
from chat import get_response
import os
TEMPLATE_DIR = os.path.abspath('templates')
STATIC_DIR = os.path.abspath('static')

# app = Flask(__name__) # to make the app run without any
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

#app=Flask(__name__)
app=Flask(__name__,template_folder='templates')
CORS(app)

@app.get("/")
def index_get():
              return render_template("base.html")

@app.post("/predict")
def predict():
                     
                     text=request.get_json().get("message")
                     response=get_response(text)
                     message={"answer":response}
                     return jsonify(message)

if __name__=="__main__":
                     app.run(debug=True)