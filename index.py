# numbers in python

product_id = 123 
sale_price = 14.99
tip_percentage = 1/5
new_product = 150

print(sale_price + new_product)

# integer
# float
# fraction
# integer

# order of opearations in python

print('Addition')
print(100 + 42)

print('Subtraction')
print(100 - 42)

print('Division')
print(100 / 42)
print(100 / 38)

print('Floor Division')
print(100 // 42)
print(100 // 38)

print('Multiplication')
print(100 * 42)

print('Modulus')
print(100 % 42)

print('Exponents')
print(100 ** 42)

# assignment operators in python

total = 100

total = total + 10
total += 10
total -= 10
total *= 2
total /= 10
total //= 10
total **= 2
total %= 2

product_two = 120
product_three = 10

total += product_two
total += product_three

print(total)

# decimal vs float in python

from decimal import Decimal

product_cost = 88.40
commission_rate = 0.08
qty = 450

product_cost += (commission_rate * product_cost)
print(product_cost * qty) # 42962.4

product_cost = Decimal(88.40)
commission_rate = Decimal(0.08)
qty = 450

product_cost += (commission_rate * product_cost)
print(product_cost * qty) # 42962.40000000000282883716451


# integer, complex, float, decimal

from decimal import Decimal

product_cost = 88.80
commission_rate = 0.08
qty = 450

print(int(product_cost))
print(float(qty))
print(Decimal(product_cost))
print(complex(commission_rate))

# popular math in python

import math

loss = -20.25
product_cost = 89.99

print(abs(loss))
print(math.floor(product_cost))
print(math.ceil(product_cost))
print(abs(math.floor(loss)))
print(round(product_cost))
print(math.sqrt(product_cost))
print(math.pow(5, 2))
print(5 ** 2)

# order of operation in python

"""
Please -> Parans ()
Excuse -> Exponents **
My -> Multiplication *
Dear -> Division /
Aunt -> Addition +
Sally -> Subtraction -

8 + 2 * 5 - (9 + 2) ** 2
8 + 2 * 5 - 11 ** 2
8 + 2 * 5 - 121
8 + 10 - 121
-103
"""

calculation = 8 + 2 * 5 - (9 + 2) ** 2

print(calculation)

# manual exponent

def manual_exponent(num, exp):
  counter = exp - 1
  total = num

  while counter > 0:
    total *= num
    counter -= 1

  return total

print(manual_exponent(2, 3))
print(manual_exponent(10, 2))

# reduce function

from functools import reduce

def manual_exponent(num, exp):
  computed_list = [num] * exp
  return(reduce(lambda total, element: total * element, computed_list))

print(manual_exponent(2, 3))
print(manual_exponent(10, 2))

# overview lists in python

"""
User Database Query
Kristine
Tiffany
Jordan
"""

users = ['Kristine', 'Tiffany', 'Jordan']

print(users)

users.insert(1, 'Anthony')

print(users)

users.append('Ian')

print(users)

print([users[2]])

users[4] = 'Brayden'

print(users)

# removing element lists in python

users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

print(users)

users.remove('Jordan')

print(users)

popped_user = users.pop()

print(popped_user)
print(users)

del users[0]

print(users)

# nested lists

users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

ids = [1, 2, 3, 4]

mixed_list = [42, 10.3, 'Altuve', users]

print(mixed_list)

user_list = mixed_list.pop()

print(user_list)
print(mixed_list)

nested_lists = [[123], [234], [345]]

# negative indexes in python

tags = ['python', 'development', 'tutorials', 'code']

number_of_tags = len(tags)
last_item = tags[-1]
index_of_last_item = tags.index(last_item)

print(number_of_tags)
print(last_item)
print(index_of_last_item)

# sort lists in python

tags = ['python', 'development', 'tutorials', 'code']

print(tags)

tags.sort()

print(tags)

tags.sort(reverse=True)

print(tags)

totals = [234, 1, 543, 2345]

totals.sort(reverse=True)

print(totals)

# url query string in python

# https://www.google.com/search?q=python+development+tutorial

uri = 'https://www.google.com/search?q='
tags = ['python', 'development', 'tutorial']
formatted_tags = '+'.join(tags)
query_uri = f'{uri}{formatted_tags}'

print(query_uri)

# ranges in python lists


tags = ['python', 'development', 'tutorials', 'code']

tag_range = tags[2:]
tag_range = tags[0:2]
tag_range = tags[:2]
tag_range = tags[0:-1]

print(tag_range)

# slices and ranges

tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
  'computer science'
]

tag_range = tags[1:-1:2]
tag_range = tags[::-1]

print(tag_range)

tags.sort(reverse=True)

print(tags)

# sorted function

sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]

sorted_list = sorted(sale_prices, reverse=True)

