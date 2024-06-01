N, Y = map(int, input().split())
A = 0
B = 0

for A in range(N + 1):
  for B in range(N - A + 1):
    C = N - A - B
    guess = A * 10000 + B * 5000 + C * 1000
    if guess == Y:
      print(f"{A} {B} {C}")
      exit()
    B += 1

print("-1 -1 -1")