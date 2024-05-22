A = int(input())
B = int(input())
C = int(input())

X = int(input())

a = 1
b = 1
c = 1
count = 0

for a in range(A + 1):
  for b in range(B + 1):
    for c in range(C + 1):
      product = a * 500 + b * 100 + c * 50
      if product != X:
        continue
      if product == X:
        count += 1

print(count)