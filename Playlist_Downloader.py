import os
from time import sleep
from tkinter import filedialog
from pytube import *     #pip install pytube

def playlist_download(itag, link): 
    pl = Playlist(link)
        
    counter = 0
    for idx,video in enumerate(pl.videos):
        counter += 1  
        
    print(f"\nTotal videos found {counter}.\n")
    for idx,video in enumerate(pl.videos):
        print(f"Downloading videos {idx+1}/{counter}")
        video.streams.get_by_itag(itag).download()
            
    sleep(1)
    print("\n<<<Download Finished>>>\n")
    
    
def directory():
    path = filedialog.askdirectory()
    os.chdir(path)
    print(f"Directory: {path}\n")
    
    
def main():
    link = str(input("Link: "))
    print("Resolutions available in 360p and 720p\n")
    resolution = str(input("Resolution: "))
    """
        itag list
        360p = 18
        720p = 22
    """
    if "360" in resolution:
        playlist_download(18, link)
    elif "720" in resolution:
        playlist_download(22, link)
    else:
        main()

try:
    print("\n<===YOUTUBE PLAYLIST DOWNLOADER===>\n\n")
    print("Select Directory for Downloads-->\n")
    sleep(2)
    directory()

    main()
except Exception as e:
    print("\n\nSomething Went Wrong___:(\n")