"""
Name:HaoxianChen
Date:19.1.2020
Brief Project Description:

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


