class Movie:
    def __init__(self, title, genre, duration, rating):
        self.title = title
        self.genre = genre
        self.duration = int(duration)
        self.rating = float(rating)
        
new_movie = Movie("reyd", "treller", 210, 5.5)
print(f"{new_movie.title} — {new_movie.genre} janridagi film. Rayting {new_movie.rating}/10")
        