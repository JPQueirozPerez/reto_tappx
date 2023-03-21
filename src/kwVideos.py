import json
from googletrans import Translator, constants

def kwVideos():
    with open("../json/videos.json") as dict_videos:
        videos = json.load(dict_videos)
        videos_kw = {}
        for i in videos:
            videos_kw[i] = videos[i]["keywords"]
        # print(videos_kw)
    dict_videos.close()
    # translate a spanish text to english keywords from article lower all the letters
    translator = Translator()
    for video in videos:
        video_list=[]
        for value in videos[video]['keywords']:
            translation = translator.translate(value)
            text_eng = (translation.text.lower())
            video_list.append(text_eng)
        videos[video] = video_list
        # print(video_list)
    return videos