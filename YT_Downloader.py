import os, shutil
from time import sleep
from pytube import YouTube # pip install pytube
from pytube import Playlist

download_dir = "F:\\Downloads\\"    # use your directory

def video_download(link):
    os.chdir(download_dir)   # change video directory
    
    videos = YouTube(link).streams.filter(progressive=True)     # filtering videos which have audio & video
    video_list = list(enumerate(videos))    # wrapping the video list into an another list 
    
    for i in video_list:
        print(i)    # printing the available video list
    print()
    
    term = int(input("Enter level: "))   # select list number from wrapped list (0 to )
    select_stream_tuple = video_list[term]   # select stream from wrapped list
    select_stream_tuple[1].download()    # download selected stream
    
    sleep(1)
    print("\n>>>Downloaded<<<")


def audio_download(link):
    os.chdir(download_dir)
    
    video_title = YouTube(link).title   # video title
    audios = YouTube(link).streams.filter(only_audio=True)
    audio_list = list(enumerate(audios))
    
    for i in audio_list:
        print(i)
    print()
    
    term = int(input("Enter level: "))
    select_stream_tuple = audio_list[term]
    mp3_file = select_stream_tuple[1].download()
    mp3_name = video_title+".mp3"
    os.rename(mp3_file, mp3_name)
    
    sleep(1)
    print("\n>>>Downloaded<<<")


def playlist_download(link):
    yt_playlist = Playlist(link)
    pl_title = yt_playlist.title    # playlist title
    
    os.chdir(download_dir)   # change directory from default to user preference
    os.makedirs(pl_title)   # create a new folder
    store_loc = download_dir+pl_title    # video store location
    
    print("Downloading Playlist......")
    for video in yt_playlist.videos:
        pl_video = video.streams.get_by_resolution(resolution="720p").download()    # download videos in 720p
        shutil.move(pl_video, store_loc)    # move videos into the store location
        
    sleep(1)
    print("\n>>>Downloaded<<<")
    
    
def main():
    try:
        print("\n***  For video type \"v\", for audio type \"a\", for playlist type \"p\"  ***\n")
        type = str(input("Enter type: "))
        
        yt_link = str(input("\nEnter link: "))
        
        if "v" in type:
            video_download(yt_link)
        elif "a" in type:
            audio_download(yt_link)
        elif "p" in type:
            playlist_download(yt_link)
        else:
            main()
    except Exception as e:
        main()
        

main()    
