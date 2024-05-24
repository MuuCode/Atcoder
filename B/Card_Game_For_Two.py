N = int(input())
cards = list(map(int, input().split()))

c_sorted = sorted(cards, reverse=True)
A = 0
B = 0
for i in range(N):
  if i % 2 == 0:
    A += c_sorted[i]
  if i % 2 == 1:
    B += c_sorted[i]

print(A - B)