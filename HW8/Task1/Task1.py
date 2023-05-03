from HW8.Task1.Module1 import get_name_of_movie


movie_name = get_name_of_movie()


def favorite_movie(name):
    print('My favorite movie is named {name}'.format(name=name))


favorite_movie(movie_name)