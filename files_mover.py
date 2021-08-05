# import the required modules
import shutil
import os
from zipfile import ZipFile


# point to the Downloads Folder/path
downloads_path = os.path.expanduser('~\\Downloads')
os.chdir(downloads_path)


# path to move the files // You can modify to save in your desired path
videos_dst = os.path.expanduser('~\\Videos')
pictures_dst = os.path.expanduser('~\\Pictures')
docs_dst = os.path.expanduser('~\\Documents')
music_dst = os.path.expanduser('~\\Music')


for root, dirs, files in os.walk(downloads_path, topdown=False):
    files = [f.lower() for f in files if not f[0] == '.']
    for file in files:
        # if it's a video
        if file.endswith(('mp4', 'avi', 'mov', 'wmv', 'flv', 'mkv')):
            # move to desired destination
            shutil.move(file, videos_dst)
        # if it is a picture
        elif file.endswith(('png', 'jpeg')):
            # move it
            shutil.move(file, pictures_dst)
        # else if they're docs
        elif file.endswith(('doc', 'docx', 'txt', 'ppt','pptx', 'epub', 'pdf', 'xls', 'xlsx')):
            # move
            shutil.move(file, docs_dst)
        elif file.endswith(('mp3', 'wav')):
            # move it
            shutil.move(file, music_dst)
        else:
            pass
print('Done Moving.')