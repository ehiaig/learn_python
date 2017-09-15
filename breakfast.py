""" Breakfast """


def make_breakfast(food, *ingredients):  # Use a * to indicate that arguments take one or more values
    _mix_and_cook()
    if len(ingredients) > 0:
        return '------Yummy {0} with {1}------'.format(food, ', '.join([word for word in ingredients]))
    return '------Yummy {0}------'.format(food)


def _mix_and_cook():
    print('Get the ingredients')
    print('Mix')
    print('Place a pan on a lit stove')
    print('Add some cooking oil to the pan and heat for 30 seconds')
    print('Add the ingredient mixture to the oil')
    print('Flip several times until ready')


print (make_breakfast('Egg', 'Tomatoes, Corianda'))
print
print (make_breakfast('Pancake'))