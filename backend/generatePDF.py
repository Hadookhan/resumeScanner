from fpdf import FPDF
import unicodedata

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

lines = [
    "John Doe",
    "Email: johndoe@example.com",
    "Phone: (555) 123-4567",
    "",
    "Summary:",
    "Experienced software engineer with a passion for building scalable backend systems and web applications.",
    "",
    "Skills:",
    "- Python",
    "- JavaScript",
    "- Flask",
    "- React",
    "- SQL",
    "- Docker",
    "",
    "Experience:",
    "Software Engineer - XYZ Tech (2020-Present)",
    "- Built REST APIs using Flask",
    "- Led migration to Docker-based deployment",
    "",
    "Education:",
    "B.S. in Computer Science - University of Example"
]

for line in lines:
    pdf.cell(200, 10, txt=line, ln=True)

pdf.output("test.pdf")
