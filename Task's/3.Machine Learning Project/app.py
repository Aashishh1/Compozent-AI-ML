from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('3.Machine Learning Project\house_price_model.pkl')

@app.route('/')
def home():
    return render_template('design.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the frontend
        data = request.json
        square_feet = float(data.get('square_feet'))
        bedrooms = int(data.get('bedrooms'))
        bathrooms = int(data.get('bathrooms'))
        location = int(data.get('location'))  # 0 for city, 1 for suburb
        age_of_house = int(data.get('age_of_house'))
        floor_number = int(data.get('floor_number'))

        # Prepare the features for prediction
        features = np.array([[square_feet, bedrooms, bathrooms, location, age_of_house, floor_number]])

        # Make prediction (the output will be in INR)
        prediction = model.predict(features)[0]

        # Return the prediction in INR
        return jsonify({'prediction': round(prediction, 2)})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
