import math

edge_length = int(input())
octahedron = {'area': lambda a: 2 * math.sqrt(3) * math.pow(a, 2),
              'volume': lambda a: 1 / 3 * math.sqrt(2) * math.pow(a, 3)}

print(f"{octahedron['area'](edge_length):.02f} {octahedron['volume'](edge_length):.02f}")