print(sorted_list)

# how to find the median

# Tools:
# - math library
# - sorted function
# - list slicing
# - computations

sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]

sorted_list = sorted(sale_prices)
num_of_sales = len(sorted_list)
half_slice = math.floor(num_of_sales/2)
first_sales_items = sorted_list[:half_slice]
last_sales_items = sorted_list[-(half_slice):]
median = sorted_list[half_slice:(half_slice + 1)]

print(sorted_list)
print(num_of_sales)
print(first_sales_items)
print(last_sales_items)
print(median)

# slice class

tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
]

print(tags[1:4:2])

slice_obj = slice(1, 4, 2)

print(slice_obj.start)
print(slice_obj.stop)
print(slice_obj.step)

print(tags[slice_obj])

# Add to a list with in place and copy processes

tags = ['python', 'development', 'tutorials', 'code']

# Nope
tags[-1] = 'Programming'

# In Place
tags.extend('Programming')
tags.extend(['Programming'])

# New List
new_tags = tags + ['Programming']

print(new_tags)

print(tags)

# weighted lottery

# import numpy as np

def weighted_lottery(weights):
    container_list = []

    for (name, weight) in weights.items():
        for _ in range(weight):
            container_list.append(name)

    # return np.random.choice(container_list)

#  weights = {
#      'winning': 1,
#      'losing': 1000
#  }
#
#  print(weighted_lottery(weights))

other_weights = {
    'green': 1,
    'yellow': 2,
    'red': 3
}

print(weighted_lottery(other_weights))



# overview of python dictionaries

players = {
  "ss": "Correa",
  "2b": "Altuve",
  "3b": "Bregman",
  "DH": "Gattis",
  "OF": "Springer",
}

second_base = players['2b']
designated_hitter = players['DH']

print(designated_hitter)


# nested collections in python dictionaries

teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
}

astros = teams['astros']
print(astros)
print(teams['angels'])
print(teams['yankees'])

# add new key/value python pairs in dictionaries

teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"]
}

teams['red sox'] = ['Price', 'Betts']

print(teams)


# get functions

teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ['Price', 'Betts'],
}

featured_team = teams.get('yankees', 'No featured team')

print(featured_team)

# view objects in python dictionnaries

players = {
  "ss" : "Correa",
  "2b" : "Altuve",
  "3b" : "Bregman",
  "DH" : "Gattis",
  "OF" : "Springer",
}

# print(players.values())
# print(players.keys())
# print(players.items())
# print(list(players.values())[1])
players_names = list(players.copy().values())
print(players_names)

teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

team_groups = teams.items()

print(len(team_groups))
print(list(team_groups)[1][1][0])

# deleting items in python dictionnaries

teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

del teams['angels']
removed_team = teams.pop('mets', 'Team not found')

print(teams)
print(removed_team)

# working with lists of nested dictionnaries

teams = [
  {
    'astros': {
      '2B': 'Altuve',
      'SS': 'Correa',
      '3B': 'Bregman',
    }
  },
  {
    'angels': {
      'OF': 'Trout',
      'DH': 'Pujols',
    }
  }
]

# print(teams[0])

team_num = teams[1].get('angels', 'team not found')

print(list(team_num.values())[1])

# Build Histogram in python

"""
g $$$$$$$$$$$$$$$$$$$$
f $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
t $$$$$$$$$$
o $$$$$$$$$$$$
"""

sales = {
  'google': 20,
  'facebook': 42,
  'twitter': 10,
  'offline': 12,
}

print('g ' + sales['google'] * '$')
print('f ' + sales['facebook'] * '$')
print('t ' + sales['twitter'] * '$')
print('o ' + sales['offline'] * '$')

# introduction to Tuples

# List: []
# Dictionary: {}
# Tuple: ()

# Tuple: immutable it can not be changed
# List: mutable

post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

# Tuple unpacking
title, sub_heading, content = post

# Equivalent to Tuple unpacking
# title = post[0]
# sub_heading = post[1]
# content = post[2]

print(title)
print(sub_heading)
print(content)

# add elements to a tuble

post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

print(id(post))
print(id(post))

post += ('published',)

print(id(post))

title, sub_heading, content, status = post

print(title)
print(sub_heading)
print(content)
print(status)

# working with lists nested in Tuples


post = ('Python Basics', 'Intro guide to Python', 'Some cool python content')

tags = ['python', 'coding', 'tutorial']

post += (tags,)

print(post[-1][1])



# guide to slices in Tuples

post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')

print(post[1::2])

# remove elements from python Tuple

post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')

# Removing elements from end
post = post[:-1]

# Removing elements from beginning
post = post[1:]

# Removing specific element (messy/not recommended)
post = list(post)
post.remove('published')
post = tuple(post)

print(post)
