import string
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer



filename="/Users/chand/Documents/NLP.txt"
file=open(filename,'rt')
text=file.read()
file.close()


# splitting into sentence based on period

sent = nltk.sent_tokenize(text)


# splitting into words -- tokenize


'''

It splits tokens based on white space and punctuation. For example, commas and periods are taken as separate tokens. 
Contractions are split apart (e.g. What’s becomes What and ’s). Quotes are kept, and so on '''

tokens = word_tokenize(text)


# converting to lower case

word=[w.lower() for w in word]


re_punc= re.compile(r'[%s]' % re.escape(string.punctuation))


# searching the punctuation characters


punct=set([w for w in word if re_punc.search(w)])


# Substituting the spcl char with ''


stripped= [re_punc.sub('',w) for w in word]


print(len(stripped))

print(stripped.count(''))



# Taking only alpha numeric characters


words = [word for word in stripped if word.isalpha()]

# filtering stop words

words = [w for w in words if w not in stop_wrds]



porter = PorterStemmer()
stemmed = [porter.stem(word) for word in words]

# stemming the words

print(stemmed)