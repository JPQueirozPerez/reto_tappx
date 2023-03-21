from kwArtcl import *
from kwVideos import *
import categories

categories = categories.list_categories()
print(categories)

articles = kwArt()
print(articles)

videos = kwVideos()
print(videos)
