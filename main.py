from pytube import YouTube

url='https://www.youtube.com/watch?v=7BXJIjfJCsA'
video = YouTube(url)

print("***************Video Title*****************")
print(video.title)
print("****************thumbnail_url**************")
print(video.thumbnail_url)

print("***************Download_Video****************")

video = video.streams.get_highest_resolution()

#for stream in my_video.streams:
 #   print(stream)
video.download()