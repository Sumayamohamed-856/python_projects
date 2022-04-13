#  Project Requirements: Build FizzBuzz in Python

def fiizbuz(max_value):
  
  for num in range(1, max_value + 1):
    if num % 3 == 0 and num % 5 == 0:
     print('fiizBuzz')
    elif num % 3 == 0:
      print('fiiz')
    elif num % 5 == 0:
      print('Buzz')
    else:
     print(num)


fiizbuz(100)


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

def even_number(max_num):
  for max_number in range(1, max_num):
    if max_number % 2 == 1:
      print(max_number)

even_number(20)