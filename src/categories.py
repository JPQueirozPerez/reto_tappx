import json

categories = set(())

with open('../json/articles.json') as f:

    articles = json.load(f)

    for i in articles:
        categoryList = articles[i]["categoriaIAB"]
        for j in range(len(categoryList)):
            category = str(categoryList[j]["class"])
            if category not in categories:
                categories.add(category) 
    f.close()

print(categories)
