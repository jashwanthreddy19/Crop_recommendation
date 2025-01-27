from flask import Flask, render_template, request
import numpy as np
import joblib
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

pipeline = joblib.load('model/random_forest_pipeline.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        n = float(request.form['n'])
        p = float(request.form['p'])
        k = float(request.form['k'])
        ph = float(request.form['ph'])
        ec = float(request.form['ec'])
        s = float(request.form['s'])
        cu = float(request.form['cu'])
        fe = float(request.form['fe'])
        mn = float(request.form['mn'])
        zn = float(request.form['zn'])
        b = float(request.form['b'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        rainfall = float(request.form['rainfall'])
        urea = float(request.form['urea'])
        moisture = float(request.form['moisture'])
        
        input_data = np.array([[n, p, k, ph, ec, s, cu, fe, mn, zn, b, temperature, humidity, rainfall, urea, moisture]])
        
        predicted_crop = pipeline.predict(input_data)
        print(f'Predicted Crop Index: {predicted_crop}')  
        if len(predicted_crop) == 0:
            return render_template('index.html', prediction_text='Error: No prediction was made.')
        
        predicted_crop_label =   predicted_crop[0]
        
        return render_template('index.html', prediction_text=f'Recommended Crop: {predicted_crop_label}')
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')


if __name__ == "__main__":
    app.run(debug=True)
