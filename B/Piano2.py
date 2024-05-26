N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = A + B
C.sort()

A_set = set(A)
for k in range(N+M-1):
  if C[k] in A_set and C[k+1] in A_set:
    print("Yes")
    exit()

print("No")


#0525 first commit
#0526 second commit