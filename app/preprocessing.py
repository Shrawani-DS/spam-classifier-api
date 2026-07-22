import string
import nltk

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download required NLTK resources (runs only once if already downloaded)
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("punkt_tab")

# Initialize stemmer
ps = PorterStemmer()

# Load stopwords once
stop_words = set(stopwords.words("english"))


def transform_text(text):
    """
    Preprocess input text by:
    1. Converting to lowercase
    2. Tokenizing
    3. Removing non-alphanumeric tokens
    4. Removing stopwords and punctuation
    5. Applying stemming

    Returns:
        Preprocessed text as a single string.
    """

    # Convert to lowercase
    text = text.lower()

    # Tokenize
    text = nltk.word_tokenize(text)

    # Keep only alphanumeric words
    words = []

    for word in text:
        if word.isalnum():
            words.append(word)

    # Remove stopwords and punctuation
    filtered_words = []

    for word in words:
        if word not in stop_words and word not in string.punctuation:
            filtered_words.append(word)

    # Apply stemming
    stemmed_words = []

    for word in filtered_words:
        stemmed_words.append(ps.stem(word))

    # Return cleaned text
    return " ".join(stemmed_words)