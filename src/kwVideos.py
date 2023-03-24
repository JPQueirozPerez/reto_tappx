import json
import string
from googletrans import Translator, constants


def kwVideos():

    with open("../json/videos.json") as dict_videos:

        videos = json.load(dict_videos)
        videos_kw = {}
        for i in videos:
            videos_kw[i] = videos[i]["keywords"]
        # print(videos_kw)
    dict_videos.close()

    # translate a spanish keywords to english from article lower all the letters
    translator = Translator()
    for video in videos:
        video_list = []
        for value in videos[video]['keywords']:
            translation = translator.translate(value)
            text_eng = (translation.text.lower())
            for c in string.punctuation:
                text_eng = text_eng.replace(c, '')
            temp = text_eng.split()
            text_eng = [ele for ele in temp if len(ele) > 2]
            text_eng = ' '.join(text_eng)
            if len(text_eng) > 0:
                video_list.append(text_eng.lower())
        videos[video] = video_list
        
    return videos
