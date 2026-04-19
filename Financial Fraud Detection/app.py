from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    final_input = np.array(data).reshape(1, -1)

    prediction = model.predict(final_input)

    if prediction[0] == 1:
        result = "Fraud Transaction ⚠️"
    else:
        result = "Normal Transaction ✅"

    return render_template('index.html', prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)