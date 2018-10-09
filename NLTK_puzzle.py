

import nltk


# forming the possible words using given alphabet

puzzle= nltk.FreqDist('egivrvonl')

mandate='r'

word_list=nltk.corpus.words.words()

puz=[w for w in word_list if mandate in w and nltk.FreqDist(w)<puzzle]


print(set(puz))
