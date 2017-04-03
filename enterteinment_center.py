import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story"
                        , "Toy come to life"
                        , "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg"
                        , "http://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar"
                     , "A marine that live in alien planet"
                     , "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg"
                     , "http://www.youtube.com/watch?v=-9ceBgWV8io")

scholl_of_rock = media.Movie("School of Rock"
                     , "A rock band become a teacher"
                     , "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg"
                     , "http://www.youtube.com/watch?hl=id&gl=ID&v=XCwy6lW5Ixc")

movies = [toy_story, avatar, scholl_of_rock]
fresh_tomatoes.open_movies_page(movies)
