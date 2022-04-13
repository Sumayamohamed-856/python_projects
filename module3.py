# How to use a Tuple as a Dictionary key in python

priority_index = {
  (1, 'premier'): [1, 34, 12],
  (1, 'mvp'): [84, 22, 24],
  (2, 'standard'): [93, 81, 3],
}

print(list(priority_index.keys()))


# Guide to python zip function

positions = ['2b', '3b', 'ss', 'dh']
players = ['Altuve', 'Bregman', 'Correa', 'Gattis']

scoreboard = zip(positions, players)

print(list(scoreboard))


# Introduction to the python set data structure

tags = {
  'python',
  'coding',
  'tutorials',
  'coding'
}

print(tags)

# Nope
# print(tags[0])

query_one = 'python' in tags
query_two = 'ruby' in tags

print(query_one)
print(query_two)


# Various methods for merging python sets

tags_one = {
  'python',
  'coding',
  'tutorials',
  'coding'
}

tags_two = {
  'ruby',
  'coding',
  'tutorials',
  'development'
}

# merged tags
merged_tags = tags_one | tags_two
print(merged_tags)

# tags in tags_one but not in tags_two
exclusive_to_tag_one = tags_one - tags_two
print(exclusive_to_tag_one)

# tags in tags_two but not in tags_one
exclusive_to_tag_two =  tags_two - tags_one
print(exclusive_to_tag_two)

# tags found in both tags_one and tags_two
universal_tags = tags_one & tags_two
print(universal_tags)


# Build Html Heading Generator function in python

def heading_generator(title, heading_type):
  return f'<h{heading_type}>{title}</h{heading_type}>'

print(heading_generator('Hi there', '1'))
print(heading_generator('greeting', '1'))


# Implement Python Loops for Lists, Tuples, and Dictionaries

players = ['Altuve', 'Bregman', 'Correa', 'Gattis']
players = ('Altuve', 'Bregman', 'Correa', 'Gattis')

for player in players:
  print(player)

players = {
  '2b': 'Altuve',
  '3b': 'Bregman',
  'ss': 'Correa',
  'dh': 'Gattis'
}

for position, player, in players.items():
  print('keyvalues', position)
  print('names', player)


# Loop Through the Characters of a Python String

alphabet = 'abcdef'

for letter in alphabet:
  print(letter)


# Guide to looping ranges in python

for num in range(1, 10):
  print(num)

for num in range(1, 10, 2):
  print(num)


# Guide to Continue and Break in Python Loops

usernames = [
  'jon',
  'tyrion',
  'theon',
  'cersei',
  'sansa',
]

for username in usernames:
  if username == 'cersei':
    print(f'Sorry, {username}, you are not allowed')
    continue
  else:
    print(f'{username} is allowed')

for username in usernames:
  if username == 'cersei':
    print(f'{username} was found at index {usernames.index(username)}')
    break
  print(username)


# overview of while loops

nums = list(range(1, 100))

while len(nums) > 0:
  print(nums.pop())

def guessing_game():
  while True:
    print('What is your guess?')
    guess = input()

    if guess == '42':
      print('You correctly guessed it!')
      return False
    else:
      print(f"No, {guess} isn't the answer, please try again\n")

guessing_game()


# How to Combine and Flatten Lists in Python with the For / In Loop

legacy_customers = ['Alice', 'Bob']
new_customers = ['Tiffany', 'Kristine']

raw_db = [legacy_customers, new_customers]

print(raw_db)

for legacy_customer in legacy_customers:
  new_customers.append(legacy_customer)

print(new_customers)


# Introduction to Using List Comprehension in Python

num_list = range(1, 11)
cubed_nums = []

for num in num_list:
  cubed_nums.append(num ** 3)

cubed_nums = [num ** 3 for num in num_list]

print(cubed_nums)

even_numbers = []

for num in num_list:
  if num % 2 == 0:
    even_numbers.append(num)

even_numbers = [num for num in num_list if num % 2 == 0]

print(even_numbers)


# Overview of Python Conditionals

# Single condition
age = 25

if age < 25:
  print(f"I'm sorry, you need to be at least 25 years old")

# if/else
age = 55

if age < 25:
  print(f"I'm sorry, {age} is under 25 years old")
else:
  print(f"You're good to go, {age} fits in the range to rent a car")

# if/elif/else
age = 55

if age < 25:
  print(f"I'm sorry, {age} is under 25 years old")
elif age > 100:
  print(f"I'm sorry, {age} is over 100 years old")
else:
  print(f"You're good to go, {age} fits in the range to rent a car")


# How to Use the Ternary Operator in Python Conditionals

role = 'guest'

auth = 'can access' if role == 'admin' else 'cannot access'

if role == 'admin':
  auth = 'can access'
else:
  auth = 'cannot access'

print(auth)


# Full List of Python Conditional Operators

# == Equality
# != Inequality
# <> Inequality (deprecated)
# >  Greater than
# >= Greater than or equal to
# < Less than
# <= Less than or equal to

