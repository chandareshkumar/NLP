import string
import re
from os import listdir
from nltk.corpus import stopwords
from keras.preprocessing.text import Tokenizer
from keras.utils.vis_utils import plot_model
from keras.models import Sequential
from keras.layers import Dense
from pandas import DataFrame
from matplotlib import pyplot


def load_doc(filename):

	file = open(filename, 'r')
	text = file.read()
	file.close()
	return text

def create_tokenizer(lines):
  tokenizer = Tokenizer()
  tokenizer.fit_on_texts(lines)
  return tokenizer	

def clean_doc(doc):
	
	tokens = doc.split()
	re_punc = re.compile('[%s]' % re.escape(string.punctuation))
	tokens = [re_punc.sub('', w) for w in tokens]
	tokens = [word for word in tokens if word.isalpha()]
	stop_words = set(stopwords.words('english'))
	tokens = [w for w in tokens if not w in stop_words]
	tokens = [word for word in tokens if len(word) > 1]
	return tokens

def doc_to_line(filename, vocab):
  
	doc = load_doc(filename)

	tokens = clean_doc(doc)

	tokens = [w for w in tokens if w in vocab] 

	return ' '.join(tokens)


def process_docs(directory, vocab, is_train):
	lines = list()
	
	
	for filename in listdir(directory):
	
		if is_train and filename.startswith('cv9'): 
	

			continue	


		if not is_train and not filename.startswith('cv9'): 
		
			continue

		path = directory + '/' + filename # load and clean the doc
		line = doc_to_line(path, vocab)

		lines.append(line)

	#print(t,f)	
	return lines



def load_clean_dataset(vocab, is_train):
	
	neg = process_docs('/Users/chand/Documents/txt_sentoken/neg', vocab, is_train)
	pos = process_docs('/Users/chand/Documents/txt_sentoken/pos', vocab, is_train)
	docs = neg + pos
	# prepare labels
	labels = [0 for _ in range(len(neg))] + [1 for _ in range(len(pos))] 
	return docs, labels




def define_model(n_words):

	model=Sequential()
	model.add(Dense(50,input_shape=(n_words,),activation='relu'))
	model.add(Dense(1,activation='sigmoid'))

	model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
	model.summary()
	plot_model(model,to_file='model.png',show_shapes=True)
	return model

def evaluate_mode(Xtrain, ytrain, Xtest, ytest):
  scores = list()
  n_repeats = 10
  n_words = Xtest.shape[1]
  for i in range(n_repeats):
    # define network
    model = define_model(n_words)
    # fit network
    model.fit(Xtrain, ytrain, epochs=10, verbose=0)
    # evaluate
    _, acc = model.evaluate(Xtest, ytest, verbose=0) 
    scores.append(acc)
    print('%d accuracy: %s' % ((i+1), acc))
  return scores


def prepare_data(train_docs, test_docs, mode):
  # create the tokenizer
  tokenizer = Tokenizer()
  # fit the tokenizer on the documents
  tokenizer.fit_on_texts(train_docs)
  # encode training data set
  Xtrain = tokenizer.texts_to_matrix(train_docs, mode=mode)
  # encode training data set
  Xtest = tokenizer.texts_to_matrix(test_docs, mode=mode)
  return Xtrain, Xtest




def predict_sentiment(review, vocab, tokenizer, model):
  # clean
	tokens = clean_doc(review)
	# filter by vocab
	tokens = [w for w in tokens if w in vocab] # convert to line
	line = ' '.join(tokens)
	# encode
	encoded = tokenizer.texts_to_matrix([line], mode='binary') # predict sentiment
	yhat = model.predict(encoded, verbose=0)
	# retrieve predicted percentage and label
	percent_pos = yhat[0,0]
	if round(percent_pos) == 0:
		return (1-percent_pos), 'NEGATIVE' 
	return percent_pos, 'POSITIVE'

# load the vocabulary
vocab_filename = '/Users/chand/Documents/git_NLP/NLP/vocab.txt'
vocab = load_doc(vocab_filename)
vocab = set(vocab.split())

modes = ['binary', 'count', 'tfidf', 'freq']




# load all reviews
train_docs, ytrain = load_clean_dataset(vocab, True) 
test_docs, ytest = load_clean_dataset(vocab, False)


results=DataFrame()
for mode in modes:
  # prepare data for mode
  Xtrain, Xtest = prepare_data(train_docs, test_docs, mode)
  # evaluate model on data for mode
  results[mode] = evaluate_mode(Xtrain, ytrain, Xtest, ytest)


#print(results.describe())


tokenizer = create_tokenizer(train_docs)
# encode data
Xtrain = tokenizer.texts_to_matrix(train_docs, mode='binary')
Xtest = tokenizer.texts_to_matrix(test_docs, mode='binary')
# define network
n_words = Xtrain.shape[1]
model = define_model(n_words)
# fit network
model.fit(Xtrain, ytrain, epochs=10, verbose=2)

# test positive text
text = 'Best movie ever! It was great, I recommend it.'
percent, sentiment = predict_sentiment(text, vocab, tokenizer, model) 
print('Review: [%s]\nSentiment: %s (%.3f%%)' % (text, sentiment, percent*100)) 

# test negative text
text = 'This is a bad movie.'
percent, sentiment = predict_sentiment(text, vocab, tokenizer, model) 
print('Review: [%s]\nSentiment: %s (%.3f%%)' % (text, sentiment, percent*100))



