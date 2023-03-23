from gensim.models import KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity


#Returns a dictionary with every keyword punctuated with every category via word2vec
def punctuate_srcs(dict_srcs, categories):
	word_vectors = KeyedVectors.load_word2vec_format('../corpus/GoogleNews-vectors-negative300.bin.gz', binary=True)
	for src in dict_srcs:
		dict_aux = {}
		for cat in categories:
				dict_aux[cat] = float(0)
		for kw in dict_srcs[src]:
			v_kw = 0
			a = 0
			for kw_pt in kw.split():
				if kw_pt in word_vectors:
					a = 1
					v_kw += word_vectors[kw_pt]
			if a:
				for cat in categories:
					v_cat = 0
					for cat_pt in cat.split():
						if cat_pt in word_vectors:
							v_cat += word_vectors[cat_pt]
					dict_aux[cat] += float(cosine_similarity([v_kw], [v_cat]))
		for cat in categories:
			dict_aux[cat] /= len(dict_srcs[src])
		dict_srcs[src] = dict_aux
	return dict_srcs
