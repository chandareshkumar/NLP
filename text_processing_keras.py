from keras.preprocessing.text import text_to_word_sequence
from keras.preprocessing.text import one_hot
from keras.preprocessing.text import Tokenizer

text = 'The qui?ck? brown fox jumped over the lazy dog.'

result= text_to_word_sequence(text)


# splits the words by space
# Filters punctuation
# converts to lower case(lower=True)


print(result)


# Encoding with one hot

# Each word in vocabulary is assinged with unique integer
# convert to lower case, filter out punctuation, and split words based on white space.
# vocabulary size need to be specified. This defines hashing size



# estimate the size of the vocabulary
words = set(text_to_word_sequence(text))

vocab_size = len(words)
print(vocab_size)
# integer encode the document
result = one_hot(text, round(vocab_size*2.3)) 
print(result)



docs = ['Well done!',
'Good work', 'Great work', 'nice work work', 'Excellent!']

# create the tokenizer
t = Tokenizer()
# fit the tokenizer on the documents
t.fit_on_texts(docs)



print(t.word_counts). # dict - returns the count of words
print(t.document_count) # count of total doc
print(t.word_index) # dict - index of words
print(t.word_docs). # dict - count of words, how many documents each appeared in



encoded_docs = t.texts_to_matrix(docs, mode='count') 
print(encoded_docs)