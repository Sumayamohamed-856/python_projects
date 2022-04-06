import math

teams = ['facebook', 'google', 'microsoft']

players = ('groups', 'chat', 'live')

members = {
  'b1': 'dark',
  'b2': 'gray',
  'b3': 'yellow',
  'b4': 'black'
}

price = 16.99

price_one = 25

price_two = 0.025

print(round(price))
print(math.sqrt(price))

first_element_dic = members['b1']
print(first_element_dic)

first, second, third = players
print(second)

teams.append('friends')
print(teams)

teams[0] = 'youtube'
print(teams)

teams.sort()
print(teams)

players += ('marketing',)
print(players)