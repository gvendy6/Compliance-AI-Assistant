import pdfplumber
import os

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

if __name__ == "__main__":
    folder = "data/raw_pdfs"
    output_folder = "data/processed"

    for file in os.listdir(folder):
        if file.endswith(".pdf"):
            path = os.path.join(folder, file)
            text = extract_text_from_pdf(path)

            with open(os.path.join(output_folder, file.replace(".pdf", ".txt")), "w", encoding="utf-8") as f:
                f.write(text)

    print("Extraction completed.")