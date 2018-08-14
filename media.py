import webbrowser #  Imports the Python web browser.

class Movie(): #  Movie is the class
    """ This class provides a way to store movie related information"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]  # Valid movie ratings.
    def __init__(self, movie_title, movie_storyline, movie_director,
                poster_image, trailer_youtube):
                #  init means to initialize, "self", refers to film as
                #  instance from the entertainment_center.py file.
                #  Inputs: title of movie, storyline of movie, director's
                #  name, url of poster image, url of youtube trailer.

        self.title = movie_title
        self.storyline = movie_storyline
        self.director = movie_director #  I have added an extra instance here.
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        """ Attributes to the class "Movie" is in the object "self" that
        follows the "dot." The error shown below is due to the fact that
        there should be a space after "def" before underscore. Everything in
        parentheses should show in "orange", "def" should be purple, "init"
        should be green to run "entertainment_center file successfully."
        I have since corrected this."""

class Parent():
    """ This class provides a way to create a Parent class whose can be
    inherited by a Child class along with attributes of its own, e.g. movies
    with a director's name, or the movies title."""

    def __init__(self, movie_title, movie_director):
        """ initializes attributes for Parent class"""

        print("Parent Constructor Called")  # prints this out.
        self.movie_title = movie_title
        self.director = movie_director

    def show_info(self):
        #  show and print Parent class attributes.
        print("Movie Title - "+self.movie_title)
        print("Movie Director - "+self.director)

class Child(Parent):
    """ The Child class inherits two attributes from the Parent class and has
        its own attribute added, (film_release_date)"""

    def __init__(self, movie_title, movie_director, film_release_date):
        """ initializes two inherited Parent class attributes for Child class
        as well as its own attribute, (film_release_date)"""

        print("Child Constructor Called")  #  prints this out.
        Parent.__init__(self, movie_title, movie_director)
        self.film_release_date = film_release_date

    def show_info(self):
        #  show and print Child class attributes.
        print("Movie Title - "+self.movie_title)
        print("Movie Director - "+self.director)
        print("Film Release Date - "+self.film_release_date)

film_specifics = Parent("Robocop", "Paul Verhoeven")
#  Instance of Parent class.

#  film_specifics.show_info()
#  print(film_specifics.movie_title)

individual_film_specifics = Child("Robocop", "Paul Verhoeven",
                                    "February 5 1988")
#  Instance of Child class, inherits first two attributes from Parent class.
#  plus has its own attribute, "film release date."

individual_film_specifics.show_info()
#  print(individual_film_specifics.movie_title)
#  print(individual_film_specifics.film_release_date)

def show_trailer(self):
    webbrowser.open(self.trailer_youtube_url)
    """ This function allows you to open a web browser with the link to the
    youtube movie trailer.
    Argument: is the movie (self).  It seems as "self" is not a keyword in
    Python, any word could be used in place of "self."
    Output: opens a web browser to open movie trailer on youtube."""
