#use classes to build movie website. The website will include trailer of the movie
#class movie will include: movie title, sotryline, poster and link to youtube trailer
#add show trailer option

import webbrowser
#Google style guide for Python suggest that name of clost
#would have first letter Capital

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)