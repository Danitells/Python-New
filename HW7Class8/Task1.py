# Create a simple function called favorite_movie, which takes a string
# containing the name of your favorite movie.
# The function should then print “My favorite movie is named {name}”.


# Hope u don't mind, I've modified solution a little.
def get_name_of_movie():
    name = input('Please enter your movie name:')
    return name


movie_name = get_name_of_movie()


def favorite_movie(name):
    print('My favorite movie is named {name}'.format(name=name))


favorite_movie(movie_name)