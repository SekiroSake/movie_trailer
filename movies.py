# Movie class
class Movie():
    def __init__(self, title, genres, rating, director, actors, poster_image_url, trailer_youtube_url):
        """Create a new instance of a movie.

        title: Movie title.
        genres: List of genres as strings.
        rating: Rating out of 10.
        director: Person instance representing the director.
        actors: List of Person instances representing the actors.
        poster_image_url: URL of the movie poster.
        trailer_youtube_url: URL of the trailer on YouTube.
        """
        self.title = title
        self.genres = genres
        self.rating = rating
        self.director = director
        self.actors = actors
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def genres_list(self):
        """Get a comma separated string of genres."""
        list = ""
        for genre in self.genres:
            list += genre + ", "

        return list.rstrip(", ")

    def actors_list(self):
        """Get a comma separated string of actors."""
        list = ""
        for actor in self.actors:
            list += actor.name + ", "

        return list.rstrip(", ")

class Person():
    def __init__(self, name, dob, image_url):
        """Create a new person instance.

        name: Name of the person.
        dob: Date of birth.
        image_url: URL of the person image.
        """
        self.name = name
        self.dob = dob
        self.image_url = image_url