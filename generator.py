def value(k):
  for i in range(k):
    yield i
for i in value(4):
  print(i)
value1 = iter(value(4))
for i in value1:
  print(i)