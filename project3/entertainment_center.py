"""

Stage 3, Final Project
Frank Costello
IPND

My task is to instantiate movie objects and display them as
a grid in a web browser.  The file fresh_tomatoes.html will created and opened.

"""


import media
import fresh_tomatoes

godfather = media.Movie("The GodFather",
                        "A light hearted frolic into the lives of a hilarious Italian family",
                        "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
                        "https://www.youtube.com/watch?v=sY1S34973zA")

						
taxi_driver = media.Movie("Taxi Driver",
                        "A slow paced account of a hard working taxi driver and his uneventful life as he slips into obscurity and peaceful retirement.",
                        "https://upload.wikimedia.org/wikipedia/en/8/8f/Taxi_Driver_original_movie_poster.jpg",
                        "https://www.youtube.com/watch?v=sLpMx8_TYOo")
                        



space_odyssey = media.Movie("2001:A Space Odyssey",
                        "Many hours are spent watching a human bone transform into a space sattelite.",
                        "http://bit.ly/2gdd2aF",
                        "https://www.youtube.com/watch?v=lfF0vxKZRhc")						

						
						
						
movies = [godfather, taxi_driver,space_odyssey]
fresh_tomatoes.open_movies_page(movies)

