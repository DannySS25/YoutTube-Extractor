import yt_dlp
import os

path = os.path.join(os.path.expanduser("~"), "Downloads")

def run_downloader():
    url = input("Paste YouTube URL: ")
    choice = input("Select: (1) MP4 Video or (2) MP3 Audio: ")

    ydl_opts = {
        'outtmpl': f'{path}/%(title)s.%(ext)s',
        'quiet': False,
        'noplaylist': True,
    }

    if choice == '1':
        # Best MP4 format
        ydl_opts['format'] = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
    else:
        # MP3 extraction
        ydl_opts['format'] = 'bestaudio/best'
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"\n--- Success! File is in your Downloads folder ---")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":

    run_downloader()
