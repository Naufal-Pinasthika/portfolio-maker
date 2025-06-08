// static/js/script.js
document.addEventListener("DOMContentLoaded", () => {
  console.log("✅ DOMContentLoaded — script.js aktif");
  console.log("html2pdf:", typeof html2pdf);  // harus "function"

  const btn = document.getElementById("btn-generate");
  console.log("btn-generate element:", btn);  // pastikan bukan null
  if (!btn) return console.error("❌ Tombol #btn-generate tidak ada di DOM");

  btn.addEventListener("click", () => {
    console.log("🖱️ Tombol Download PDF diklik");
    const element = document.getElementById("portfolio-content");
    console.log("portfolio-content element:", element);  // pastikan bukan null
    if (!element) return console.error("❌ Elemen #portfolio-content tidak ada di DOM");

    const opt = {
      margin:       0.5,
      filename:     "portfolio.pdf",
      image:        { type: "jpeg", quality: 0.98 },
      html2canvas:  { scale: 2, logging: true, useCORS: true },
      jsPDF:        { unit: "in", format: "a4", orientation: "portrait" }
    };
    html2pdf()
      .set(opt)
      .from(element)
      .save()
      .then(() => console.log("✅ PDF berhasil digenerate"))
      .catch(err => console.error("❌ Gagal generate PDF:", err));
  });
});
