# import the required modules
import shutil
import os
from zipfile import ZipFile


# point to the Downloads Folder
downloads_path = os.path.expanduser('~\\Downloads')
os.chdir(downloads_path)


# path to move the files // You can modify to save in your desired path
videos_dst = os.path.expanduser('~\\Videos')
pictures_dst = os.path.expanduser('~\\Pictures')
docs_dst = os.path.expanduser('~\\Documents')
music_dst = os.path.expanduser('~\\Music')


for root, dirs, files in os.walk(downloads_path, topdown=False):
    for file in files:
        try:
            # if it's a video
            if file.lower().endswith(('mp4', 'avi', 'mov', 'wmv', 'flv', 'mkv')):
                # move to desired destination
                shutil.move(file, videos_dst)
                print('moved a video')
            # if it is a picture
            elif file.lower().endswith(('png', 'jpeg')):
                # move it
                shutil.move(file, pictures_dst)
                print('moved a picture')
            # else if they're docs
            elif file.lower().endswith(('doc', 'docx', 'txt', 'ppt','pptx', 'epub', 'pdf', 'xls', 'xlsx')):
                # move
                shutil.move(file, docs_dst)
                print('moved a document')
            elif file.lower().endswith(('mp3', 'wav')):
                # move it
                shutil.move(file, music_dst)
                print('moved an audio')
            else:
                pass
        except Exception as e:
            print (e)
print('Done Moving.')
