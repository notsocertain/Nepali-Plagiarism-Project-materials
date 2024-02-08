import string
import nltk
class tokenize:
    def __init__(self):
        pass
    def word_tokenize(self,text):
        self.text = text
        import string
        punctuations = list(string.punctuation)
        # Add the Nepali purnabiram to the list of punctuations
        punctuations.append("।")
        for punctuation in punctuations:
            self.text = self.text.replace(punctuation, ' ')
        self.text = self.text.strip().split()
        return self.text
    
    def __str__(self):
        return "return the tokenized text removing the punctuations"