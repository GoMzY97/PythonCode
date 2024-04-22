import yt_dlp

#ENter the url for download

url = input("Enter Video URL:  ")

ydl_opts = {}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
	ydl.download([url])

print("Video downloaded successfully!")
