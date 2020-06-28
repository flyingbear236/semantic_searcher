import gensim
import numpy as np
import re
from sklearn.preprocessing import normalize



model = gensim.models.KeyedVectors.load_word2vec_format('model.bin', binary=True)

if model:
    print ('Vectors loaded...')
else: 
    print ('Damn! Vectors not found')

# doc = 'vectors/c_old_ready copy.txt'


def change(doc, divider):
    inp = open(doc, 'r').read()
    new = re.sub(divider + '+', divider, inp)
    new = re.sub(divider, ' qwerty ', new)
    # new = re.sub('qwerty' + '{2,5}', 'hui', new)
    new = re.sub('\s+', '', new, 1)
    new = re.sub('\W', ' ', new)
    new = re.sub(' +', ' ', new)
    out = open('aux ' + doc, 'w')
    out.write(new)
    # return(new)


def divide_1D(textline):
    # text_1D = open(doc).read()
    text_1D = re.split(' qwerty'+'\w*'+'\s*', textline)
    if text_1D[-1] == '':
        text_1D.remove(text_1D[-1])
    return text_1D


# def divide_1D(doc):
#     text_1D = open(doc).read()
#     text_1D = re.split(' qwerty'+'\w*'+'\s*', text1D)
#     return text_1D
    
def divide_2D(text_1D):
    text_2D = []
    for article in text_1D:
        text_2D.append([word for word in article.split(' ')])

    return text_2D

def stem(doc):
    doc_changed = 'aux ' + doc
    import process as p
    p.stem(textfile = doc_changed)


doc = 'Конст.txt'



# change(doc, 'Статья')

# stem(doc)

raw = open('aux ' + doc).read()

raw = divide_1D(raw)
# copyraw = raw
raw = divide_2D(raw)

# k = open('test hobo.txt', 'w')
# k.write(str(raw))
# k.close()
# это проверка обычного 2д списка

stemmed_raw = open('stemmed aux '+ doc).read()

stemmed_raw = divide_1D(stemmed_raw)
stemmed_raw = divide_2D(stemmed_raw)

# k = open('test hobo stem.txt', 'w')
# k.write(str(stemmed_raw))
# k.close()
# это проверка стиммированного 2д списка




# print(c)











def get_sums(text_2D):
    sums = []
    

    for article in text_2D:  
        sum1 = np.ndarray(300)
        # i = 0
        for word in article:
            if word in model:
                # i += 1
                vector = model.get_vector(word)
                sum1 =  np.add(sum1, vector)
        # sum1 = np.divide( sum1 , len(article)) 
        sums.append(sum1)
    sums = np.vstack(sums)
    np.savetxt('saved.txt', sums)
    # sums = normalize(sums)
    return sums

sums = get_sums(stemmed_raw)
print(sums.shape)

# def closest_from_sums(sums):
#     i = 0
#     for row in sums:
#         i += 1
#         list_of_tuples = model.similar_by_vector(vector=row, topn=1) 
#         print  ('статья {}'.format(i))
#         print (list_of_tuples[0])





# for vec in sums:
#     k = model.similar_by_vector(vec, topn =1)
#     print (k)

def search_search(word, sums = sums, raw = raw):   
    cosines = model.cosine_similarities(model.get_vector(word), sums)
    print (type(cosines))
    print (cosines.shape)
    cos_s = cosines.copy()
    cos_s.sort()
    index = np.where(cosines == cos_s[-1])
    print ('Нашлась хуйня номер ', str(index[0])[1:-1])
    print (index)
    print ('ok')
    print (raw[int(str(index[0])[1:-1])])

search_search('ребенок_NOUN')
print('========================================')


def search_by_vec(doc, word):
    sums = open(doc, 'r').readlines()
    sums1 = []
    for vec in sums:
        vec = [float (vec) for vec in re.split(" ", vec)]
        sums1.append(vec)
    sums = np.vstack(sums1)    
    cosines = model.cosine_similarities(model.get_vector(word), sums)
    cos_s = cosines.copy()
    cos_s.sort()
    index = np.where(cosines == cos_s[-1])
    print (index)

    return int(str(index[0])[1:-1])

vectores = 'saved.txt'
word = 'ребенок_NOUN'

qw = search_by_vec(vectores, word)

print (raw[qw])

print ('===============================================')

# def search_by_vec_v3(text_2D, word):
#     sums = []
#     sum1 = np.empty(300)
#     for article in text_2D: 
#         for word in article:
#             if word in model:
#                 vector = model.get_vector(word)
#                 sum1 += vector
#         # sum1 = sum1 / len(article)  
#         sums.append(sum1)
#     sums = np.vstack(sums)
#     cos = model.cosine_similarities(model.get_vector('ребенок_NOUN'), sums)
#     print(type(cos))
#     cos_s = cos.copy()
#     cos_s.sort()
#     index = np.where(cos == cos_s[-1])
#     print (index, 'Yay2')
#     return int(str(index[0])[1:-1]) + 1

# # word = 'ребенок_NOUN'

# k = search_by_vec_v3(stemmed_raw, word= word)
# print(raw[k])











# word = 'природа_NOUN'

# doc = 'Конституция старая UTF-8.txt'
# search(doc, word)

# fix_sums(doc)
# preprocess(doc, 'Статья')
# search(doc, 'банк_NOUN')
# search_by_vec




# print(help(model))




# words = ['день_NOUN', 'ночь_NOUN', 'человек_NOUN', 'семантика_NOUN', 'студент_NOUN', 'студент_ADJ']

# def find_similar(words=words):
#     for word in words:
#     # есть ли слово в модели? Может быть, и нет
#         if word in model:
#/             print(word)
#             # выдаем 10 ближайших соседей слова:
#             for i in model.most_similar(positive=[word], topn=10):
#                 # слово + коэффициент косинусной близости
#                 print(i[0], i[1])
#             print('\n')
#         else:
#             # Увы!
#             print(word + ' is not present in the model')


