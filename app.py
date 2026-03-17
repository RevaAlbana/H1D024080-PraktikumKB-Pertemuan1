from flask import Flask, render_template, request
import json

app = Flask(__name__)

def get_data_laptop():
    with open('data.json', 'r') as file:
        return json.load(file) # JSON diubah menjadi List of Dictionaries di Python

@app.route('/', methods=['GET', 'POST'])
def index():
    rekomendasi = []
    pesan_error = ""

    # Jika form di website disubmit
    if request.method == 'POST':
        budget = int(request.form.get('budget'))
        kebutuhan = request.form.get('kebutuhan')
        
        database_laptop = get_data_laptop()

        for laptop in database_laptop:
            # 1. STRUKTUR KONTROL: Percabangan Sistem Pakar yang sudah dioptimalkan
            # Mengecek apakah harga <= budget AND kebutuhan pengguna ada di dalam list kategori laptop
            if laptop['harga'] <= budget and kebutuhan in laptop['kategori']:
                rekomendasi.append(laptop)

        if len(rekomendasi) == 0:
            pesan_error = "Maaf, tidak ada laptop yang sesuai dengan budget dan kebutuhanmu."

    return render_template('index.html', rekomendasi=rekomendasi, error=pesan_error)

if __name__ == '__main__':
    app.run(debug=True)