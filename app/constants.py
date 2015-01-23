import os

HOME = os.path.expanduser("~")
BINARY_FILE_PATH = HOME + '/' + os.environ.get('BINARY_PATH').strip('/')

small_test_rel_pronouns = ["that","who","which","what","where","whose"]
prepositions_basic = ["as","at","but","by","down","for","from","in","into","like","near","next","of","off","on","onto","out","over","past","plus","minus","since","than","to","up","with"]
prepositions_advanced = ["aboard","about","above","across","after","against","along","around","before","behind","below","beneath","beside","between","beyond","during","except","following","inside","minus","onto","opposite","outside","round","since","through","toward","under","underneath","unlike","until","upon","without"]
determinators = ["the","a","an"]
prepositions_bnc = ['by', 'through', 'with', 'from', 'of', 'for', 'without', 'out', 'at', 'as', 'in', 'on', 'like', 'about', 'after', 'during', 'into', 'before', 'over', 'despite', 'around', 'against', 'between', 'under', 'beyond', 'until', 'via', 'within', 'since', 'upon', 'among', 'across', 'unlike', 'than', 'near', 'outside', 'towards', 'behind', 'up', 'because', 'per', 'above', 'alongside', 'inside', 'except', 'en', 'throughout', 'off', 'along', 'toward', 'amid', 'instead', 'whereas', 'besides', 'beside', 'beneath', 'past'] # '\xe2\x80\x94'

insigwords = set(small_test_rel_pronouns + prepositions_basic + prepositions_advanced + determinators + prepositions_bnc)

# test = ['animal loves milk','a cat']
