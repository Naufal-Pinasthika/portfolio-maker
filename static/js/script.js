document.getElementById("btn-generate")?.addEventListener("click", () => {
  const element = document.getElementById("portfolio-content");
  const opt = {
    margin:       0.5,
    filename:     "portfolio.pdf",
    image:        { type: "jpeg", quality: 0.98 },
    html2canvas:  { scale: 2, logging: true, useCORS: true },
    jsPDF:        { unit: "in", format: "a4", orientation: "portrait" }
  };
  html2pdf().set(opt).from(element).save()
    .catch(err => {
      console.error("Gagal generate PDF:", err);
      alert("Maaf, terjadi kesalahan saat generate PDF. Cek console untuk detail.");
    });
});
