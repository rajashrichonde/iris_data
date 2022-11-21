from flask import Flask,jsonify,request
from project_app.utils import SpeciesType
import config
app=Flask(__name__)

@app.route("/") #Basic API
def home_api():
    print("Hello Python")
    return "Home api"

@app.route("/predict_iris")
def predict_iris():
    
    input_data=request.get_json()
    
    sepal_length =int(input_data["sepal_length"])
    sepal_width = int(input_data["sepal_width"])
    petal_length =int(input_data["petal_length"])
    petal_width = int(input_data["petal_width"])
    
    Species=SpeciesType(sepal_length,sepal_width,petal_length,petal_width)

    iris_types=Species.predict_target()
    
    return jsonify({"Result":f"print the iris flower types is:{iris_types}"})
if __name__=="__main__":
    app.run(debug=True)