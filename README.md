# Sentiment Analysis Web Application

Aplikasi web untuk melakukan klasifikasi sentimen berdasarkan teks ulasan pengguna menggunakan metode **Machine Learning Naive Bayes**.

Project ini mengimplementasikan model klasifikasi teks yang digunakan untuk memprediksi kategori sentimen dari input pengguna melalui antarmuka web berbasis Flask.

## Features

- Input teks ulasan pengguna
- Prediksi kategori sentimen secara otomatis
- Menampilkan hasil klasifikasi sentimen
- Menampilkan probabilitas prediksi setiap kelas
- Web interface sederhana menggunakan Flask

## Tech Stack

**Programming Language**
- Python

**Framework & Library**
- Flask
- Scikit-learn
- Joblib
- NumPy
- SciPy

**Machine Learning Algorithm**
- Multinomial Naive Bayes

## Project Structure
sentiment-analysis/
│
├── app.py
├── model_prediksi_sentimen.pkl
├── requirements.txt
│
├── templates/
│ └── index.html
│
├── static/
│ └── style.css
│
└── README.md
