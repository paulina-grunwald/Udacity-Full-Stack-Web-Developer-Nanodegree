import webbrowser

class Movie():

    ###Class for representing a movie
    def __init__(self, movie_title, movie_storyline, poster_image_url, trailer_youtube_url):
        """ Inits a Movie object
        Args:
        title = a string of the movie's title
        year = an integer for the year of the movie's release
        poster_url = a string containing a URL to a poster image
        trailer_url = a string containing a youtube URL of the movie's trailer
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url


    def show_trailer(self):
        ###Opens trailer in a web browser
        webbrowser.open(self.trailer_url)