M = 998244353
d = input()
n,k = int(d), len(d)

r = 10 ** k

rest = n % M * (r ** n -1) % M * pow(r-1, -1, M)
print(rest)

#むりぽ