import pdfplumber
import os

def upload_pdf(resume):

    script_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = script_dir + "/" + resume

    def extractpdf(path):
        try:
            with pdfplumber.open(path) as pdf:
                all_text = ""
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        all_text += page_text + "\n"
            return all_text.strip() if all_text else "No text found in PDF."
        except Exception as e:
            return f"Error reading PDF: {e}"

    return extractpdf(full_path)