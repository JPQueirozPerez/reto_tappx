import json
from googletrans import Translator, constants

def kwArt():
    with open("../json/articles.json") as dict_article:
        articles = json.load(dict_article)
        article_kw = {}
        for i in articles:
            article_kw[i] = articles[i]["keywords"]
    dict_article.close()

# TRANSLATE USING GOOGLE API THE KEYWORDS GIVEN
    translator = Translator()
    # translate a spanish text to english keywords from article and lower all the letters
    for article in articles:
        articles_list =[]
        for value in articles[article]['keywords']:
            translation = translator.translate(value)
            text_eng = (translation.text)
            articles_list.append(text_eng.lower())
        articles[article] = articles_list
        # print(articles_list)
    return articles