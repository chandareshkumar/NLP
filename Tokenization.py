from urllib.request import urlopen
url = "http://www.gutenberg.org/files/2554/2554.txt"

raw = urlopen(url).read()

#Process of breaking string into words and punctuations are called tokenization

tokens = nltk.word_tokenize(raw)

#tokens is list

print(tokens[:10])