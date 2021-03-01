from pytube import Playlist
from pytube import YouTube

print("Playlist or a Video")
print("\t1 for playlist\n\t2 for video")
userInput = int(input("What do you want to do?: "))
if userInput == 1:
    try:
        #https/playlist?list=PLNPxoPbcEcXvtm4jpsC7ZIeHmhqnheNEt
        URL = input("Paste URL Here: ")
        playlist = Playlist(URL)
        print(f'Downloading: {playlist.title}')

        for video in playlist.videos:
            print(f'Downloading: {video.title}')
            video.streams.first().download()
        print("\nDownload has completed!")
    except:
        print("\nDownload hasn't completed!, Please check URL!")
else:
    try:
        #https://www.youtube.com/watch?v=v3gcXj9k4k8&ab_channel=LearningLad
        URL = input("Paste URL Here: ")
        video = YouTube(URL)
        print(f'Downloading: {video.title}')
        video.streams.first().download('../Desktop')
        print("\nDownload has completed!")
    except:
        print("\nDownload hasn't completed!, Please check URL!")
