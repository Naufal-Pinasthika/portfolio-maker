**Portfolio Maker**

**Description**
Portfolio Maker is a simple web application that allows users to create a Curriculum Vitae (CV) interactively and download it as a PDF.

---

## Key Features

* **Form Input**: Users fill in personal details, education, work experience, leadership roles, and skills.
* **Live Preview**: After submitting the form, the application displays a CV preview directly in the browser.
* **One-click PDF**: With a single click on the **`View & Download CV`** button, the CV is automatically generated and downloaded as a PDF.

---

## Project Structure

```
portfolio-maker/
├─ api/
│  └─ app.py                   # Flask application without PDFkit
├─ templates/
│  ├─ form.html                # Form input page
│  └─ portfolio_template.html  # CV template using html2pdf.js
├─ static/
│  └─ js/
│     └─ script.js             # Client-side html2pdf trigger & auto-download code
├─ requirements.txt            # Python dependencies
└─ vercel.json                 # Vercel deployment configuration
```

---

## Requirements

* Python 3.7 or higher
* Git
* Vercel account (optional, for deployment)

---

## Local Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Naufal-Pinasthika/portfolio-maker.git
   cd portfolio-maker
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # Linux/Mac
   venv\\Scripts\\activate   # Windows
   pip install -r requirements.txt
   ```

3. **Start the Flask server**:

   ```bash
   python api/app.py
   ```

   The application will run at `http://127.0.0.1:5000/`.

4. **Open the application** in your browser at `http://127.0.0.1:5000/`.

---

## Deployment to Vercel

1. **Install Vercel CLI**:

   ```bash
   npm install -g vercel
   ```

2. **Login and deploy**:

   ```bash
   vercel login
   vercel
   ```

3. Follow the prompts to complete the deployment. Your app will be available at `https://YOUR-DEPLOYMENT-URL.vercel.app/`.

---

## How to Use

1. Navigate to the home page.
2. Fill in all required fields (name, email, education, experience, etc.).
3. Click the **`View & Download CV`** button.
4. The app will show a live preview of your CV and automatically download it as `portfolio.pdf`.

---

## Technical Notes

* PDF generation is handled **entirely on the client side** using `html2pdf.js`.
* No external binaries (e.g., `wkhtmltopdf`) or additional server-side libraries are required.
* The PDF is generated automatically when the preview page loads.

---
