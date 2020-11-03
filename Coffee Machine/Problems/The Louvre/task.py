class Painting:
    museum = "Louvre"

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year


painting = Painting(input(), input(), input())
print(f'"{painting.title}" by {painting.artist} ({painting.year}) hangs in the {Painting.museum}.')
