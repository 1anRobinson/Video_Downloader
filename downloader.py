"""
6/24/2022

@author: Ian Robinson
"""
from pytube import YouTube
#import os

print('Welcome to the video downloader by Ian Robinson!')
path = input('Please specify the desintation of your download: ') # path to directory they want to store video
url = input('Paste URL here: ') #get the link as input from user
while "www.youtube.com/watch?v=" not in url: # keep looping if url is invalid
    url = input('Invalid URL. Try Again or press \"E\" to exit: ')
    if url == 'E':
        exit()
    
video = YouTube(url) # store the url of the type YouTube into variable

print('\n*****************Video***********************')
print(video.title) #get and print Youtube Title
print('Size: ', video.streams.get_highest_resolution().filesize,'MB')
response = input('Continue with download? [Y/N]: ')
if response == 'y' or response == 'Y':
    video = video.streams.get_highest_resolution() #set stream resolution
    video.download(path)
elif response == 'n' or response == 'N':
    print('Got it. Thank you for using the video downloader!')
    exit()