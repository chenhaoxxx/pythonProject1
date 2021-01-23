from movie import Movie
from operator import attrgetter
import csv


# TODO: Create your MovieCollection class in this file


class MovieCollection:
    def __init__(self):
        """The constructor by moviecollection."""
        self.movies = []

    def __str__(self):
        """String representation"""
        max_title = 0
        max_category = 0
        for movie in self.movies:
            if len(movie.title) > max_title:
                max_title = len(movie.title)
            if len(movie.category) > max_category:
                max_category = len(movie.category)
        if self.unwatched_num() == 0:
            max_num = self.watched_num() // 10 + 1
        else:
            max_num = self.watched_num() // 10 + 2
        printout = ""
        for i, movie in enumerate(self.movies):
            num_str = str(i + 1)
            title = movie.title
            category = movie.category
            year = movie.year
            if movie.is_watched:
                printout += "{0:>{4}s}. {1:<{5}s}  {2:<{6}s}  {3:3d}".format(num_str, title, category, year,
                                                                             max_num, max_title, max_category)
            else:
                num_str = "*" + num_str
                printout += "{0:>{4}s}. {1:<{5}s}  {2:<{6}s}  {3:3d}".format(num_str, title, category, year,
                                                                             max_num, max_title, max_category)
            if i != self.movies_num() - 1:
                printout += "\n"

        return printout

    def __repr__(self):
        """String representation"""
        return self.__str__

    def load_movies(self, filePath):
        """Load  the file."""
        with open(filePath, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                row[1] = int(row[1])
                if row[3] == "w":
                    row[3] = True
                else:
                    row[3] = False
                self.movies.append(Movie(*row))

    def movies_num(self):
        """Movies' number in the list."""
        return len(self.movies)

    def watched_num(self):
        """The number of movies which had watched."""
        num = 0
        for movie in self.movies:
            if movie.is_watched:
                num += 1
        return num

    def unwatched_num(self):
        """The number of movies which had not movies"""
        num1 = 0
        for movie in self.movies:
            if not movie.is_watched:
                num1 += 1

        return num1

    def add_movies(self, movie):
        """Add movie to the list."""
        self.movies.append(movie)

    def save_movies(self, filePath):
        """Save movie to the list of file csv."""
        with open(filePath, 'w', newline="") as file:
            writer = csv.writer(file)
            for movie in self.movies:
                if movie.is_watched:
                    pass
                else:
                    pass
                writer.writerow([movie.title, movie.year, movie.category, movie.watched])

    def sort(self, sort_key):
        """Sort by the key."""
        self.movies.sort(key=attrgetter(sort_key, "year"))
