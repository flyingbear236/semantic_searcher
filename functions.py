from datetime import datetime

begin_time = datetime.now()

import gensim
import numpy as np
import re
from sklearn.preprocessing import normalize



model = gensim.models.KeyedVectors.load_word2vec_format('model.bin', binary=True)

if model:
    print ('Vectors loaded...')
else: 
    print ('Damn! Vectors not found')


def change(doc, divider):
    inp = open(doc, 'r').read()
    new = re.sub(divider + '+', divider, inp)
    new = re.sub(divider, ' qwerty ', new)
    new = re.sub('[0-9]', '', new)
    new = re.sub('\s+', '', new, 1)
    new = re.sub('\W', ' ', new)
    new = re.sub(' +', ' ', new)
    out = open('aux ' + doc, 'w')
    out.write(new)


def divide_1D(textline):
    text_1D = re.split(' qwerty'+'\w*'+'\s*', textline)
    if text_1D[-1] == '':
        text_1D.remove(text_1D[-1])
    return text_1D



    
def divide_2D(text_1D):
    text_2D = []
    for article in text_1D:
        text_2D.append([word for word in article.split(' ')])

    return text_2D

def stem(doc):
    doc_changed = 'aux ' + doc
    import process as p
    p.stem(textfile = doc_changed)



def get_sums(text_2D):
    sums = []
    output1 = output[:]
    ia = 0
    for article in text_2D: 
        ia += 1 
        # sum1 = []
        sum1 = np.empty(300)
        i = 0
        for word in article:
            if word in model:     
                i += 1
                vector = model.get_vector(word)
                sum1 += vector
                # sum1.append(vector)
        if i == 0:
            # print (ia)
            # raw.remove(raw[ia])
            # print(ia)
            # sum1 = []
            output.remove(output1[text_2D.index(article)])
            # print ('!')
        else:   
            # sum1 = np.vstack(sum1)
            # sum1 = normalize(sum1)
            # sum1 = np.mean(sum1, axis = 0)
            # sum1 = np.sum(sum1, axis = 0)
            sum1 = np.divide(sum1 , i) 
            # sum1 = sum1 / i
            sums.append(sum1)
        
    sums = np.vstack(sums)
    
    # sums = normalize(sums)
    return sums

def sums_as_words(sums):
    i = 0
    for row in sums:
        i += 1
        list_of_tuples = model.similar_by_vector(vector=row, topn=1) 
        print  ('статья {}'.format(i))
        print (list_of_tuples[0])

def search(word, sums, n=1):   
    cosines = model.cosine_similarities(model.get_vector(word), sums)
    cos_s = cosines.copy()
    cos_s.sort()
    while np.isnan(cos_s[-1]):
        cos_s = np.delete(cos_s, -1)
        # print ('deleted')
    # print ('cos_s', cos_s[-1])
    out = []
    
    for i in range (-1, -n-1, -1):
        # print ('start')
        # print ('i', i)
        index = np.where(cosines == cos_s[i])
        # print (cos_s[i])
        out.append(int(str(index[0])[1:-1]))
    # print (index)
    return out

def search_in_sums_doc(doc, word, n=1):
    sums = open(doc, 'r').readlines()
    sums1 = []
    for vec in sums:
        vec = [float (vec) for vec in re.split(" ", vec)]
        sums1.append(vec)
    sums1 = np.vstack(sums1)    
    cosines = model.cosine_similarities(model.get_vector(word), sums1)
    cos_s = cosines.copy()
    cos_s.sort()
    while np.isnan(cos_s[-1]):
        cos_s = np.delete(cos_s, -1)
    # np.savetxt('to.txt', cos_s)
    out = []
    for i in range (-1, -n-1, -1):
        index = np.where(cosines == cos_s[i])
        # print (cos_s[i])
        out.append(int(str(index[0])[1:-1]))

    # print (index)

    return out


###
#  runtime instructions 
# 


doc = 'Hobbit.txt'


# change(doc, '\.')

# stem(doc)

raw = open('aux ' + doc).read()

raw = divide_1D(raw)
output = raw[:]

raw = divide_2D(raw)

# k = open('test hobo.txt', 'w')
# k.write(str(raw))
# k.close()
# это проверка обычного 2д списка

stemmed_raw = open('stemmed aux '+ doc).read()

stemmed_raw = divide_1D(stemmed_raw)
print('stemmed', len(stemmed_raw))
stemmed_raw = divide_2D(stemmed_raw)

# k = open('test hobo stem.txt', 'w')
# k.write(str(stemmed_raw))
# k.close()
# это проверка стеммированного 2д списка






sums = get_sums(stemmed_raw)

print ('sums', sums.shape)
print ('output', len(output))

np.savetxt('saved.txt', sums)

# print(sums.shape, 'sums shape')


word = 'жираф_NOUN'


ss = search(word, sums, n=3)
print('=========fresh========divided=======================')
for i in ss:
    print ('Отрывок {}'.format(i))
    print (output[i])



vectores = 'saved copy.txt'


ans = search_in_sums_doc(vectores, word, n=3)

print ('=======from doc=========not divided===============================')
for i in ans:
    print ('Отрывок {}'.format(i))
    print (output[i])

print ('Запрос: ', word , '\n')

print(datetime.now() - begin_time)





