import json
from googletrans import Translator, constants
from pprint import pprint

# GUARDAMOS EN LA VARIABLE ARTICLE_KW EL DICCIONARIO CON EL ID Y SUS KEYWORDS
with open("../json/articles.json") as dict_article:
    articles = json.load(dict_article)
    article_kw = {}
    for i in articles:
        article_kw[i] = articles[i]["keywords"]
    # print(article_kw)
dict_article.close()

# GUARDAMOS EN LA VARIABLE VIDEOS_KW EL DICCIONARIO CON EL ID Y SUS KEYWORDS
with open("../json/videos.json") as dict_videos:
    videos = json.load(dict_videos)
    videos_kw = {}
    for i in videos:
        videos_kw[i] = videos[i]["keywords"]
    # print(videos_kw)
dict_article.close()

# init the Google API translator
translator = Translator()
# translate a spanish text to english text (by default)
for article in articles:
    # print(article)
    articles_list =[]
    for value in articles[article]['keywords']:
        translation = translator.translate(value)
        text_eng = (translation.text)
        articles_list.append(text_eng)
    articles[article]['keywords'] = articles_list
    # print(articles.list)


for video in videos:
    print(video)
    video_list=[]
    for value in videos[video]['keywords']:
        translation = translator.translate(value)
        text_eng = (translation.text)
        video_list.append(text_eng)
    videos[video]['keywords'] = video_list
    # print(video_list)
