def digital_root(n):
  if n <= 10:
    return n
  else:
    return digital_root(sum([int(num) for num in str(n)]))
n = 1351
print(digital_root(n))