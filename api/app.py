from flask import Flask, request, render_template, redirect, flash

# Inisialisasi Flask, folder templates relatif terhadap file ini
app = Flask(__name__, template_folder="../templates")
app.secret_key = 'ganti_dengan_secret_key_anda'  # Ganti sesuai kebutuhan

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Validasi required fields
        required_fields = [
            'name', 'email', 'phone', 'edu_university',
            'edu_city', 'edu_degree_major', 'edu_gpa', 'edu_year'
        ]
        missing = [f for f in required_fields if not request.form.get(f)]
        if missing:
            flash("Mohon lengkapi field berikut: " + ", ".join(missing), "danger")
            return redirect('/')

        # Ambil semua data form sebagai dict
        data = request.form.to_dict()

        # Render halaman portfolio (HTML saja; PDF di-generate di browser)
        return render_template('portfolio_template.html', **data)

    # GET → tampilkan form
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
