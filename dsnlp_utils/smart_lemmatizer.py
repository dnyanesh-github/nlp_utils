import nltk
from nltk import pos_tag, word_tokenize
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer


class SmartLemmatizer:
    """
    A reusable, production-ready lemmatizer that tokenizes a sentence,
    POS-tags each token, converts POS tags to WordNet format,
    and returns lemmatized tokens.
    """

    def __init__(self):
        """Initialize the WordNet lemmatizer."""
        self.lemmatizer = WordNetLemmatizer()

    @staticmethod
    def get_wordnet_pos(treebank_tag):
        """
        Convert Treebank POS tags to WordNet POS tags.

        Parameters:
            treebank_tag (str): POS tag from nltk.pos_tag

        Returns:
            str: WordNet-compatible POS tag
        """
        if treebank_tag.startswith('J'):
            return wordnet.ADJ
        elif treebank_tag.startswith('V'):
            return wordnet.VERB
        elif treebank_tag.startswith('N'):
            return wordnet.NOUN
        elif treebank_tag.startswith('R'):
            return wordnet.ADV
        else:
            return wordnet.NOUN  # Default to noun

    def lemmatize_sentence(self, sentence):
        """
        Tokenize, POS-tag, and lemmatize a sentence.

        Parameters:
            sentence (str): The input sentence.

        Returns:
            List[str]: List of lemmatized tokens.
        """
        tokens = word_tokenize(sentence.lower())
        pos_tags = pos_tag(tokens)
        lemmatized = [self.lemmatizer.lemmatize(word, self.get_wordnet_pos(pos))
                      for word, pos in pos_tags]
        return lemmatized

    def lemmatize_text(self, text):
        """
        Lemmatize multiple sentences.

        Parameters:
            text (str): Full text (can contain multiple sentences).

        Returns:
            List[List[str]]: A list of lemmatized token lists for each sentence.
        """
        sentences = nltk.sent_tokenize(text)
        return [self.lemmatize_sentence(sentence) for sentence in sentences]


# Example usage:
if __name__ == "__main__":
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('wordnet')
    nltk.download('omw-1.4')

    lemmatizer = SmartLemmatizer()
    sample_text = "The children are playing happily in the gardens. They have been running fast."
    result = lemmatizer.lemmatize_text(sample_text)
    for sentence in result:
        print(sentence)
