import kwArtcl as kA
import kwVideos as kV
import categories as cat
import json

categories = cat.list_categories()
print(categories)

articles = kA.kwArt()
print(articles)

#videos = kV.kwVideos()
#print(videos)


def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)


# Example
#data = categories
#data['key'] = 'value'

#writeToJSONFile('./','file-name2',data)
