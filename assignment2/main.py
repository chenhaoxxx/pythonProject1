"""
Name:HaoxianChen
Date:19.1.2020
Brief Project Description:
https://github.com/chenhaoxxx/pythonProject1/tree/master/assignment2
"""
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.button import Button
from movie import Movie
from moviecollection import MovieCollection

WELCOME = "Watching movies"
DICTIONARY = dict({"Watched": "is_watched", "Title": "title", "Year": "year", "Category": "category"})
DATA = "movies.csv"
button_color = [0.5, 0.5, 1, 1]


class MoviesToWatchApp(App):
    """GUI version of Movie to watch App."""

    def __init__(self, **kwargs):
        """creat the main of the app."""
        super().__init__(**kwargs)
        self.text_attr = DICTIONARY
        self.sort_methods = list(self.text_attr.keys())
        self.sort_current = self.sort_methods[0]
        self.movies = MovieCollection()
        self.movies.load_movies(DATA)
        self.information = WELCOME
        Window.size = (1000, 750)

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Movies to watch"
        self.source = Builder.load_file("app.kv")
        self.button_creat()

        return self.source

    def rank(self, text):
        """sort movies"""
        attr = self.text_attr[text]
        self.movies.sort(attr)
        self.button_creat()

    def button_creat(self):
        """Clear all buttons"""
        self.source.ids.movie_button.clear_widgets()
        for i, movie in enumerate(self.movies.movies):
            temp_button = Button(id=str(i))
            temp_button.bind(on_release=self.movie_button)
            title = movie.title
            year = movie.year
            category = movie.category

            if movie.is_watched:
                watched = " (watched)"
                temp_button.background_color = [1, 1, 1, 1]
            else:
                watched = ""
                temp_button.background_color = button_color
            text = "{} from {},  {} {}".format(title, year, category, watched)
            temp_button.text = text
            # add button to movies_press
            self.source.ids.movie_button.add_widget(temp_button)

    def add_button(self):
        """add movie button."""
        title = self.source.ids.title.text
        year = self.source.ids.year.text
        category = self.source.ids.category.text

        if (title == "") | (year == "") | (category == ""):
            self.information = "All fields must be completed."
            self.bottom_inf()
        else:
            try:
                year = int(year)
                if year < 1:
                    # if the year is less than 1
                    self.information = "Year must be bigger than  0."
                    self.bottom_inf()
                else:
                    movie = Movie(title, year, category)
                    self.movies.add_movies(movie)
                    self.all_inf()
            except ValueError:
                # year is a message
                self.information = "Please input a valid number."
                self.bottom_inf()

    def clear_button(self):
        """What the Clear Button do."""
        self.source.ids.title.text = ""
        self.source.ids.year.text = ""
        self.source.ids.category.text = ""

    def movie_button(self, instance):
        """creat movie button."""
        i = int(instance.id)
        movie = self.movies.movies[i]
        if movie.is_watched:
            movie.unwatch()
            self.information = "You can watch {}.".format(movie.title)
        else:
            movie.watch()
            self.information = "You have watched {}.".format(movie.title)
        self.all_inf()

    def top_inf(self):
        """display the information on the top."""
        self.source.ids.top_message.text = "To watch: {}  Watched: {}".format(self.movies.unwatched_num(),
                                                                              self.movies.watched_num())

    def bottom_inf(self):
        """display the information of bottom."""
        self.source.ids.bottom_message.text = self.information

    def all_inf(self):
        """display all information"""
        self.button_creat()
        self.top_inf()
        self.bottom_inf()

    def run_exit(self):
        self.movies.save_movies(DATA)


if __name__ == '__main__':
    MoviesToWatchApp().run()
