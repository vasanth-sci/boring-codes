import yt_dlp

# Specify the URL of the video you want to download
video_url = 'https://www.youtube.com/watch?v=3DRdl7i56Xs'

# Define the options for the download (such as format, output directory, etc.)
ydl_opts = {
    'format': 'best',  # Download the best quality available
    'outtmpl': 'D:/neeti mullai.mp4',  # Save the file with the video title as its name
}

# Use yt-dlp to download the video
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

print("Video downloaded successfully!")

