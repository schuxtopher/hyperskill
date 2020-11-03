def tracklist(**artists):
    for artist, albums in artists.items():
        print(artist)
        for album, track in albums.items():
            print(f"ALBUM: {album} TRACK: {track}")
