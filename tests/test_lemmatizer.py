import pytest
from smart_lemmatizer import SmartLemmatizer

@pytest.fixture
def lemmatizer():
    return SmartLemmatizer()

def test_single_sentence(lemmatizer):
    text = "Dogs are barking loudly."
    result = lemmatizer.lemmatize_text(text)
    assert result == [['dog', 'be', 'bark', 'loudly', '.']]

def test_multiple_sentences(lemmatizer):
    text = "The children are playing. They love to run."
    result = lemmatizer.lemmatize_text(text)
    assert result == [['The', 'child', 'be', 'play', '.'], ['They', 'love', 'to', 'run', '.']]

def test_empty_string(lemmatizer):
    text = ""
    result = lemmatizer.lemmatize_text(text)
    assert result == []

def test_punctuation_only(lemmatizer):
    text = "?!.,"
    result = lemmatizer.lemmatize_text(text)
    assert result == [['?', '!', '.', ',']]

