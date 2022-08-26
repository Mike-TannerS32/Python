"""n = int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end='')
    print('')"""
sum = 0
N = int(input())
sumTot= 0
for i in range(1, N+1):
    sumTot += i
for i in range(1,N):
    a = int(input())
    sum = sum + a
r = sumTot - sum
print(r)