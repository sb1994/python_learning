sizes = ['small', 'medium', 'large']
colors = ['lavendar', 'teal', 'orange']
animals = ['bear', 'cat', 'dog']


def combine(size, color, animals):
    return '{} {} {}'.format(size, color, animals)


# print(combine(size=sizes, color=colors, animals=animals))

print(list(map(combine, sizes, colors, animals)))
