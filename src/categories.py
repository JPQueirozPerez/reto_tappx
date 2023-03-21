import string
import json

def list_categories():

    categories = []

    with open('../json/articles.json') as f:

        articles = json.load(f)

        for i in articles:
            categoryList = articles[i]["categoriaIAB"]
            for j in range(len(categoryList)):
                category = str(categoryList[j]["class"]).lower()
                for c in string.punctuation:
                    category = category.replace(c, '')
                if category not in categories:
                    categories.append(category)
        f.close()

    with open('../json/videos.json') as f:

        articles = json.load(f)

        for i in articles:
            categoryList = articles[i]["categoriaIAB"]
            for j in range(len(categoryList)):
                category = str(categoryList[j]["class"]).lower()
                for c in string.punctuation:
                    category = category.replace(c, '')
                if category not in categories:
                    categories.append(category) 
        f.close()

    return(categories)
