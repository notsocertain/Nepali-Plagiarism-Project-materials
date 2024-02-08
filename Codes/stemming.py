import snowballstemmer
class stemming:

    def __init__(self) -> None:
        self.stemmer = snowballstemmer.NepaliStemmer()
    
    def word_stemmer(self, text):
        self.text = text 
        if isinstance(self.text, str):
            return self.stemmer.stemWords(self.text.split())
        return self.stemmer.stemWords(self.text)

    def __str__(self):
        return "stemmization is done in nepali words and return the list or stemmized words"