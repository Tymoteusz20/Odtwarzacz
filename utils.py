import os 
from song import Song

def init_songs():
    songs = []
    for song_title in os.listdir("music/"):
        song_title = song_title.split(".")[0]
        songs.append(Song(song_title,'','','',)) 

    return songs