username = 'sum'

if username != 'voo':
  print('Welcome Jon')
else:
  print('You shall not pass!')


age = 55

if age <= 50:
  print('You good to go')
else:
  print('you not good to go')
  

user_list = ['samiya' 'siham']
second_list = ['samiya' 'siham']

if user_list == second_list:
  print('they match')


# How to Check if a Value is Included in a Python String or List

sentence = 'The quick brown fox jumped over the lazy Dog'
word = 'dog'

if word.lower() in sentence.lower():
  print('The word is in the sentence')
else:
  print('The word is not in the sentence')


nums = [1, 2, 3, 4]

if 3 in nums:
  print('The number was found')
else:
  print('The number was not found')


# How to Build Compound Conditionals in Python

username = 'jonsnow'
email = 'jon@snow.com'
password = 'thenorth'

if username == 'jonsnow' and password == 'thenorth':
  print('Access permitted')
else:
  print('Not allowed')


if (username == 'jonsnow' or email == 'jon@snow.com') and password == 'thenorth':
  print('Access permitted')
else:
  print('Not allowed')


if username == 'jonsnow' or password == 'thenorth':
  print('Access permitted')
else:
  print('Not allowed')


logged_in = True
standard_user = False

if logged_in and not standard_user:
  print('You can access the admin dashboard')
else:
  print('You can only access the standard dashboard')


# How to remove first and last element from a list

def remove_first_last(some_content):
  first, *second, last = some_content
  return second

list = ['Html', 'design', 'laptop', 'books']

html = ['Html', 'design', 'grapes', 'books']

if list == html:
 print('error')

print(remove_first_last(html))


# Basic Syntax for Creating Python Functions

def full_name(first, last):
  print(f'{first} {last}')


full_name('Kristine', 'Hudgens')

def auth(email, password):
  if email == 'kristine@hudgens.com' and password == 'secret':
    print('You are authorized')
  else:
    print('You are not authorized')


auth('kristine@hudgens.com', 'asdf')

def hundred():
  for num in range(1, 101):
    print(num)


hundred()

def counter(max_value):
  for num in range(1, max_value):
    print(num)


counter(501)


# What Does it Mean to Return a Value from a Python Function?

def full_name(first, last):
  return f'{first} {last}'


kristine = full_name('Kristine', 'Hudgens')

def greeting(name):
  print(f'Hi {name}!')


greeting(kristine)


# How to Nest Functions in Parent Functions in Python

def greeting(first, last):
  def full_name():
    return f'{first} {last}'

  print(f'Hi {full_name()}!')


greeting('Kristine', 'Hudgens')


# Guide to default arguments in python functions

def greeting(name = 'Guest'):
  print(f'Hi {name}!')

greeting()
greeting('Kristine')

# Nope
def some_function(collection = []):
  collection.append(1)
  print(id(collection))
  return collection


print(some_function())
print(some_function())


# How to Utilize Named Function Arguments in Python

def full_name(first, last):
  print(f'{first} {last}')


full_name('Kristine', 'Hudgens')
full_name(first = 'Kristine', last = 'Hudgens')
full_name(last = 'Hudgens', first = 'Kristine')


# Guide to Function Argument Unpacking in Python

def greeting(*args):
  print('Hi ' + ' '.join(args))


greeting('Kristine', 'M', 'Hudgens')
greeting('Tiffany', 'Hudgens')


def greeting(*names):
  print('Hi ' + ' '.join(names))


greeting('Kristine', 'M', 'Hudgens')
greeting('Tiffany', 'Hudgens')


def greeting(time_of_day, *args):
  print(f"Hi {' '.join(args)}, I hope that you're having a good {time_of_day}")


greeting('Afternoon', 'Kristine', 'M', 'Hudgens')
greeting('Morning', 'Tiffany', 'Hudgens')


# Overview of Keyword Arguments in Python Functions

def greeting(**kwargs):
  print(kwargs)


greeting()
greeting(first = 'Kristine', last = 'Hudgens', very = 'welcome')

def greeting(**kwargs):
  if kwargs:
    print(f"Hi {kwargs['first']} {kwargs['last']}, have a great day!")
  else:
    print('Hi Guest!')


greeting()
greeting(first = 'Kristine', last = 'Hudgens')



# Combine All Argument Types in a Single Python Function

def greeting(time_of_day, *args, **kwargs):
  print(f"Hi {' '.join(args)}, I hope that you're having a good {time_of_day}.")

  if kwargs:
    print('Your tasks for the day are:')
    for key, val in kwargs.items():
      print(f'{key} -> {val}')


greeting('morning',
         'Sumaya', 'moha',
         first = 'Empty dishwasher',
         second = 'Take pupper out',
         third = 'math homework')



# Guide to Python Lambdas

full_name = lambda first, last: f'{first} {last}'


def greeting(name):
  print(f'Hi there {name}')


greeting(full_name('Kristine', 'Hudgens'))


