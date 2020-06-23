import functions as f

words = f.divide_by_words()


# sums = f.get_sums(words)


# f.summarize_articles(words)

sums = f.get_sums(words)
# f.summarize_articles_v2(sums)

f.search_by_vec(sums)


# print (summ)
# f.search_by_vec(sums)

# f.search_by_vec_v3(words)


# for article in words:
#     vector = f.np.ndarray(300)
#     l = words.index(article)
#     vector += sums[l]
#     print(type(vector))
#     out = f.model.similar_by_vector(vector = vector, topn=1)
#     print (out)
#     vector = None

# f.summarize_articles(f.get_sums(words))

print ('Ok')