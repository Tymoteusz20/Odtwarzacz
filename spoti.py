import sys , pygame
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout , QPushButton, QLabel
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

from buttons_functions import load_song, play_song,pause_song,next_song,previous_song

from utils import *

class MusicApp(QWidget):
    def __init__(self):
        super().__init__()
        pygame.mixer.init()
        self.songs = init_songs()
        if self.songs:
            self.current_song = self.songs[0]
        else:
            self.current_song = None
        self.current_song_paused = False
        self.calosc()

    def calosc(self):

        self.setWindowTitle("Spotipy")
        self.main_layout = QVBoxLayout()
        if self.songs:
            self.songs_list_screen()
        else:
            self.initial_screen()

        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        

        self.setLayout(self.main_layout)

    def handle_add_button(self):
        new_song = load_song(self)
        self.songs.append(new_song)

        if len(self.songs) == 1:
            if self.current_song is None:
                self.current_song = new_song
                pygame.mixer.music.load(self.current_song.path)
            self.clear()
            self.songs_list_screen()

    def handle_previous_button(self):
        pass

    def handle_play_button(self):
        if not self.current_song_paused:
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.unpause()
        self.play_button.setText('||')
        self.play_button.clicked.disconnect(self.handle_play_button)
        self.play_button.clicked.connect(self.handle_pause_button)
        
    
    def handle_pause_button(self):
        pygame.mixer.music.pause()
        self.current_song_paused = True
        self.play_button.setText('|>')
        self.play_button.clicked.disconnect(self.handle_pause_button)
        self.play_button.clicked.connect(self.handle_play_button)

    def handle_next_button(self):
        pass

    def songs_list_screen(self):
       

        # dodawanie nowego layoutu 

        control_layout = QHBoxLayout()

        self.play_button = QPushButton("|>",self)
        self.play_button.clicked.connect(self.handle_play_button)

        # self.pause_button = QPushButton("||",self)
        # self.pause_button.clicked.connect(pause_song)

        self.next_button = QPushButton("->",self)
        self.next_button.clicked.connect(next_song)

        self.previous_button = QPushButton("<-",self)
        self.previous_button.clicked.connect(previous_song)

        
        
        control_layout.addWidget(self.previous_button)
        control_layout.addWidget(self.play_button)
        control_layout.addWidget(self.next_button)


        self.main_layout.addLayout(control_layout)
        
    

    def initial_screen(self):
        self.title_label = QLabel("NO SONGS FOUND\nADD A SONG", self)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  
        self.main_layout.addWidget(self.title_label)

     
        self.add_button = QPushButton(self)
        self.add_button.setIcon(QIcon.fromTheme("list-add")) 
        self.add_button.clicked.connect(self.handle_add_button)
        # self.add_button.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.add_button.setFixedSize(100, 100) 
        self.main_layout.addWidget(self.add_button)


    def clear(self):
        self.main_layout.removeWidget(self.title_label)
        del self.title_label

        self.main_layout.removeWidget(self.add_button)
        del self.add_button


if __name__ == '__main__':
    app = QApplication(sys.argv)
    music_app = MusicApp()
    music_app.showMaximized()  
    sys.exit(app.exec())
