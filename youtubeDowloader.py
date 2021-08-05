# A YOUTUBE VIDEO DOWNLOADER
# BY AMINU AHMADH 
# GITHUB @AminuAhmadh


from pytube import YouTube
import pyinputplus, time, os
from pytube.cli import on_progress
from pytube.request import filesize


# path to save the file
def file_path():
    home = os.path.expanduser('~')
    download_path = os.path.join(home, 'videos')
    return download_path


print('A Youtube downloader')
link = input('Enter the Youtube video Link: \n')
print('Got the link!')
print('Getting Video Info...')

try:
    yt = YouTube(link, on_progress_callback=on_progress)
    highest_resolution = yt.streams.get_highest_resolution()
except Exception as error:
    print('Opps! an ERROR Occured. try: \n — Checking your connection \n — Url is a valid YouTube watch url \n — Or try again later ')
    print("Your error occured due to:", error)
    exit()

# Get the file size
def size():
    if prompt == 'yes':
        if highest_resolution.filesize < 1000000000:
            megabyte = highest_resolution.filesize / 1000000
            print('SIZE: ',round(megabyte),'MB' ) 
        elif highest_resolution.filesize >= 1000000000:
            gigabyte = highest_resolution.filesize / 1000000000
            print('SIZE: ',round(gigabyte),'GB' ) 

# prints out details of the video
print('TITLE:', yt.title)
print('YOUTUBER/CHANNEL:', yt.author)
print('LENGTH:', yt.length, 'seconds')
print('RATING:', str(yt.rating))
desc = pyinputplus.inputYesNo(prompt='Do you want to see the video description? ')
if desc == 'yes':
    print('The video description is:', yt.description)
else:
    pass
prompt = pyinputplus.inputYesNo(prompt='Download the video with 720p resolution? ')
if prompt == 'no':
    print('Sorry, that is the only resolution available for download right now')
    quit()
else:
    print('Getting Video...')
    print('Getting Resolution...')
    quality = highest_resolution
    file_size = quality.filesize
    print('RESOLUTION: 720p')
    size()
    print('Downloading Your File...')
    print()
    try:
        quality.download(file_path())
    except Exception as Downloaderror:
        print("Error occured due to:", Downloaderror)
        exit()

print("Downloaded Successfully!")

