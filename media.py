import webbrowser


# Class movie is reflect the blue print of movie
# that we want to display in web browser
class Movie():
    # Init the class first time by passing title, storyline, poster and triler url
    def __init__(self, movieTitle, movieStoryline, moviePoster, movieTrialUrl):
        self.title = movieTitle
        self.storyline = movieStoryline
        self.poster_image_url = moviePoster
        self.trailer_youtube_url = movieTrialUrl

    # show the trailer by opening browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
