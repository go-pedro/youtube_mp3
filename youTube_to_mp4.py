from pytube import YouTube

url='https://youtu.be/u_MgpbuJG8Q'
YouTube(url).streams.get_highest_resolution().download()
yt = YouTube(url)

print(yt.title)

# YouTube('https://youtu.be/9bZkp7q19f0').streams.get_highest_resolution().download()