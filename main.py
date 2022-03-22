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