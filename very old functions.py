import gensim
import numpy as np
import re



model = gensim.models.KeyedVectors.load_word2vec_format('model.bin', binary=True)

if model:
    print ('Vectors loaded...')
else: 
    print ('Damn! Vectors not found')

# doc = 'vectors/c_old_ready copy.txt'


def change(doc, divider):
    inp = open(doc, 'r').read()
    new = re.sub(divider, ' qwerty ', inp)
    out = open('aux ' + doc, 'w')
    out.write(new)



def divide_1D(doc, divider = 'qwerty_X'):
    text_1D = open(doc).read().split(divider)
    return text_1D
    
def divide_2D(text_1D):
    text_2D = []
    for article in text_1D:
        # article = article.replace('\n',' ')
        text_2D.append([i for i in article.split(' ') if i in model])
    return text_2D





def get_sums(text_2D):
    sums = []
    sum1 = np.empty(300)
    for article in text_2D:  
        for word in article:
            if word in model:
                vector = model.get_vector(word)
                sum1 += vector
        sum1 = sum1 / len(article)  
        sums.append(sum1)
    sums = np.vstack(sums)
    return sums



def closest_from_sums(sums):
    i = 0
    for row in sums:
        i += 1
        list_of_tuples = model.similar_by_vector(vector=row, topn=1) 
        print  ('статья {}'.format(i))
        print (list_of_tuples[0])


def closest_from_words(text_2D):
    sums = get_sums(text_2D)
    closest_from_sums(sums)
    


def search_by_vec(doc, word):
    doc = 'vectors ' + doc
    sums = open(doc, 'r').read().split(']')
    sums.remove(sums[-1])
    sums1= []
    for vec in sums:
        vec = [float (vec) for vec in re.split(" ", vec)]
        sums1.append(vec)
    sums = np.vstack(sums1)    
    cosines = model.cosine_similarities(model.get_vector(word), sums)
    cos_s = cosines.copy()
    cos_s.sort()
    index = np.where(cosines == cos_s[0])
    print (index)
    return int(str(index[0])[1:-1])

def search(doc, word):
    num = search_by_vec(doc=doc, word=word)
    # print ('Ближе всего статья {}'.format(num+1))
    doc = 'aux ' + doc
    arts = divide_1D(doc, divider = 'qwerty') 
    # print (len(arts))
    print ('Ближе всего статья {}'.format(num-1))
    print (arts[num-1])
    print ('Ближе всего статья {}'.format(num))
    print (arts[num])
    print ('Ближе всего статья {}'.format(num+1))
    print (arts[num+1])
    



def search_by_vec_v3(text_2D):
    sums = []
    sum1 = np.empty(300)
    for article in text_2D: 
        for word in article:
            if word in model:
                vector = model.get_vector(word)
                sum1 += vector
        sum1 = sum1 / len(article)  
        sums.append(sum1)
    sums = np.vstack(sums)
    cos = model.cosine_similarities(model.get_vector('банк_NOUN'), sums)
    print(type(cos))
    cos_s = cos.copy()
    cos_s.sort()
    index = np.where(cos == cos_s[-1])
    print (index, 'Yay2')


    return index


def preprocess(doc, divider):
    change(doc=doc, divider=divider)
    import process as p
    p.stem('aux ' + doc)
    search_base = divide_1D('stemmed aux ' + doc)
    search_base = divide_2D(search_base)
    search_base = get_sums(search_base)
    put_sums_to_file(search_base, doc)
    # fix_sums(doc)
    

def put_sums_to_file(sums, doc):
    f = open('vectors ' + doc, 'w')
    l = []
    for i in sums:
        l.append(str(i))
    f.writelines(sums)
    f.close()


def fix_sums(doc):
    doc = 'vectors ' + doc
    f = open(doc, 'r') 
    sums = f.read()
    sums = re.sub('\[\s+', '', sums)
    sums = sums.replace('[', '')
    sums = sums.replace('\n', '')
    sums = re.sub('\s+]', ']', sums)
    sums = re.sub('\s\s+', ' ', sums)
    f.close()
    k = open(doc, 'w')  
    k.write(sums)



def search(doc, word):
    num = search_by_vec(doc=doc, word=word)
    # print ('Ближе всего статья {}'.format(num+1))
    doc = 'aux ' + doc
    arts = divide_1D(doc, divider = 'qwerty') 
    # print (len(arts))
    print ('Ближе всего статья {}'.format(num-1))
    print (arts[num-1])
    print ('Ближе всего статья {}'.format(num))
    print (arts[num])
    print ('Ближе всего статья {}'.format(num+1))
    print (arts[num+1])
    



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


# def preprocess(doc, divider):
#     change(doc=doc, divider=divider)
#     import process as p
#     p.stem('aux ' + doc)
#     search_base = divide_1D('stemmed aux ' + doc)
#     search_base = divide_2D(search_base)
#     search_base = get_sums(search_base)
#     put_sums_to_file(search_base, doc)
#     # fix_sums(doc)
    

# def put_sums_to_file(sums, doc):
#     f = open('vectors ' + doc, 'w')
#     l = []
#     for i in sums:
#         l.append(str(i))
#     f.writelines(sums)
#     f.close()


# def fix_sums(doc):
#     doc = 'vectors ' + doc
#     f = open(doc, 'r') 
#     sums = f.read()
#     sums = re.sub('\[\s+', '', sums)
#     sums = sums.replace('[', '')
#     sums = sums.replace('\n', '')
#     sums = re.sub('\s+]', ']', sums)
#     sums = re.sub('\s\s+', ' ', sums)
#     f.close()
#     k = open(doc, 'w')  
#     k.write(sums)
