# sources : https://pytube.io/en/latest/

from pytube import YouTube

path = "/Users/Jakub/Desktop/YT_Downloads"

URL = input("Enter URL of the video you want to download : ")
yt = YouTube(URL, use_oauth=False, allow_oauth_cache=True) # bypass age restrictions and access private videos
Itags = yt.streams.all()

for i in Itags:
    print(i)
yt.streams.get_by_itag(int(input("Itag: "))).download(path)

print("'" + yt.title + "' has been downloaded.")
print("Thumbnail : " + yt.thumbnail_url)

# you can merge audio files with video files by using FFMPEG # by downloading audio and video files seperately you get much better quality
# https://www.youtube.com/watch?v=GdfE9WiIQqo
