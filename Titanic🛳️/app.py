from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

with open('/Users/Ashish Mishra/OneDrive/Desktop/Titanic🛳️/titanic.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        gender = int(request.form['gender'])
        age = float(request.form['age'])
        nos = int(request.form['nos'])
        tier = int(request.form['tier'])
        embarked = int(request.form['embarked'])
        cabin = int(request.form['cabin'])
        fare = float(request.form['fare'])
        npca = int(request.form['npca'])
        
        user_input = np.array([[tier, gender, age, nos, npca, fare, cabin, embarked]])
        
        model_output = model.predict(user_input)[0]
        output_user = "Survived" if model_output == 1 else "Not Survived"
        
        return render_template('templates\index.html', survived=output_user)
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    app.run(debug=True, port=8000)
