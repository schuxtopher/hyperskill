matches = [input().split() for _ in range(int(input()))]
winners = [player[0] for player in matches if player[1] == 'win']

print(winners, len(winners), sep='\n')
