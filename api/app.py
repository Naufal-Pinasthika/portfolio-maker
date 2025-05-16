from flask import Flask, request, render_template, send_file, redirect, flash
import pdfkit
from io import BytesIO
from werkzeug.wrappers import Request, Response

app = Flask(__name__, template_folder="templates")
app.secret_key = 'ganti_dengan_secret_key_anda'  # Ubah sesuai kebutuhan

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Validasi field yang diperlukan
        required_fields = ['name', 'email', 'phone', 
                           'edu_university', 'edu_city', 'edu_degree_major', 'edu_gpa', 'edu_year']
        missing_fields = [field for field in required_fields if not request.form.get(field)]
        if missing_fields:
            flash("Mohon lengkapi field berikut: " + ", ".join(missing_fields), "danger")
            return redirect('/')
        
        # Ambil data dari form
        name   = request.form.get('name')
        email  = request.form.get('email')
        phone  = request.form.get('phone')
        
        edu_university  = request.form.get('edu_university')
        edu_city        = request.form.get('edu_city')
        edu_degree_major = request.form.get('edu_degree_major')
        edu_gpa         = request.form.get('edu_gpa')
        edu_year        = request.form.get('edu_year')
        edu_achievement = request.form.get('edu_achievement')
        
        work_company  = request.form.get('work_company')
        work_city     = request.form.get('work_city')
        work_position = request.form.get('work_position')
        work_period   = request.form.get('work_period')
        work_details  = request.form.get('work_details')
        
        leadership_role     = request.form.get('leadership_role')
        leadership_org      = request.form.get('leadership_org')
        leadership_period   = request.form.get('leadership_period')
        leadership_details  = request.form.get('leadership_details')
        
        skills = request.form.get('skills')
        
        # Render template PDF dengan data
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
            # Di lingkungan deploy, pastikan wkhtmltopdf telah tersedia di PATH
            pdf = pdfkit.from_string(rendered, False)
        except Exception as e:
            flash("Error saat generate PDF: " + str(e), "danger")
            return redirect('/')
        
        return send_file(BytesIO(pdf),
                         as_attachment=True,
                         download_name="portfolio.pdf",
                         mimetype='application/pdf')
    return render_template('form.html')

# Fungsi handler untuk Vercel (tanpa awsgi)
def handler(request):
    """
    Fungsi ini bertugas mengkonversi request Vercel ke format WSGI,
    memanggil aplikasi Flask, dan mengembalikan response dalam format
    yang sesuai dengan Vercel.
    """
    # Ambil WSGI environ dari request
    environ = request.environ

    # Gunakan list untuk menangkap status dan header yang akan di-set
    status_headers = []

    def start_response(status, headers, exc_info=None):
        status_headers.append((status, headers))

    # Panggil aplikasi Flask dengan environ dan start_response tersebut
    response_iter = app(environ, start_response)
    status, headers = status_headers[0]
    response_body = b"".join(response_iter)

    # Konversi hasil menjadi objek Response dari werkzeug
    return Response(response_body, status=int(status.split(" ")[0]), headers=dict(headers))
