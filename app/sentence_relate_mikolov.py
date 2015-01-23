from __future__ import with_statement
from numpy import linalg as LA
import re
import numpy
import scipy
import scipy.spatial
import scipy.stats as sstats
import shelve
import linecache
from gensim.models import Word2Vec
from constants import *

vspace = Word2Vec.load_word2vec_format(BINARY_FILE_PATH, binary=True)  # C binary format

def returnPossibleKeys(sentenceString):
	# print [x for x in sentenceString.split() if (x.lower() not in insigwords)]
	return [x for x in sentenceString.split() if (x.lower() not in insigwords)]

# this is the additive model, but usually it works well
def verySimpleModelMikolov(sentence1,sentence2):
	bagS1 = returnPossibleKeys(sentence1.strip())
	bagS2 = returnPossibleKeys(sentence2.strip())
	if len(bagS1) == 0 or len(bagS2) == 0:
		print "111"
		return -2
	else:
		try:
			sVector1 = vspace[bagS1[0]]
			for ss in bagS1[1:]:
				try:
					sVector1 = numpy.add(sVector1,vspace[ss])
				except:
					pass
			sVector2 = vspace[bagS2[0]]
			for ss in bagS2[1:]:
				try:
					sVector2 = numpy.add(sVector2,vspace[ss])
				except:
					pass
			try:
				cos = scipy.spatial.distance.cosine(sVector1,sVector2)
				#print cos
				return cos
			except:
				return -4
		except:
			return -3

#print verySimpleModelMikolov(test[0],test[1])
