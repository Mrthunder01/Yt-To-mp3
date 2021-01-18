# Coded By Mr Thunder
# Thank to my all community

# Install package (pip install youtube_dl)

# Import Module
from __future__ import unicode_literals
import youtube_dl
import os

class Download(object):
    def __init__(self, url):
        self.url = url
        self.save_path = os.path.join(os.path.expanduser('~'), str(pathj))
        self.song()

    def song(self):
        opts = {
            'verbose': True,
            'fixup': 'detect_or_warn',
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '1411'
            }],

            'extraction': True,
            'outtmpl': self.save_path + '/%(title)s.%(ext)s',
            'noplaylist': 'True'
        }
        ydl = youtube_dl.YoutubeDL(opts)
        ydl.download([self.url])

if __name__ == '__main__':
    print("#------------------------------------------------------------------------#")
    print("[/] YT-TO-MP3 By : MR THUNDER")
    print("[/] Github : https://github.com/MR Thunder - https://github.com/IT-World-ID")
    print("[/] IT-World - 3XPLOID.ID - AnonymouS Indonesia")
    print("#------------------------------------------------------------------------#\n")
    url = input("Enter Youtube URL : ")
    pathj = input("Enter Path To Save (EX - C:\\Users\\Administrator\\Desktop) : ")
    Download(url)
    os.system("cls || clear")
    print("Successfully Convert To mp3")
    input('Enter any key to close...')