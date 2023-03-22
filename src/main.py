from kwArtcl import *
from kwVideos import *
import categories
import json

categories = categories.list_categories()
print(categories)

articles = kwArt()
print(articles)

#videos = kwVideos()
#print(videos)


def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)


# Example
#data = categories
#data['key'] = 'value'

#writeToJSONFile('./','file-name2',data)
