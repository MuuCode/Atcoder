A, B = map(int, input().split())
for i in range(3):
  if A == B:
    print(-1)
    break
  if A != i+1 and B != i+1:
    print(i+1)