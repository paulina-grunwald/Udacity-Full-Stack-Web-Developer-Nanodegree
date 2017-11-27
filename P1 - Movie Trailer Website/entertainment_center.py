import os
import sys
import media
import fresh_tomatoes

#create instance of the Spirited Away movie
spirited_away = media.Movie("Spirited Away",
                        "Travel of ten-year old Chihiro and her parents to their new home",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BOGJjNzZmMmUtMjljNC00ZjU5LWJiODQtZmEzZTU0MjBlNzgxL2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UY1200_CR90,0,630,1200_AL_.jpghttps://images-na.ssl-images-amazon.com/images/M/MV5BOGJjNzZmMmUtMjljNC00ZjU5LWJiODQtZmEzZTU0MjBlNzgxL2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                        "https://www.youtube.com/watch?v=ByXuk9QqQkk")

#create instance of the Under the Toscan sun movie
under_the_tuscan_sun = media.Movie("Under the Tuscan Sun",
                     "Story of a writer impulsively buys a villa in Tuscany in order to change her life",
                     "https://upload.wikimedia.org/wikipedia/en/8/8e/Under_the_tuscan_sun_poster.jpg",
                     "https://www.youtube.com/watch?v=vdJGMZDY0-8")

#create instance of the Under the Toscan sun movie
under_the_tuscan_sun = media.Movie("Under the Tuscan Sun",
                     "Story of a writer impulsively buys a villa in Tuscany in order to change her life",
                     "https://upload.wikimedia.org/wikipedia/en/8/8e/Under_the_tuscan_sun_poster.jpg",
                     "https://www.youtube.com/watch?v=vdJGMZDY0-8")

#create instance of Race movie
race = media.Movie("Race",
                     "Athlete Jesse Owens, who won a record-breaking four gold medals at the 1936 Berlin Olympic Games",
                     "https://upload.wikimedia.org/wikipedia/en/0/02/Race_2016_film_poster.jpg",
                     "https://www.youtube.com/watch?v=E31LnSw47xo")
print(race.storyline)
race.show_trailer()