def manual_incrementing_matrix(n):
  #matrix n * n
  matrix = [[None for y in range(n)] for x in range(n)]

  counter = 0

  for idx, el in enumerate(matrix): 
    for nested_idx, nested_el in enumerate(el):
      matrix[idx][nested_idx] = counter + nested_idx
    counter += 1

  return(matrix)
  
print (manual_incrementing_matrix(5))

# varibles

name = 'sumaya'
post_count = 55

print(name)
print(post_count)

# overview of strings with numbers

meal_completed = True
sub_total = 100
tip = sub_total * 1/5
total = sub_total + tip
receipt = "Your total is " + str(total)
print(receipt)

# variables

# meal_completed = True
# total = 100
# tip = total * 1/5
# total = total + tip
# receipt = "Your total is " + str(total)
# print(receipt)

first = 'Springer'
second = 'Bregman'
third = 'Altuve'

print(first)

first = third

print(first)


# comments

# Single Line:
# I'm a single line comment

name = 'Kristine Hudgens' # TODO: Split into two variables
print(name)

"""
Multi-Line:

Aenean lacinia bibendum nulla sed consectetur.

Aenean lacinia bibendum nulla sed consectetur.

Aenean lacinia bibendum nulla sed consectetur.
"""

# more on strings

sentence = 'The quick brown fox jumped over the lazy dog'

sentence_two = 'That is my dog\'s bowl'

sentence_three = "That is my dog's bowl"

sentence_four = "Tiffany said, \"That is my dog's bowl\""

print(sentence_four)


# upper, lower case, capitalize on strings


sentence = 'The quick brown fox jumped'
sentence_two = sentence.upper()

print(sentence)
print(sentence_two)

sentence = 'the quick brown fox jumped'.capitalize()
print(sentence)

sentence = 'the quick brown fox jumped'.title()
print(sentence)

sentence = 'the Quick Brown fOx jumped'
print(sentence.lower())


# number rogers

# The quick brown fox jumped
# T => 0
# h => 1
# e => 2
# ' ' => 3

starter_sentence = 'The quick brown fox jumped'

# first = starter_sentence[0]

# second = starter_sentence[1]

# third = starter_sentence[2]

# new_sentence = first + second + third

# print(new_sentence)

first_word = starter_sentence[0:3]
new_sentence = 'thy' + starter_sentence[3:]
print(new_sentence)


# Heredoc

content = """
Nullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.

Vestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.

Integer posuere erat a ante venenatis dapibus posuere velit aliquet.
""".strip()

print(content)


# line breakes, multi string sentences

# Integer posuere erat a ante venenatis dapibus posuere velit aliquet.
# """

# print(repr(content))

long_string = '\nNullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.\n\nVestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.\n\nInteger posuere erat a ante venenatis dapibus posuere velit aliquet.\n'

print(long_string)


# functions in python

import operator
from functools import reduce

def dynamic_reducer(collection, op):
    operators = {
        "+": operator.add,
        "_": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
}
    return reduce((lambda total, element: 
    operators[op](total, element)), collection)

print(dynamic_reducer([1, 2, 3], '+'))
print(dynamic_reducer([1, 2, 3], '_'))
print(dynamic_reducer([1, 2, 3], '*'))
print(dynamic_reducer([1, 2, 3], '/'))


# string interpolation

name = 'Kristine'
customer = f'Hi {name}'
greeting = f'This is my {{bracket}} blog test'
print(greeting)
print(customer)

name = 'Kristine'
customer = f'Hi {name}'
greeting = f'This is my {{bracket}} blog test'
product = 'Python elearning course'

email_content = f"""
Hi {name}

Thank you for purchasing {product}

Regards,

Sales Team
"""
print(greeting)
print(customer)
print(email_content)

# old format

name = 'Kristine'
age = 12
product = 'Python eLearning course'
from_account = 'Jordan'

greeting = "Product Purchase: {2} - Hi {0}, you are listed as {1} years old. - {3}".format(name, age, product, 'Jordan')

greeting = f"Product Purchase: {product} - Hi {name}, you are listed as {age} years old. - {from_account}"

print(greeting)


# query string methods

sentence = 'The quick brown fox jumped over the lazy dog.'

# query = sentence.find('oops')
# query_two = sentence.index('oops')

# print(query)
# print(query_two)

query = 'oops' in sentence

print(query)

# replace function in string

sentence = 'The quick brown fox jumped over the lazy dog.'

sentence = sentence.replace('quick', 'slow')

print(sentence.replace('quick', 'slow'))
print(sentence)

# working with negative index

sentence = 'The quick brown fox jumped over the lazy dog.'

print(sentence[-4:])

# python strip

url = 'https://google.com'

print(url.strip())

print(url.strip('https://'))

url = url.lstrip('https://')
url = url.rstrip('.com')

print(url.capitalize())

# partition

heading = "Python: An Introduction, and Python: Advanced"

header, _, subheader = heading.partition(': ')

print(header)
print(subheader)

first, second, third = heading.partition(': ')

print(first)
print(second)
print(third)

# splits in string

tags = 'python,coding,programming,development'

list_of_tags = tags.split(',')
list_of_tags = tags.split()

print(list_of_tags)

# heading = "Python: An Introduction"

# heading, subheading = heading.split(': ')

# print(heading)
# print(subheading)

# Alpha numric and numric functions in strings

api_data = '5'
greeting = 'Hi there'

print(api_data.isalpha())
print(greeting.isalpha())

print(api_data.isnumeric())
print(greeting.isnumeric())

# checkpoint 3

greeting = 'Welcome back'
numbers = 5
meeting = True
list_items = ['books', 'pens', 'laptops']
names = 'harry,alex,susie,jared,gail,conner'

index = greeting[0:3]
string = greeting[0:7]
string_two = greeting.upper()

items_lists = list_items

first_element = list_items[-3]

name_lists = names.split(',')

addition_of_numbers = numbers + 5

last_element = list_items[-1]

age = f'Under below age {numbers} you qualify for free purchase'

customers = "hello world."

print(index)
print(items_lists)
print(first_element)
print(addition_of_numbers)
print(last_element)
print(name_lists)
print(string)
print(string_two)
print(age)
print(customers)

# A descriptive logo is that textual and visual design elements and 
# indistinctive logo is distinctive logo are more like image brand and they show off personality brand