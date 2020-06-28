import re
import gensim
import numpy as np
from sklearn.preprocessing import normalize

model = gensim.models.KeyedVectors.load_word2vec_format('model.bin', binary=True)

def change(doc, divider):
    inp = open(doc, 'r').read()
    new = re.sub(divider, ' qwerty ', inp)
    out = open('aux ' + doc, 'w')
    out.write(new)

def stem(doc):
    doc_changed = 'aux ' + doc
    import process as p
    p.stem(textfile = doc_changed)


def divide(doc):
    f = open(doc)
    text = f.read()
    f.close()
    text = re.sub('\n', ' ', text)
    text = re.sub(' +', ' ', text) 
    text = re.split('qwerty'+'\w*'+'\s*', text)
    return (text)

def divide_2D(text_1D):
    text_2D = []
    for article in text_1D:
        text_2D.append([i for i in article.split(' ') if i in model])
    return text_2D





def fix_sums(doc):
    doc = 'vecs stemmed aux ' + doc 
    numbers = open(doc).read()
    numbers = re.sub(' +', ' ', numbers)
    numbers = re.sub('\[', '', numbers)
    k = open(doc, 'w')
    k.write(numbers)

def read_sums(doc):
    doc = 'vecs stemmed aux ' + doc 
    numbers = open(doc).read()
    numbers = numbers[:-1]
    numbers = numbers.split(']')
    sums = []
    for vector in numbers:
        vector = re.sub('\n', '', vector)
        vector = re.sub('\s+', ' ', vector)
        if vector[0] == ' ':
            vector = vector.replace(' ', '', 1)
        kek = [float(i) for i in re.split(' ', vector) if i]
        sums.append(np.array(kek, dtype = 'float64'))
    sums = np.vstack(sums)
    return sums

model = gensim.models.KeyedVectors.load_word2vec_format('model.bin', binary=True)

def search_by_vec(sums, word):  
    cosines = normalize(model.cosine_similarities(model.get_vector(word), sums))
    print (cosines.shape)
    cos_s = cosines.copy()
    print (cos_s.shape)
    cos_s.sort()
    index = np.where(cosines == cos_s[0])
    print (index)
    return int(str(index[0])[1:-1])





doc = 'Хоббит.txt'
# read_sums(doc)


# change(doc, '\.')
# stem(doc)
d1 = divide('stemmed aux Хоббит.txt')
d2 = divide_2D(d1)
# divide(stemmed aux doc)
l = make_sums(d2)
# fix_sums(doc)

# l = read_sums(doc)
# print (l)
# l = normalize(l)

# word = 'дракон_NOUN'

# search_by_vec(l, word)

# r = open('aux Хоббит copy 3.txt').read().split('\n')
# print (len(r))

# print (r[185])
# print (r[186])
# print (r[187])





    #  if stemmed, divider = qwerty_X
    #  else (changed) divider = qwerty
    # return list(articles)
    # pass

# def get_vecs(articles):
    # for i in articles get_vec()
    # write vecs to vec_doc
    # pass


# workflow

# raw text → changed text
# changed text → stemmed text
# stemmed text → sums txt
#  

