# Smart Lemmatizer

A production-ready wrapper around NLTK's tokenizer, POS tagger, and WordNet lemmatizer. It simplifies the process of lemmatizing text by combining all necessary preprocessing steps into one reusable class.

---

## 🚀 Features

- Sentence and word tokenization
- POS tagging using NLTK's `pos_tag`
- WordNet POS tag conversion
- Lemmatization with context-aware POS tagging

---

## 📦 Installation

Make sure you have `nltk` installed. If not, install it with:

```bash
pip install nltk
```

Then download the required NLTK resources (done automatically if you run the script as-is):

```python
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('omw-1.4')
```

---

## 🧠 Usage

```python
from smart_lemmatizer import SmartLemmatizer

lemmatizer = SmartLemmatizer()
text = "The children are playing happily in the gardens. They have been running fast."
lemmatized_output = lemmatizer.lemmatize_text(text)

for sentence in lemmatized_output:
    print(sentence)
```

---

## 📁 Project Structure

```
nlp-utils/
├── smart_lemmatizer.py       # Main lemmatizer class
├── README.md                 # Documentation
└── tests/
    └── test_lemmatizer.py    # Unit tests
```

---

## ✅ Example Output

Input:
```
The children are playing happily in the gardens.
```

Output:
```
['The', 'child', 'be', 'play', 'happily', 'in', 'the', 'garden', '.']
```

---

## 🧪 Testing

Run tests using `pytest`:

```bash
pytest tests/test_lemmatizer.py
```

---

## 👨‍💻 Author

Crafted with ❤️ by Dnyanesh(Dan)

