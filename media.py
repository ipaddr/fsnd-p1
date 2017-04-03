import webbrowser

class Movie():
    def __init__(self, movieTitle, movieStoryline, moviePoster, movieTrialUrl):
        self.title = movieTitle
        self.storyline = movieStoryline
        self.poster_image_url = moviePoster
        self.trailer_youtube_url = movieTrialUrl

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
