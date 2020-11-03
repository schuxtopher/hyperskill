planets = open('planets.txt', 'w', encoding='utf-8')
planets.write('\n'.join(['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']))
planets.close()
