import json
import string
from googletrans import Translator, constants
from pprint import pprint


def kwArt():

    with open("../json/articles.json") as dict_article:

        articles = json.load(dict_article)
        article_kw = {}
        for i in articles:
            article_kw[i] = articles[i]["keywords"]
    dict_article.close()

# TRANSLATE USING GOOGLE API THE KEYWORDS GIVEN
    translator = Translator()
    # translate spanish keywords to english from article and lower all the letters
    for article in articles:
        articles_list = []
        for value in articles[article]['keywords']:
            translation = translator.translate(value)
            text_eng = (translation.text)
            for c in string.punctuation:
                text_eng = text_eng.replace(c, '')
            temp = text_eng.split()
            text_eng = [ele for ele in temp if len(ele) > 2]
            text_eng = ' '.join(text_eng)
            if len(text_eng) > 0:
                articles_list.append(text_eng.lower())
            # print(text_eng)
        articles[article] = articles_list
        
    return articles
