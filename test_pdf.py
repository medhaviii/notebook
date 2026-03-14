from app.pdf_parser import extract_text_from_pdf
from app.utils import clean_text, chunk_text
from app.classifier import classify_text

file_path = "sample.pdf"

text = extract_text_from_pdf(file_path)

print("RAW TEXT LENGTH:", len(text))
print("RAW TEXT:", text[:200])

text = clean_text(text)

chunks = chunk_text(text)

print("Number of Chunks:", len(chunks))

for chunk in chunks:
    subject = classify_text(chunk)

    print("Subject:", subject)
    print("Preview:", chunk[:150])
    print("-"*40)