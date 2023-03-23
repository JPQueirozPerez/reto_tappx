def linker(punct_artcl, punct_vid):

	dict1 = {}
	dict2 = {}
	dict3 = {}
	for vid in punct_vid:
		dict2[vid] = sorted(vid, key=vid.get, reverse=True)[:4]
	for artcl in punct_artcl:
		dict3[artcl] = []
		dict1[artcl] = sorted(artcl, key=artcl.get, reverse=True)[:4]
		for vid in dict2:
			i = 0
			for c in vid:
				if c in dict1[artcl]:
					i += 1
			if i > 2:
				dict3[artcl].append(vid)
