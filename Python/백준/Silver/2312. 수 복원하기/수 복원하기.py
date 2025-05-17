t = int(input())

for _ in range(t) :
  n = int(input())
  number = 2

  data = {}
  for i in range(n + 1) :
    data[i] = 0

  while n > 1 :
    if n % number != 0 :
      number += 1
    else :
      n /= number
      data[number] += 1

  for i in data.items() :
    if i[1] != 0 :
      print(i[0], i[1])