#autor i czas trwania rodzaj (info)
class Song:
    def __init__(self,title,author,duration,genre) -> None:
        self.title = title
        self.author = author
        self.duration = duration
        self.genre = genre
        self.path = f"music/{title}.mp3"

    def __del__(self):
        # usun piosenke pod sciezka self.path
        pass

