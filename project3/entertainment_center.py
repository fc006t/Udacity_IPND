import fresh_tomatoes
import media


toy_story = media.Movie("Toy Story",
                        "A story of a boy and haunted toys",
                        "https://en.wikipedia.org/wiki/File:Toy_Story.jpg",
                        "https://m.youtube.com/watch?v=vPHRTK02rL0")

avatar = media.Movie("Avatar",
                        "A marine on an alien planet",
                        "https://en.wikipedia.org/wiki/File:Toy_Story.jpg",
                        "https://m.youtube.com/watch?v=vPHRTK02rL0")
                        
                        

PNID = media.Movie("PNID",
                        "A great class online",
                        "https://en.wikipedia.org/wiki/File:Toy_Story.jpg",
                        "https://youtu.be/e4AFN3rYkR0")
                        
school_of_rock = media.Movie("PNID",
                        "A great class online",
                        "https://en.wikipedia.org/wiki/File:Toy_Story.jpg",
                        "https://youtu.be/e4AFN3rYkR0")
                        
                        
#print(toy_story.storyline)
#print(avatar.storyline)
#avatar.show_trailer()
#PNID.show_trailer()

movies = [toy_story, avatar,PNID,school_of_rock]
print movies
fresh_tomatoes.open_movies_page(movies)

