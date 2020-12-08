# 8-8 User albums
def make_album(artist, title, tracks = 0):
    '''Build a dictionary containing the info about an album'''
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

# prepare the prompts
artist_prompt = 'Who is the artist: '
title_prompt = '\nWhat albums are you thinking of: '
# Let user know how to quit:
print('(Enter "q" anytime to quit)')
while True:
    title = input(title_prompt).title()
    if title == "q" or 'Q':
        break
    artist = input(artist_prompt).title()
    if artist == "q" or 'Q':
        break

    album = make_album(artist, title)
    print(album)

print('\nThanks for your response')
