from gensim.models import KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity

#Returns a dictionary with every keyword punctuated with every category via word2vec
def punctuate_artcls(dict_artcl, categories):
	word_vectors = KeyedVectors.load_word2vec_format('/Users/ggispert/Desktop/keyed/GoogleNews-vectors-negative300.bin.gz', binary=True)
	for artcl in dict_artcl:
		dict_aux = {}
		for cat in categories:
				dict_aux[cat] = float(0)
		for kw in dict[artcl]:
			v_kw = 0
			for kw_pt in kw.split():
				if len(kw_pt > 2)
					v_kw += word_vectors[kw_pt]
			for cat in categories:
				v_cat = 0
				for cat_pt in cat.split():
					if len(cat_pt) > 2:
						v_cat += word_vectors[cat_pt]
				dict_aux[cat] += float(cosine_similarity([v_kw], [v_cat]))
		for cat in categories:
			dict_aux[cat] /= len(dict_artcl[artcl])
		dict_artcl[artcl] = dict_aux
	return dict_artcl
