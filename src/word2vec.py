from gensim.models import KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity


# Returns a dictionary with every keyword punctuated with every category via word2vec
def punctuate_srcs(dict_srcs, categories):

	word_vectors = KeyedVectors.load_word2vec_format('/Users/ggispert/Desktop/keyed/GoogleNews-vectors-negative300.bin.gz', binary=True)

	for src in dict_srcs:
		dict_aux = {}
		for cat in categories:
			dict_aux[cat] = float(0)
		for kw in dict[src]:
			v_kw = 0
			for kw_pt in kw.split():
				v_kw += word_vectors[kw_pt]
			for cat in categories:
				v_cat = 0
				for cat_pt in cat.split():
					v_cat += word_vectors[cat_pt]
				dict_aux[cat] += float(cosine_similarity([v_kw], [v_cat]))
		for cat in categories:
			dict_aux[cat] /= len(dict_src[src])
		dict_src[src] = dict_aux

	return dict_srcs
