import numpy as np 
from flask import Flask,request,jsonify,render_template
import pickle
import math
import webbrowser

app = Flask(__name__)
model = pickle.load(open('text.pkl','rb'))

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
	int_features  = [int(x) for x in request.form.values()]
	final_features = [np.array(int_features)]
	prediction = model.predict(final_features)
	output = round(prediction[0],2)
	if output > 0:
		return render_template('index.html',prediction_text="Number of Weekly Rides Should be {}".format(math.floor(output)))
	else :
		return render_template('index.html',prediction_text="Inappropriate input parameters")


if __name__ == '__main__':
	webbrowser.open('http://127.0.0.1:5000/')
	# webbrowser.open(' ')
	app.run(debug=False)				
