from flask import Flask, render_template, send_file
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    # Membaca data dari file CSV
    jan = pd.read_csv('Penjualan_Jan.csv')
    feb = pd.read_csv('Penjualan_Feb.csv')
    mar = pd.read_csv('Penjualan_Mar.csv')

    # Menggabungkan data
    data = pd.concat([jan, feb, mar], ignore_index=True)
    print(data)  # Menampilkan data di terminal
    return data.to_html()

@app.route('/grafik')
def grafik():
    # Membaca data dari file CSV
    jan = pd.read_csv('Penjualan_Jan.csv')
    feb = pd.read_csv('Penjualan_Feb.csv')
    mar = pd.read_csv('Penjualan_Mar.csv')

    # Menggabungkan data
    data = pd.concat([jan, feb, mar], ignore_index=True)
    data['Bulan'] = pd.to_datetime(data['Tanggal']).dt.month

    # Membuat grafik
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Bulan', y='Jumlah_Terjual', data=data, ci=None)
    plt.title('Total Penjualan per Bulan')
    plt.xlabel('Bulan')
    plt.ylabel('Jumlah Terjual')
    
    # Path to save the image
    image_path = os.path.join('static', 'penjualan_per_bulan.png')
    plt.savefig(image_path)
    plt.close()

    return send_file(image_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)

