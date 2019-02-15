
import nltk
import re, string

filename="/Users/chand/Documents/NLP.txt"
file=open(filename,'rt')
text=file.read()
file.close()


# splitting the words based on white spaces and '-'

words = re.split(r'\s+|-', text)


# removing '' spaces from the list

wrd=[]
for w in word:
    if w=='':
        pass
    else:
        wrd.append(w)
    

print(string.punctuation)

re_punc=re.compile('[%s]'%re.escape(string.punctuation))


# replacing the spcl characters with '' 
stripped = [re_punc.sub('', w) for w in wrd]
print(len(stripped))



print(stripped)

