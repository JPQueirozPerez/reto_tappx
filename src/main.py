import kwArtcl as kA
import kwVideos as kV
import categories as cat
import word2vec as w2v
import linker as l
import json


categories = cat.list_categories()
print(categories)

articles = w2v.punctuate_srcs(kA.kwArt(), categories)
#print(articles)

videos = w2v.punctuate_srcs(kV.kwVideos(), categories)
# print(videos)

data = l.link_srcs(articles, videos)


def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)


data = categories
data['key'] = 'value'

writeToJSONFile('../json','json_scores',data)
