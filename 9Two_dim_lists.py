#1 Problem maximum
def max():
    o = input().split(' ')
    l = []
    m = int(o[0])
    n = int(o[1])
    row = 0
    col = 0
    for i in range(0,m):
        r = input().split(' ')
        l.append(r)
    max = int(l[0][0])
    for i in range(len(l)):
        for j in range(len(l[i])):
            if int(l[i][j]) > max:
                max = int(l[i][j])
                row = i
                col = j
    return row, col
    
"""
Model 
n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
best_i, best_j = 0, 0
curr_max = a[0][0]
for i in range(n):
    for j in range(m):
        if a[i][j] > curr_max:
            curr_max = a[i][j]
            best_i, best_j = i, j
print(best_i, best_j)
"""

#2 Snowflake
n = int(input())
l = [['.'] * n for i in range(n)]
for  i in range(len(l)):
    l[i][i] = '*'
    l[n//2][i] = '*'
    l[i][n//2] = '*'
    l[i][n-i-1] = '*'
for row in l:
    print(' '.join(row))

#3 Chess board

n,m = [int(i) for i in input().split()]
a = []
for i in range(n):
    a.append([])
    for j in range(m):
        if (i+j) %2 ==0:
            a[i].append('.')
        else:
            a[i].append('*')
for row in a:
    print(' '.join(row))

#4 Diagonal parallel to the main
n = int(input())
a = []
for i in range(n):
    a.append([])
    for j in range(n):
        a[i].append(abs(i-j))
for row in a:
    print(' '.join([str(i) for i in row]))
"""
Model
n = int(input())
a = [[abs(i - j) for j in range(n)] for i in range(n)]
for row in a:
    print(' '.join([str(i) for i in row]))
"""

#5 side diagonal

n = int(input())
a = [[0]*n for i in range(n)]
for i in range(len(a)):
    for j in range(len(a[i])):
        if j == n-1-i:
            a[i][j] = 1
        if j == n-i:
            a[i][j] = 2
        if j < n and j > n-i:
            a[i][j] = 2
for row in a:
    print(' '.join(str(i) for i in row))

#6 Swap the columns
def swap_columns(a,i,j):
    for k in range(len(a)):
        a[k][i], a[k][j] = a[k][j], a[k][i] #troca de coluna
n,m = [int(i) for i in input().split(' ')]
a = []
for i in range(n):
    l = input().split(' ')
    a.append(l)
s1, s2 = [int(i) for i in input().split(' ')]
swap_columns(a,s1,s2) 
for row in a:
    print(' '.join(str(i) for i in row))

#7 Scale a matrix
n,m = [int(i) for i in input().split(' ')]
a = []
for i in range(n):
    l = input().split(' ')
    a.append(l)
s = int(input())
for i in range (len(a)):
    for j in range(len(a[i])):
        a[i][j] = int(a[i][j])*s
for row in a: 
    print(' '.join(str(i) for i in row))

#8 Multiply two matrices
m,n,r = [int(i) for i in input().split()]
a = [[int(k) for k in input().split()] for i in range(m)]
b = [[int(k) for k in input().split()] for i in range(n)]
c = [[0]*r for i in range(m)]

for i in range(m):
    for k in range(r):
        for j in range(n):
            c[i][k] += a[i][j]*b[j][k]
for row in c :
    print(' '.join(str(i) for i in row))