import webbrowser

# create class movie


class Movie():
    # Create class for representing a movie and it's properties
    def __init__(self, movie_title, movie_storyline,
                 poster_image_url, trailer_youtube_url):
        """
        Arguments in Inits a Movie object:
        title = a string of the movie's title
        movie_storyline = a string that include short description of the movie
        poster_url = a string containing a URL to a poster image
        trailer_url = a string containing a youtube URL of the movie's trailer
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        # Open trailer in a web browser
        webbrowser.open(self.trailer_url)
