import webbrowser

class Movie():

    ###Class for representing a movie
    def __init__(self, title, storyline, poster_url, trailer_url, year):
        """ Inits a Movie object
        Args:
        title = a string of the movie's title
        year = an integer for the year of the movie's release
        poster_url = a string containing a URL to a poster image
        trailer_url = a string containing a youtube URL of the movie's trailer
        """
        self.title = title
        self.poster_url = storyline
        self.poster_url = poster_url
        self.trailer_url = trailer_url
        self.year = year

    def show_trailer():
        """ Opens trailer in a web browser """
        webbrowser.open(self.trailer_url)