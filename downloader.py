from pytube import YouTube

url = input('Paste URL here: ') #get the link as input from user
video = YouTube(url) # variable of ty

print('\n*****************Video Title*****************')
print(video.title) #get and print Youtube Title
