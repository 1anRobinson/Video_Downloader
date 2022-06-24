"""
6/24/2022

@author: Ian Robinson
"""
from pytube import YouTube
import os

print(os.path.expanduser('~/Desktop'))
url = input('Paste URL here: ') #get the link as input from user
while "www.youtube.com/watch?v=" not in url: # keep looping if url is invalid
    url = input('Invalid URL. Try Again or press \"E\" to exit: ')
    if url == 'E':
        exit()
    
video = YouTube(url) # store the url of the type YouTube into variable

print('\n*****************Video Title*****************')
print(video.title) #get and print Youtube Title

video = video.streams.get_highest_resolution() #set stream resolution

video.download(os.path.expanduser('~/Desktop')) #download method that downloads to the desktop