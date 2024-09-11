from PyQt6.QtWidgets import QFileDialog
from song import Song
import os , shutil

def load_song(self):
    # kopiowanie piosenki ze sciezki path do folderu music
    filepath,_=QFileDialog.getOpenFileName(self,"Open File","","All Files (*)")
    title = os.path.splitext(os.path.basename(filepath))[0]
    shutil.copy(filepath,f'music/{title}.mp3')
    #TODO:jezeli taka piosenka juz sie tam znajduje 
    # to  pytamy uzytkownika czy na pewno chce ja zastapic 
    return Song(title,"","","")

def delete_song(song):
    # usuwanie piosenki z music 
    pass

def previous_song(songs,index):
    # uruchom piosenke poprzedniom
    pass

def next_song(songs,index):
    # uruchom kolejna piosenke 
    pass

def pause_song(song):
    # zatrzymanie piosenki
    pass

def play_song(song):
    # uruchomienie piosenki
    pass