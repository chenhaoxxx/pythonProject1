from movie import Movie
from moviecollection import MovieCollection

WELCOME = "Watching movies"
MENU = "Menu:\nL - List movies\nA - Add new movies\nW - Watch a movie\nQ - Quit"


def input_string(message):
    """Print the  message which from the users."""
    while True:
        string = input(message)
        if string != "":
            break
        else:
            print("Input can not be blank")

    return string


def input_int(message):
    """Print out message."""
    while True:
        num = input(message)
        try:
            num = int(num)
            if num <= 0:
                print("Number must be > 0")
            else:
                return num
        except ValueError:
            print("Invalid input; enter a valid number")


def print_inf(movies):
    """Print the information about the movie's list."""
    print(movies)
    unwatched_num = movies.unwatched_num()
    watched_num = movies.watched_num()
    if unwatched_num != 0:
        print("{} movies watched, {} movies still to watch.".format(watched_num, unwatched_num))
    else:
        print("No more movies to watch!")


def main():
    """Main part of the movie."""
    print(WELCOME)
    data_file = "movies.csv"
    movies = MovieCollection()
    movies.load_movies(data_file)
    print("{0} movies loaded from {1}".format(movies.movies_num(), data_file))
    while True:
        print(MENU)
        movies.sort("is_watched")
        command = input()
        command = command.lower()
        movies_num = movies.movies_num()
        unwatched_num = movies.watched_num()
        # read the movie from the list

        if command == "l":
            print_inf(movies)

            # input l read the list
        elif command == "a":
            title = input_string("Title: ")
            category = input_string("Category: ")
            year = input_int("Year: ")
            # add movie into movies
            movies.add_movies(Movie(title, category, year))
            print("{}  ({} from {}) added to the movie list".format(title, category, year))
            # input a read the "add movies"
        elif command == "m":
            if unwatched_num >= 1:
                print_inf(movies)
                print("Enter the number of a movies to mark as watched")
                while True:
                    sign_num = input_int("")
                    if sign_num > movies_num:
                        print("Invalid number")
                    elif sign_num > unwatched_num:
                        print("That movie is already watched")
                        break
                    else:
                        sign_index = sign_num - 1
                        movie = movies.movies[sign_index]
                        title = movie.title
                        category = movie.category
                        movie.watched()
                        print("{0} in {1} visited!".format(title, category))
                        break
            else:
                print("No more movies to watch!")
                # input m to get the number of wwatched movies and unwatched movies.
        elif command == "q":
            movies.save_movies(data_file)
            print("{0} movies saved to {1}".format(movies_num, data_file))
            print("Thanks for watching")
            break
        else:
            print("Invalid menu choice")


if __name__ == '__main__':
    main()
