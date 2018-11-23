from numpy import array
from numpy import asarray
from numpy import zeros

from keras.preprocessing.text import Tokenizer, text_to_word_sequence
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Embedding





def open_glove():
	
	embeddings_file = open('./glove.6B/glove.6B.100d.txt',encoding="utf8")
	embeddings_index_glove = dict()
	for line in embeddings_file:
		values = line.split()
		word = values[0]
		coefs = asarray(values[1:], dtype='float32')
		embeddings_index_glove[word] = coefs
	embeddings_file.close()
	print('Loaded %s word vectors.' % len(embeddings_index_glove))
	return embeddings_index_glove


def embedd (text):	
	#tokenizer = Tokenizer(num_words=None, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~', lower=True, split=' ', char_level=False)
	#tokenizer.fit_on_texts(text)
	tokenizer = text_to_word_sequence(text, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~', lower=True, split=' ')
	#vocab_size = len(tokenizer.word_index) + 1
	#text_encoded = tokenizer.texts_to_sequences(text)
	return tokenizer#text_encoded

def embedd_with_glove(tokenizer, embeddings_index_glove):
	#print(len(tokenizer.word_index))
	#embeddings_current = zeros((len(tokenizer.word_index)+1, 100))
	embeddings_current = zeros((len(tokenizer)+1, 100))
	#print(tokenizer)
	for word in tokenizer:
		print(embeddings_current)
		embeddings_vector = embeddings_index_glove.get(word)
		if embeddings_vector is not None:
			embeddings_current[tokenizer.index(word)] = embeddings_vector
	return embeddings_current

def embedd_this(text):
	global embeddings_index_glove
	global tokenizer
	global embeddings_current
	open_glove()
	embedd(text)
	return embedd_with_glove()
	
