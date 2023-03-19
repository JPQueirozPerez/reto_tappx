import json

# GUARDAMOS EN LA VARIABLE ARTICLE_KW EL DICCIONARIO CON EL ID Y SUS KEYWORDS
with open("articles.json") as dict_article:
    articles = json.load(dict_article)
    article_kw = {}
    for i in articles:
        article_kw[i] = articles[i]["keywords"]
    # print(article_kw)
dict_article.close()

# GUARDAMOS EN LA VARIABLE VIDEOS_KW EL DICCIONARIO CON EL ID Y SUS KEYWORDS
with open("videos.json") as dict_videos:
    print("hola")
    videos = json.load(dict_videos)
    videos_kw = {}
    for i in videos:
        videos_kw[i] = videos[i]["keywords"]
    print(videos_kw)
dict_article.close()