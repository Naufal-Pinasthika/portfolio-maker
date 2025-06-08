**Portfolio Maker**

**Deskripsi**
Portfolio Maker adalah aplikasi web sederhana yang memungkinkan pengguna membuat Curriculum Vitae (CV) secara interaktif dan mengunduhnya dalam format PDF hanya dengan satu klik.

---

## Fitur Utama

* **Form Input**: Pengguna mengisi data pribadi, pendidikan, pengalaman kerja, kepemimpinan, dan keterampilan.
* **Preview**: Setelah submit form, aplikasi menampilkan preview CV langsung di browser.
* **One-click PDF**: Dengan satu klik tombol `Lihat & Download CV`, PDF CV otomatis dihasilkan dan diunduh.

---

## Struktur Proyek

```
portfolio-maker/
├─ api/
│  └─ app.py            # Aplikasi Flask tanpa PDFkit
├─ templates/
│  ├─ form.html         # Halaman input form
│  └─ portfolio_template.html  # Template CV dengan html2pdf.js
├─ static/
│  └─ js/
│     └─ script.js      # Kode client-side html2pdf trigger & auto-download
├─ requirements.txt     # Daftar dependencies Python
└─ vercel.json          # Konfigurasi deploy ke Vercel
```

---

## Persyaratan

* Python 3.7+
* Git
* Akun Vercel (opsional, untuk deploy)

---

## Cara Menjalankan Secara Lokal

1. **Clone repository**:

   ```bash
   git clone https://github.com/Naufal-Pinasthika/portfolio-maker.git
   cd portfolio-maker
   ```

2. **Pasang environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\\Scripts\\activate  # Windows
   pip install -r requirements.txt
   ```

3. **Jalankan server Flask**:

   ```bash
   python api/app.py
   ```

   Aplikasi berjalan di `http://127.0.0.1:5000/`.

4. **Akses aplikasi** di browser: buka `http://127.0.0.1:5000/`.

---

## Cara Deploy ke Vercel

1. Pasang Vercel CLI:

   ```bash
   npm install -g vercel
   ```

2. Login & deploy:

   ```bash
   vercel login
   vercel
   ```

3. Ikuti instruksi hingga selesai. Aplikasi akan tersedia di `https://portfolio-maker-green.vercel.app/` (atau subdomain-mu sendiri).

---

## Cara Menggunakan Aplikasi

1. Buka halaman utama.
2. Isi semua field yang diperlukan (nama, email, pendidikan, pengalaman, dsb.).
3. Klik tombol **Lihat & Download CV**.
4. Aplikasi akan menampilkan preview CV, lalu otomatis mengunduh file `portfolio.pdf`.

---

## Catatan Teknis

* Proses PDF dijalankan **sepenuhnya di sisi klien** menggunakan `html2pdf.js`.
* Tidak diperlukan binary eksternal (`wkhtmltopdf`) atau library server-side lain.
* PDF otomatis ter-generate saat halaman preview dimuat.

---

**Selamat mencoba!**
