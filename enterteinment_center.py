import media
import fresh_tomatoes


import media
import fresh_tomatoes

# object toy story with supporting attribute
toy_story = media.Movie("Toy Story", "Toy come to life", "http://" +
                        "upload.wikimedia.org/wikipedia/en/1/13" +
                        "/Toy_Story.jpg", +
                        "http://www.youtube.com/watch?v=vwyZH85NQC4")

# object avatar with supporting attribute
avatar = media.Movie("Avatar", "A marine that live in alien" +
                     "planet", "http://upload.wikimedia." +
                     "org/wikipedia/id/b/b0/Avatar-Teaser-Poster." +
                     "jpg", "http://www.youtube.com/watch?v=-9ceBgWV8io")

# object scholl of rock with supporting attribute
scholl_of_rock = media.Movie("School of Rock", "A rock band " +
                             "become a teacher", "https://" +
                             "upload.wikimedia.org/wikipedia" +
                             "/en/1/11/School_of_Rock_Poster.jp" +
                             "g", "http://www.youtube.com/watch?" +
                             "hl=id&gl=ID&v=XCwy6lW5Ixc")


# insert movie into array
movies = [toy_story, avatar, scholl_of_rock]
# execute the method
fresh_tomatoes.open_movies_page(movies)
