import random

colors = ['red', 'orange']
animals = ['dog', 'cat']
states = ['texas', 'arkansas']
allLists = [colors, animals, states]

colorOption = random.choice(colors)
print(colorOption)
print(len(colorOption))

print(random.choice(animals))
print(random.choice(states))

randomOption = random.choice(allLists)
print(random.choice(randomOption))

