import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


DATA_PATH = "data"


def load_dataset():

    texts = []
    labels = []

    for subject in os.listdir(DATA_PATH):

        subject_path = os.path.join(DATA_PATH, subject)

        if os.path.isdir(subject_path):

            for file in os.listdir(subject_path):

                file_path = os.path.join(subject_path, file)

                with open(file_path, "r", encoding="utf-8") as f:
                    text = f.read()

                    texts.append(text)
                    labels.append(subject)

    return texts, labels


# Load training data
texts, labels = load_dataset()


# TF-IDF vectorization
vectorizer = TfidfVectorizer(stop_words="english")

X = vectorizer.fit_transform(texts)


# Train classifier
model = LogisticRegression()

model.fit(X, labels)


def classify_text(text):

    X_test = vectorizer.transform([text])

    prediction = model.predict(X_test)

    return prediction[0]