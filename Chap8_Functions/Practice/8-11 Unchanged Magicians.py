# 8-11 Unchanged Magicians
magicians = ['quentin coldwater', 'julia wicker', 'alice quinn', 'eliot waugh', 'william adiyodi']
completed_magicians = []
def show_magicians(magicians):
    while magicians:
        current_magician = magicians.pop()
        current_magician = current_magician.title()
        completed_magicians.append(current_magician)
        print('Currently presenting: ' + current_magician)
def make_great(completed_magicians):
    for magician in completed_magicians:
        print('Great Magician ' + magician)
show_magicians(magicians[:])
make_great(completed_magicians)
print(magicians)
print(completed_magicians)


