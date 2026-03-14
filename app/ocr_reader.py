import easyocr
from pdf2image import convert_from_path
import numpy as np
import cv2

reader = easyocr.Reader(['en'])

def extract_text_from_handwritten_pdf(pdf_path):

    pages = convert_from_path(
        pdf_path,
        poppler_path=r"C:\poppler\poppler-23.11.0\Library\bin"
    )

    full_text = ""

    for page in pages[:1]:

        image = np.array(page)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        height = gray.shape[0]

        # split into horizontal strips
        for i in range(0, height, 120):

            line = gray[i:i+120, :]

            results = reader.readtext(line, detail=0)

            for text in results:
                full_text += text + " "

    return full_text