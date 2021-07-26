import os
import joblib
classifier = joblib.load(r'smartirrigation.pkl')

# importing Flask and other modules
from flask import Flask, request, render_template 
import numpy as np
  
# Flask constructor
app = Flask(__name__)   
  
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods = ["GET", "POST"])
def green_hacks():
    if request.method == "POST":
       m_c = request.form.get("m_c")
       temp = request.form.get("temp")
       p = classifier.predict(np.array([m_c, temp]).reshape(-2,2))
       if p == 0:
           output = "No need for the pump to be on."
           return render_template('index.html', output=output)
       elif p == 1:
           output = "Switch on your pump immediately."
           return render_template('index.html', output=output)
        
    return render_template('index.html')
  
if __name__=='__main__':
   port = int(os.environ.get("PORT", 5000))
   app.run(host='0.0.0.0', port=port)
