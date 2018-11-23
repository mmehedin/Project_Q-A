import pickle
import os

CURRENT_PATH = '.'
PICKLE_STRUCTURE = os.path.join(CURRENT_PATH, 'pickle_structure.pkl')

def pickle_this(ob, name=PICKLE_STRUCTURE):
	with open(name, 'wb') as st:    #w write   b binary
		return pickle.dump(ob, st)

def unpickle_this(name=PICKLE_STRUCTURE):
	with open(name, 'rb') as st:
		return pickle.load(st)