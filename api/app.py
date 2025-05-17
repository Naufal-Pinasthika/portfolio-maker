from flask import Flask, request, render_template, send_file, redirect, flash
import pdfkit
from io import BytesIO
from werkzeug.wrappers import Response

# Inisialisasi Flask dengan mengarahkan ke folder templates yang satu level di atas
app = Flask(__name__, template_folder="../templates")
app.secret_key = 'ganti_dengan_secret_key_anda'  # Ganti dengan secret key Anda

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Validasi required fields
        required_fields = ['name', 'email', 'phone', 'edu_university', 'edu_city', 
                           'edu_degree_major', 'edu_gpa', 'edu_year']
        missing_fields = [field for field in required_fields if not request.form.get(field)]
        if missing_fields:
            flash("Mohon lengkapi field berikut: " + ", ".join(missing_fields), "danger")
            return redirect('/')

        # Mengambil data Personal Information
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')

        # Mengambil data Education
        edu_university = request.form.get('edu_university')
        edu_city = request.form.get('edu_city')
        edu_degree_major = request.form.get('edu_degree_major')
        edu_gpa = request.form.get('edu_gpa')
        edu_year = request.form.get('edu_year')
        edu_achievement = request.form.get('edu_achievement')

        # Mengambil data Work Experience
        work_company = request.form.get('work_company')
        work_city = request.form.get('work_city')
        work_position = request.form.get('work_position')
        work_period = request.form.get('work_period')
        work_details = request.form.get('work_details')

        # Mengambil data Leadership & Activities
        leadership_role = request.form.get('leadership_role')
        leadership_org = request.form.get('leadership_org')
        leadership_period = request.form.get('leadership_period')
        leadership_details = request.form.get('leadership_details')

        # Mengambil data Skills & Interests
        skills = request.form.get('skills')

        # Render template HTML portfolio dengan data yang disediakan
        rendered = render_template('portfolio_template.html',
                                   name=name,
                                   email=email,
                                   phone=phone,
                                   edu_university=edu_university,
                                   edu_city=edu_city,
                                   edu_degree_major=edu_degree_major,
                                   edu_gpa=edu_gpa,
                                   edu_year=edu_year,
                                   edu_achievement=edu_achievement,
                                   work_company=work_company,
                                   work_city=work_city,
                                   work_position=work_position,
                                   work_period=work_period,
                                   work_details=work_details,
                                   leadership_role=leadership_role,
                                   leadership_org=leadership_org,
                                   leadership_period=leadership_period,
                                   leadership_details=leadership_details,
                                   skills=skills)

        try:
            # Konfigurasi untuk menggunakan binary wkhtmltopdf dari folder proyek
            config = pdfkit.configuration(wkhtmltopdf="./wkhtmltopdf/bin/wkhtmltopdf")
            pdf = pdfkit.from_string(rendered, False, configuration=config)
        except Exception as e:
            flash("Error saat generate PDF: " + str(e), "danger")
            return redirect('/')

        return send_file(BytesIO(pdf),
                         as_attachment=True,
                         download_name="portfolio.pdf",
                         mimetype='application/pdf')

    return render_template('form.html')


# Fungsi handler untuk Vercel.
# Fungsi ini menjadi entry point yang digunakan oleh Vercel untuk menangani request.
def handler(request):
    environ = request.environ
    status_headers = []

    def start_response(status, headers, exc_info=None):
        status_headers.append((status, headers))
    
    response_iter = app(environ, start_response)
    status, headers = status_headers[0]
    response_body = b"".join(response_iter)
    return Response(response_body, status=int(status.split(" ")[0]), headers=dict(headers))


if __name__ == '__main__':
    app.run(debug=True)
