"""

Stage 3, Final Project
Frank Costello
IPND

My task is to write a movie class in media.py and define
properties of a movie are that need to be encapsulated 
in a movie object.  Additionally, write a constructor 
to instantiate movie objects.



"""

import webbrowser      #Leverage existing code to interface with web browser

class Movie():
    #This class provides a way to store movie and display related information

    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

