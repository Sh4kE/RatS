class Inserter:
    def __init__(self, site):
        self.site = site
        self.failed_movies = []

    def insert(self, movies, source):
        raise NotImplementedError("Should have implemented this")
