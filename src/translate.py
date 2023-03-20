import json
import goslate

with open('../json/articles.json') as f:

    articles = json.load(f)

    categories = []
    gs = goslate.Goslate() 

    for i in articles:
        categoryList = articles[i]["categoriaIAB"]
        #category = gs.translate(categoryList[0].values(), 'es')
        for j in range(len(categoryList)):
            category = categoryList[j].values()
            category = gs.translate(categoryList[j].values(), 'es')
            categories.append(category) if category not in categoryList else categoryList
    print(categories)

    f.close()
