class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    artists_count = artist_count

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artists_count()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    def add_to_genres(self):
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    def add_to_artists(self):
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    def add_to_genre_count(self):
        Song.genre_count[self.genre] = Song.genre_count.get(self.genre, 0) + 1

    def add_to_artists_count(self):
        Song.artists_count[self.artist] = Song.artists_count.get(
            self.artist, 0) + 1
        Song.artist_count = Song.artists_count

    def add_to_artist_count(self):
        self.add_to_artists_count()
