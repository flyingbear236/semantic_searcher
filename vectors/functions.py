import zipfile
import gensim
import numpy as np



model = gensim.models.KeyedVectors.load_word2vec_format('model.bin', binary=True)

if model:
    print ('Yeet')
else: 
    print ('Damn')

doc = 'vectors/c_old_ready copy.txt'

def divide_articles(doc=doc):
    out = open(doc).read().split('статья_NOUN')
    return out
    
def divide_by_words():
    word_list = []
    for i in range (len(divide_articles())):
        article = divide_articles()[i]
        article = article.replace('\n',' ')
        word_list.append([i for i in article.split(' ')])
    return word_list


def get_sums(word_list):
    out = []
    sum1 = np.empty(300)
    for article in word_list:  
        for word in article:
            if word in model:
                vector = model.get_vector(word)
                sum1 += vector
        sum1 = sum1 / len(article)  
        out.append(sum1)
    out = np.vstack(out)
    return out



def closest_from_sums(sums):
    i = 0
    for row in sums:
        i += 1
        list_of_tuples = model.similar_by_vector(vector=row, topn=1) 
        print  ('статья {}'.format(i))
        print (list_of_tuples[0])


def closest_from_words(words):
    sums = get_sums(words)
    closest_from_sums(sums)
    

def search_by_vec(sums):
    cosines = model.cosine_similarities(model.get_vector('космос_NOUN'), sums).tolist()
    cosines_s = cosines[:]
    cosines_s.sort()
    i = 0
    for val in cosines:
        i += 1
        if val == cosines_s[0]:
            print ('Yay!')
            print ('Ближе всего статья {}'.format(i))
        


def search_by_vec_v3(words):
    sums = []
    for article in words:
        
        sum1 = np.ndarray(300)
        for word in article:
            if word in model:
                vector = model.get_vector(word)
                sum1 += vector
        sum1 = sum1 / len(article)
        sums.append(sum1)
    sums = np.stack(sums, axis = 1)
    print (type(sums))
    print (sums.shape)









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


