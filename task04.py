class Movie:
    def __init__(self, title, genre, duration, rating):
        self.title = title
        self.genre = genre
        self.duration = int(duration)
        self.rating = float(rating)
        
new_movie = Movie("reyd", "treller", 210, 5.5)


print("Kino nomi:", new_movie.title)
print("Janri:", new_movie.genre)
print("Davomiyligi:", new_movie.duration, "daqiqa")
print("IMDB reytingi:", new_movie.rating)

        