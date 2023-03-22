

def link_srcs(punct_artcl, punct_vid):
	dict1 = {}
	dict2 = {}
	dict3 = {}
	for vid in punct_vid:
		dict2[vid] = [key for key, value in sorted(punct_vid[vid].items(), key=lambda x: x[1], reverse=True)[:6]]
	for artcl in punct_artcl:
		dict3[artcl] = {}
		dict1[artcl] = [key for key, value in sorted(punct_artcl[artcl].items(), key=lambda x: x[1], reverse=True)[:6]]
		for vid in dict2:
			i = 0
			for c in dict2[vid]:
				if c in dict1[artcl]:
					i += 1
			if i > 5:
				dict3[artcl].append(vid)
		if len(dict3[artcl]) < 2:
			for vid in dict2:
				i = 0
				for c in dict2[vid]:
					if c in dict1[artcl]:
						i += 1
				if i > 4 and vid not in dict3[artcl]:
					dict3[artcl][vid] = round(i/6,3)
			if len(dict3[artcl]) < 2:
				for vid in dict2:
					i = 0
					for c in dict2[vid]:
						if c in dict1[artcl]:
							i += 1
					if i > 3 and vid not in dict3[artcl]:
						dict3[artcl][vid] = round(i/6,3)
				if len(dict3[artcl]) < 2:
					for vid in dict2:
						i = 0
						for c in dict2[vid]:
							if c in dict1[artcl]:
								i += 1
						if i > 2 and vid not in dict3[artcl]:
							dict3[artcl][vid] = round(i/6,3)
					if len(dict3[artcl]) < 2:
						for vid in dict2:
							i = 0
							for c in dict2[vid]:
								if c in dict1[artcl]:
									i += 1
							if i > 0 and vid not in dict3[artcl]:
								dict3[artcl][vid] = round(i/6,3)
	return dict3
