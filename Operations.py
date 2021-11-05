import os
import requests
from pytube import YouTube
import shutil
from zipfile import ZipFile
import zipfile
class File:
    def Testfile(FileName,FileType,Location):
        print("file name :"+ FileName)
        print("file type: " + FileType)
        print('file location: '+ Location)

    def UnzipFile(ZipName,FolderName,FolderNameExit):
        with zipfile.ZipFile(FolderName+'/'+ZipName+".zip","r") as zip_ref:
            zip_ref.extractall(FolderNameExit)
                 
    def DownloadAddList(FileName,FolderName,link,Items):
        directory = './'+FolderName+''

        filename = FileName

        file_path = os.path.join(directory, filename)
        if not os.path.isdir(directory):
            os.mkdir(directory)
        url = link
        r = requests.get(url)
        
        open(file_path, 'wb').write(r.content)
        
        
        
        
        print(file_path)

        file = open(file_path, "a")
        file.writelines(Items)
        file.close()
        
    def Download(FileName,FolderName,link):
        directory = './'+FolderName+''

        filename = FileName

        file_path = os.path.join(directory, filename)
        if not os.path.isdir(directory):
            os.mkdir(directory)
        url = link
        r = requests.get(url)
        
        open(file_path, 'wb').write(r.content)
    def DownloadE(FileName,link,FolderName):
        directory = './'+FolderName

        filename = FileName

        file_path = os.path.join(directory, filename)
        if not os.path.isdir(directory):
            os.mkdir(directory)
        url = link
        r = requests.get(url)
        
        open(file_path, 'wb').write(r.content)
    def Create(FileName,FolderName,Items):
        directory = './'+FolderName+''

        filename = FileName
        file_path = os.path.join(directory, filename)
        
        if not os.path.isdir(directory):
            os.mkdir(directory)
        file = open(file_path, "a")
        
        for items in Items:

            file.writelines([items])
            
        file.close()
        print(file_path)

class Youtube:

    def GetVideo(YoutubeLink):
        
        youtube_video_url = YoutubeLink
        
        try:
            yt_obj = YouTube(youtube_video_url)
        
            filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
        
            # download the highest quality video
            filters.get_highest_resolution().download()
            print('Video Downloaded Successfully')
        except Exception as e:
            print(e)
            
            