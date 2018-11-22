def collatz(number):
  print('{:.0f}'.format(number), end = ' ')
  if number == 1:
    return 0
  elif number % 2 == 0:
    return 1 + collatz(number / 2)
  else:
    return 1 + collatz(number * 3 + 1)

number = 27
steps = collatz(number)
print(f'\nIt takes {steps} steps to reach 1 from {number}')