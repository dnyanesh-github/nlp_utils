![Build Status](https://github.com/dnyanesh-github/nlp_utils/actions/workflows/python-app.yml/badge.svg?branch=main)

# 🚀 Smart Lemmatizer

A production-ready wrapper around NLTK's tokenizer, POS tagger, and WordNet lemmatizer.  
It simplifies the text lemmatization process by combining all necessary preprocessing steps into a single reusable Python class.

---

## ✨ Features

- ✅ Sentence and word tokenization  
- ✅ POS tagging using NLTK’s `pos_tag`  
- ✅ POS tag conversion to WordNet format  
- ✅ Context-aware lemmatization using NLTK’s `WordNetLemmatizer`  
- ✅ Modular design for production use  
- ✅ Built-in test suite with `pytest`  
- ✅ GitHub Actions CI pipeline included  

---

## 📦 Installation

Install the package directly from GitHub:

```bash
pip install git+https://github.com/dnyanesh-github/nlp_utils.git
```

Also ensure `nltk` is installed:

```bash
pip install nltk
```

---

## 📥 Required NLTK Resources

Before running the lemmatizer, download the following NLTK resources:

```python
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('wordnet')
nltk.download('omw-1.4')
```

> ✅ These are automatically downloaded in GitHub Actions for CI.

---

## 🧠 Usage

```python
from nlp_utils.smart_lemmatizer import SmartLemmatizer

lemmatizer = SmartLemmatizer()

text = "The children are playing happily in the gardens."
result = lemmatizer.lemmatize_text(text)

print(result)
# Output: [['the', 'child', 'be', 'play', 'happily', 'in', 'the', 'garden', '.']]
```

---

## 🧪 Running Tests

To run the tests locally:

```bash
pytest tests/test_lemmatizer.py
```

> Install `pytest` if needed:
```bash
pip install pytest
```

---

## 📁 Project Structure

```
nlp_utils/
├── nlp_utils/
│   ├── __init__.py
│   └── smart_lemmatizer.py
├── tests/
│   └── test_lemmatizer.py
├── .github/
│   └── workflows/
│       └── python-app.yml
├── setup.py
└── README.md
```

---

## ✅ Sample Output

**Input:**
```
The children are playing happily in the gardens.
```

**Output:**
```
[['the', 'child', 'be', 'play', 'happily', 'in', 'the', 'garden', '.']]
```

---

## 👨‍💻 Author

Crafted with ❤️ by [Dnyanesh (Dan)](https://github.com/dnyanesh-github)

---

## 🪪 License

This project is licensed under the [MIT License](LICENSE)

---

## 🙌 Contributions

PRs are welcome! Feel free to fork the repo, improve the utility, or expand it with more NLP tools like:

- Stopword removers  
- Custom stemmers  
- Named Entity Recognizers  

Let’s build something great together!
