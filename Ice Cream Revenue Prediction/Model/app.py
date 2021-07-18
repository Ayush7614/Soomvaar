import joblib
model = joblib.load(r'C:\Users\DELL\Desktop\Technical Work\Github GSSoC21\ML-ProjectYard\Ice Cream Revenue Prediction\Model\IceCreamRevenuePrediction.pkl')

# importing Flask and other modules
from flask import Flask, request, render_template 
import numpy as np
  
# Flask constructor
app = Flask(__name__)   
  
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods = ["GET", "POST"])
def gfg():
    if request.method == "POST":
       temp = request.form.get("fname")
       return "Today's revenue is: Rs. "+ str(round(float(model.predict(np.array(temp).reshape(-1,1))),2))
    return render_template('form.html')
  
if __name__=='__main__':
   app.run()