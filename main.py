import fucking_shit as f


doc = 'Хоббит.txt'
# doc1 = 'Конституция старая UTF-8.txt'

f.preprocess(doc, '\.[\n ]')

f.search(doc, 'танцевать_VERB')