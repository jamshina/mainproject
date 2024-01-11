from flask import Flask
from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model
model = load('Significant_Earthquakes.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the request
        latitude = float(request.form['latitude'])
        longitude = float(request.form['longitude'])
        depth = float(request.form['mag'])

        # Make a prediction
        input_data = np.array([[latitude, longitude, mag]])
        prediction = model.predict(input_data)

        # Return the result
        return render_template('result.html', prediction=prediction[0])

    except Exception as e:
        return render_template('error.html', error_message=str(e))

if __name__ == '__main__':
    app.run(debug=True)



