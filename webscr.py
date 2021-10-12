import requests
from bs4 import BeautifulSoup
from video import *
import json

def encodeTittle(tittle, encoding, removeFinal, removeInitial):
    encodedTittle = tittle.encode(encoding)
    encodedTittle = str(encodedTittle)
    encodedTittle = encodedTittle[:-removeFinal]
    encodedTittle = encodedTittle[removeInitial:]
    return encodedTittle

def getVideos():
    videos = ['https://www.youtube.com/watch?v=PGlaDTSG_Es',
    'https://www.youtube.com/watch?v=-imUMC13sMQ',
    'https://www.youtube.com/watch?v=aN3pPkFqPlc',
    'https://www.youtube.com/watch?v=Z5LMSt-CxAY']

    pages = []
    for video in videos:
        page = requests.get(video)
        pages.append(page)

    returnVideos = []
    for page in pages:
        soup = BeautifulSoup(page.content, 'html.parser')
        tittle = soup.select_one('meta[itemprop="name"][content]')['content']
        views = soup.select_one('meta[itemprop="interactionCount"][content]')['content']

        try:
            encodedTittle = encodeTittle(tittle,'iso-8859-8', 1, 2)
            addVideo = Video(encodedTittle,views,videos[pages.index(page)])
        except:
            encodedTittle = encodeTittle(tittle,'utf-8', 33, 2)
            addVideo = Video(encodedTittle,views,videos[pages.index(page)])

        returnVideos.append(addVideo)

    return returnVideos