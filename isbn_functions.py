import re

def look_at_num(number):
    regex = re.compile('^[xX\d+]*$')
    number = filter(regex.match, number)
    numbers = list(number)
    return numbers

def validate_isbn10(number):
  if number[-1] == 'x' or number[-1] == 'X':
    number[-1] = 10
    number = [ int(x) for x in number ]
    counter = 10
    new_arr = []
    for i in number:
      x = i * counter
      counter -= 1
      new_arr.append(x)
    if sum(new_arr) % 11 == 0:
      print(True)
    else:
      print(False)

def validate_isbn13(number):
  number = [ int(x) for x in number ]
  check_digit = number.pop()
  new_arr = []
  for index, value in enumerate(number):
    if index+1 % 2 == 0:
      x = int(value) * 1
      new_arr.append(x)
    else:
      x = int(value) * 3
      new_arr.append(x)
  index = index+1
  num = sum(new_arr)
  final = num % 10
  final = 10 - final
  while True:
    if final <= 9:
      final = final % 10
      break
    if check_digit == final:
      print(True)
    else:
      print(False)

def isbn10_or_isbn13(number):
  numbers = look_at_num(number)
  if len(numbers) == 13:
    validate_isbn13(numbers)
  elif len(numbers) == 10:
    validate_isbn10(numbers)
  else:
    return print("Sorry, this is not a valid isbn")