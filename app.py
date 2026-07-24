from flask import Flask, render_template, request
import joblib

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Load model
model = joblib.load('model_prediksi_sentimen.pkl')

# Fungsi prediksi
def predict_sentiment(text):
    prediction = model.predict([text])[0]
    proba = model.predict_proba([text])[0]
    classes = dict(zip(model.classes_, proba))
    return prediction, classes

# Routing halaman utama
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['ulasan']
        label, probabilities = predict_sentiment(text)
        return render_template('index.html', text=text, label=label, probabilities=probabilities)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)