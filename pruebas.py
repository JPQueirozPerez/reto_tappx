from gensim.models import KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity
word_vectors = KeyedVectors.load_word2vec_format('/Users/ggispert/Desktop/keyed/GoogleNews-vectors-negative300.bin.gz', binary=True)
dict = {
	'098' : ['armas', 'balas'],
	'097' : ['submarinos','sumergibles'],
	'2364' : ['cariñosa', 'paparazzi'],
	'2365' : ['química', 'profesor', 'Avogadro']
}
cat = ('educación', 'ciencia', 'tecnología', 'arte', 'entretenimiento', 'noticias')

# dict2 = {}
# dict3 = {}
# for article in dict:
# 	dict2[article] = {}
# 	for keyword in dict[article]:
# 		v_keyword = word_vectors[keyword]
# 		dict2[article][keyword] = {}
# 		for keyword_part in keyword.split()
# 			for category in cat:
# 				v_category = word_vectors[category]
# 				dict2[article][keyword][category] += float(cosine_similarity([v_keyword],[v_category]))

# for article in dict:
# 	dict3[article] = {}
# 	for category in cat:
# 		dict3[article][category] = float(0)
# 		for keyword in dict[article]:
# 			dict3[article][category] += dict2[article][keyword][category]
# 		dict3[article][category] /= len(dict[article])
# print(dict3)
v0 = word_vectors['most']
v1 = word_vectors['valued']
v2 = word_vectors['player']
v3 = word_vectors['nba']
print(v0)
print(v1)
print(v2)
print(v3)
print(cosine_similarity([v0], [v3]))
print(cosine_similarity([v1], [v3]))
print(cosine_similarity([v2], [v3]))
print(cosine_similarity([v1 + v2], [v3]))
print(cosine_similarity([v0 + v2], [v3]))
print(cosine_similarity([v0 + v1], [v3]))
print(cosine_similarity([v0 + v1 + v2], [v3]))
