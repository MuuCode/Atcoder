N, A, B = map(int, input().split())

sum = 0
total = 0
i = 1
for i in range(N + 1):
  j: int = i
  sum = 0
  while j > 0:
    sum += j % 10
    if j < 10:
      break
    j //= 10
  if (sum >= A and sum <= B):
    total += i

print(total)
