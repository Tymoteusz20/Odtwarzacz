import sys 
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout , QPushButton, QLabel
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

from buttons_functions import load_song, play_song,pause_song,next_song,previous_song

class MusicApp(QWidget):
    def __init__(self):
        super().__init__()
        self.songs=[]
        self.calosc()

    def calosc(self):

        self.setWindowTitle("Spotipy")

     
        self.main_layout = QVBoxLayout()

        self.title_label = QLabel("NO SONGS FOUND\nADD A SONG", self)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  
        self.main_layout.addWidget(self.title_label)

     
        self.add_button = QPushButton(self)
        self.add_button.setIcon(QIcon.fromTheme("list-add")) 
        self.add_button.clicked.connect(self.handle_add_button)
        # self.add_button.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.add_button.setFixedSize(100, 100) 
        self.main_layout.addWidget(self.add_button)

        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        

        self.setLayout(self.main_layout)

    def handle_add_button(self):
        new_song = load_song(self)
        self.songs.append(new_song)
        print(self.songs)
        # TODO:Jesli jest to pierwsza piosenka to uruchamiamy songs_list_screens

    def songs_list_screen(self):
        self.main_layout.removeWidget(self.title_label)
        del self.title_label

        self.main_layout.removeWidget(self.add_button)
        del self.add_button

        # dodawanie nowego layoutu 

        control_layout = QHBoxLayout()

        self.play_button = QPushButton("|>",self)
        self.play_button.clicked.connect(play_song)

        self.pause_button = QPushButton("||",self)
        self.pause_button.clicked.connect(pause_song)

        self.next_button = QPushButton("->",self)
        self.next_button.clicked.connect(next_song)

        self.previous_button = QPushButton("<-",self)
        self.previous_button.clicked.connect(previous_song)

        control_layout.addWidget(self.play_button)
        control_layout.addWidget(self.play_button)
        control_layout.addWidget(self.play_button)
        control_layout.addWidget(self.play_button)
        

    def initial_screen(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    music_app = MusicApp()
    music_app.showMaximized()  
    sys.exit(app.exec())
