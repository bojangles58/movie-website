import fresh_tomatoes   # imports the html file fresh_tomatoes.py
import media    # imports the file I saved as media.py

# Details of 9 movies below that I like.
# I have also included a name place for movie_director.

black_panther = media.Movie("Black Panther",
                        "Centuries ago, five African tribes war over a "
                        "vibranium meteorite.One warrior ingests a herb "
                        "in the shape of a heart, he is affected by the "
                        "metal and gains superhuman powers, becoming the "
                        "first 'Black Panther'.",
                        "Ryan Coogler",
                        "https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg",  # noqa
                        "https://www.youtube.com/watch?v=xjDjIWPwcPU")
# print(black_panther.storyline)
# black_panther.show_trailer()

robocop = media.Movie("Robocop",
                     "The company see a way forward to regaining the trust "
                     "of the public when a cop, Alex Murphy is killed by "
                     "violent robbers. Murphy's body is rebuilt within a "
                     "steel frame enclosure. His memory is wiped and he is "
                     "re-named Robocop.",
                     "Paul Verhoeven",
                     "https://upload.wikimedia.org/wikipedia/en/1/16/RoboCop_%281987%29_theatrical_poster.jpg",  # noqa
                     "https://www.youtube.com/watch?v=zbCbwP6ibR4")
# print(robocop.storyline)
# robocop.show_trailer()

twelve_angry_men = media.Movie("Twelve Angry Men",
                        "A drama written by Reginald Rose concerning the jury "
                        "of a homicide trial. The men are at loggerheads with "
                        "one another and have there own personal reasons for "
                        "wanting to convict the young man or not for killing "
                        "his own father",
                        "Sidney Lumet",
                        "https://upload.wikimedia.org/wikipedia/en/9/91/12_angry_men.jpg",  # noqa
                        "https://www.youtube.com/watch?v=A7CBKT0PWFA")
# print(twelve_angry_men.storyline)
# twelve_angry_men.show_trailer()

taken = media.Movie("Taken",
                        "A former spy (Liam Neeson) has acquired 'a very "
                        "'particular set of skills' which he uses to rescue "
                        "his kidnapped daughter, (Maggie Grace), who is "
                        "separated from her friend. and is sold to the "
                        "highest bidder.",
                        "Olivia Magaton, Pierre Morel",
                        "https://upload.wikimedia.org/wikipedia/en/e/ed/Taken_film_poster.jpg",  # noqa
                        "https://www.youtube.com/watch?v=uPJVJBm9TPA")
# print(taken.storyline)
# taken.show_trailer()

predator = media.Movie("Predator",
                        "A team of commandos on a mission in a Central Amer- "
                        "ican jungle are 'hunted for sport' by an extraterres-"
                        "trial warrior.  They are killed off one by one in a "
                        "desperate attempt to out-smart the strange being "
                        "from hell.",
                        "John McTieman",
                        "https://upload.wikimedia.org/wikipedia/en/2/23/Predator_--_soundtrack_album_cover.jpg",  # noqa
                        "https://www.youtube.com/watch?v=X2hBYGwKh3I")
# print(predator.storyline)
# predator.show_trailer()

assault_on_precinct_13 = media.Movie("Assault On Precinct 13",
                        "A 1976 action thriller film stars Austin Stoker as a "
                        "police officer who defends a defunct precinct "
                        "against an attack by a relentless criminal gang, "
                        "along with Darwin Joston as a convicted murderer and "
                        "a brave secretary, Laurie Zimmer.",
                        # Source: https://en.wikipedia.org/wiki/Assault_on_"
                        # Precinct_13_(1976_film)
                        "John Carpenter",
                        "https://upload.wikimedia.org/wikipedia/en/9/9d/Assault_on_precinct_thirteen_movie_poster.jpg",  # noqa
                        "https://www.youtube.com/watch?v=7wnAjYDVObs")
# print(assault_on_precinct_13.storyline)
# assault_on_precinct_13.show_trailer()

legend = media.Movie("Legend",
                        "The hero Jack (Tom Cruise), has a mission to "
                        "vanquish Darkness and allow the sun to prevail. Lili "
                        "(Mia Sara), is the young woman he encounters and "
                        "falls in love with, but she is lured into the under-"
                        "world and seduced by an exotic priestess into "
                        "seemingly becoming evil.",
                        # Source:#https://www.rogerebert.com/reviews/legend-
                        # 1986.
                        "Ridley Scott",
                        "https://upload.wikimedia.org/wikipedia/en/9/98/Legendposter.jpg",  # noqa
                        "https://www.youtube.com/watch?v=SjMnXHzw534")
# print(legend.storyline)
# legend.show_trailer()

dispicable_me_3 = media.Movie("Dispicable Me 3",
                        "In the film, Gru teams up with his long-lost twin "
                        "brother Dru in order to defeat a new enemy named "
                        "Balthazar Bratt, a former child actor, obsessed with "
                        "the 1980s, who grows up to become a villain after "
                        "having his show cancelled following puberty.",
                        # Source: https://en.wikipedia.org/wiki/Despicable_Me_3
                        "Pierre Coffin, Kyle Balda",
                        "https://upload.wikimedia.org/wikipedia/en/9/91/Despicable_Me_3_%282017%29_Teaser_Poster.jpg",  # noqa
                        "https://www.youtube.com/watch?v=6DBi41reeF0")
# print(dispicale_me_3.storyline)
# dispicable_me_3.show_trailer()

the_terminator = media.Movie("The Terminator",
                        "Schwarzenegger stars as the Terminator, a cyborg "
                        "assassin sent back in time from 2029 to 1984 to "
                        "kill Sarah Connor (Linda Hamilton), whose son will "
                        "one day become a saviour against machines in a "
                        "post-apocalyptic future.  Kyle Reese (Michael Biehn) "
                        "is her protector.",
                        # Source: https://en.wikipedia.org/wiki/The_Terminator
                        "James Cameron",
                        "https://upload.wikimedia.org/wikipedia/en/7/70/Terminator1984movieposter.jpg",  # noqa
                        "https://www.youtube.com/watch?v=c4Jo8QoOTQ4")
# print(the_terminator.storyline)
# the_terminator.show_trailer()

movies = [black_panther, robocop, twelve_angry_men, taken, predator,
          assault_on_precinct_13, legend, dispicable_me_3, the_terminator]

fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.VALID_RATINGS)
# print(media.Movie.__doc__) # ensure 2 underscores on either side of "doc"
