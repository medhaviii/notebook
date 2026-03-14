import re


def clean_text(text):

    text = text.lower()

    # remove symbols
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)

    # remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    return text


def chunk_text(text, chunk_size=200):

    words = text.split()

    chunks = []

    for i in range(0, len(words), chunk_size):

        chunk = " ".join(words[i:i+chunk_size])

        chunks.append(chunk)

    return chunks