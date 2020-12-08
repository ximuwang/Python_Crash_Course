# A module for 8-15
def print_models(unprinted_designs, completed_desings):
    '''
    Simulate printing each design, until none are left.
    Move each design to completed_designs after printing
    '''
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # Simulate creating a 3D print from the design.
        print('Printing Model: ' + current_design)
        completed_desings.append(current_design)

def show_completed_designs(completed_designs):
    '''Show all the models that were printed'''
    print('\nThe following models have been printed: ')
    for completed_design in completed_designs:
        print(completed_design)
# unprinted_designs = ['Iphone case', 'robor pendant', 'dodecahedron']
# completed_designs = []

# print_models(unprinted_designs[:], completed_designs)
# show_completed_designs(completed_designs)
# print(unprinted_designs)