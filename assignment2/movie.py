"""..."""


class Movie:
    """creat a class of movie"""

    def __init__(self, title="", year=0, category="", is_watched=False):
        self.title = title
        self.year = year
        self.category = category
        self.is_watched = is_watched
        """make a function of movies"""

    def __str__(self):
        """Determine if had seen the movie"""
        if self.is_watched:
            watch = "w"
        else:
            watch = "u"
        return "{} ({}) {} {}".format(self.title, self.year, self.category, watch)

    def watch(self):
        """if had watched the movie, it is watch"""
        self.is_watched = True

    def unwatch(self):
        """if had not watched the movie, it is unwatch"""
        self.is_watched = False

    pass
