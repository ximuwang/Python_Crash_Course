# 8-7
def make_album(artist, title, tracks = 0):
    music_album = {'artist': artist.title(),
                   'title': title.title(),
                   }
    if tracks:
        music_album['tracks'] = tracks
    return music_album
album = make_album('Beattles', 'Abbey Road', tracks = 8)
print(album)
album = make_album('metallica', 'ride the lighting')
print(album)
album = make_album('beethoven', 'ninth symphony')
print(album)
album = make_album('willie nelson', 'red-head stranger')
print(album)
