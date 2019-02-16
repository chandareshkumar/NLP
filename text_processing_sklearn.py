
# Learning CountVectorizer
# Learning TfidfVectorizer
# Learning HashingVectorizer



from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer

text = ["The quick brown fox jumped over the lazy dog."]

vectorizer = CountVectorizer()


vectorizer.fit(text). # in order to learn a vocabulary from one or more documents
vector = vectorizer.transform(text) # to encode one or more doc  as a vector.

print(vector.shape)
print(type(vector))
print(vector.toarray())


# checking the tokenization

print(vectorizer.vocabulary_)


text2=["the", "alexander"]


# Encoding the other doc

vector=vectorizer.transform(text2)


print(vector.toarray())


text = ["The quick brown fox jumped over the lazy dog.",
"The lion.",
    "The fox"]

vectorizer=TfidfVectorizer()

vectorizer.fit(text)

# summary

print(vectorizer.vocabulary_)
print(vectorizer.idf_).   # assigns lowest score of 1.0 to the most frequently


# encode document

vector=vectorizer.transform(text)

# summarize encoded vector

print(vector.shape)
print(vector.toarray())      # values are noramalized btw 0 to 1



'''

Counts and frequencies can be very useful, but one limitation of these methods is that the vocabulary can become very large. 
This, in turn, will require large vectors for encoding documents and impose large requirements on memory and slow down algorithms.
 A clever work around is to use a one way hash of words to convert them to integers. 
The clever part is that no vocabulary is required and you can choose an arbitrary-long fixed length vector.'''




text = ["The quick brown fox jumped over the lazy dog."]
vectorizer = HashingVectorizer(n_features=20)

vector=vectorizer.transform(text)

print(vector.shape)
print(vector.toarray())   # values are normalized btw -1 to 1
