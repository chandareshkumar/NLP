
import nltk

names=nltk.corpus.names

male_names=names.words('male.txt')

female_names=names.words('female.txt')


male_names= [w for w in male_names]

female_names =[w for w in female_names]

print("Male Name ", male_names)
print("Female Name ", female_names)

#gives the freq distribution of last letter in names

cfd = nltk.ConditionalFreqDist( (fileid, name[-1])
								for fileid in names.fileids()
									for name in names.words(fileid))

cfd.plot()