with open('../INPUT.TXT', 'r') as f:
  numbers = f.readline().split(' ')
  with open('../OUTPUT.TXT', 'w') as o:
    o.write(str(int(numbers[0]) + int(numbers[1])))