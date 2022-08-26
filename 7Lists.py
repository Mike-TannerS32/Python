#1 Even indices
"""n = input()
for i in range(len(n)):
    s = n.split(" ")
for i in range(len(s)):
    if i % 2 == 0:
        print(s[i])"""
"""
a = input().split()
for i in range(0, len(a), 2):
    print(a[i])
"""

#2 Even elements
"""
s = input().split()
for i in range(len(s)):
    if int(s[i])%2==0:
        print(s[i])"""
"""
a = [int(i) for i in input().split()]
for elem in a:
    if elem % 2 == 0:
        print(elem)
"""
#3 Greater than previous
"""a = input().split()
for i in range(1,len(a)):
    if(int(a[i+1]) > int(a[i])):
        print(a[i])"""

#4 Neighbors of the same sign

"""m = []
a = input().split()
for b in a:
    m.append(int(b))

for i in range(len(m)-1):
    if m[i]>0 and m[i+1]>0:
        print(m[i],end = ' ')
        print(m[i+1])
        break
    elif m[i]<0 and m[i+1]<0:
        print(m[i])
        print(m[i+1])
        break"""
"""
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i - 1] * a[i] > 0:
        print(a[i - 1], a[i])
        break
"""

#5 Greater than neighbours
"""m = []
a= input().split()
counter = 0
for b in a:
    m.append(int(b))
for i in range(1,len(m)-1):
    if(m[i]> m[i-1] and m[i]> m[i+1]):
        counter += 1
print(counter)"""

"""
a = [int(i) for i in input().split()]
counter = 0
for i in range(1, len(a) - 1):
    if a[i - 1] < a[i] > a[i + 1]:
        counter += 1
print(counter)
"""

#6 largest element
"""m= []
maximum= 0
index = 0
a = input().split()
for b in a:
    m.append(int(b))
maximum = max(m)
index = m.index(maximum)
print(maximum, end= ' ')
print(index)"""

"""
index_of_max = 0
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[index_of_max]:
        index_of_max = i
print(a[index_of_max], index_of_max)
"""

#7 Number of distinct elements
"""a = input().split()
m = []
counter = 1
for b in a:
    m.append(int(b))
for i in range(1,len(m)):
    if(m[i] != m[i-1]):
        counter += 1
print(counter)
"""
"""
a = [int(i) for i in input().split()]
num_distinct = 1
for i in range(0, len(a) - 1):
    if a[i] != a[i + 1]:
        num_distinct += 1
print(num_distinct)
"""
#8 Swap neighbours
"""a = input().split()
m=[]
aux = 0
for b in a:
    m.append(int(b))
for i in range(1,len(m),2):
    aux = m[i]
    m[i] = m[i-1]
    m[i-1] = aux
g = ' '.join([str(b) for b in m])
print(g)"""
"""
Model solution
a = [int(i) for i in input().split()]
for i in range(1, len(a), 2):
    a[i - 1], a[i] = a[i], a[i - 1]
print(' '.join([str(i) for i in a]))
"""
#9 Swap min and max
"""a = input().split()
m= []
index1 = 0
index2 = 0
for b in a:
    m.append(int(b))
for pos1 in range(len(m)):
    if(m[pos1] == max(m)):
        index1 = pos1
for pos2 in range(len(m)):
    if(m[pos2] == min(m)):
        index2 = pos2
m[index1], m[index2] = m[index2], m[index1]
print(' '.join([str(b) for b in m]))"""

#10 number of pairs of equal
"""a = input().split()
m= []
counter= 0
for b in a:
    m.append(int(b))
for i in range(0,len(m)):
    for j in range(i+1, len(m)):
        if m[i] - m[j] == 0 or m[j] - m[i] == 0:
            counter+=1
print(counter)"""
"""
a = [int(s) for s in input().split()]
counter = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            counter += 1
print(counter)
"""
#11 unique elements (por resolver)

a = input().split()
m= []
u = []
for b in a:
    m.append(int(b))
n = len(m)
for i in range(0,len(m)):
    for j in range(0,len(m)):
        if m[i] == m[j] and i != j:
            u.append(m[i])
for i in range(0,len(m)):
    if m[i] not in u:
        print(m[i])

"""
Model solution
a = [int(s) for s in input().split()]
for i in range(len(a)):
    for j in range(len(a)):
        if i != j and a[i] == a[j]:
            break
    else:
        print(a[i], end=' ')
"""

#12 Queens
"""m = []
for i in range(8):
    a = input().split()
    m.append(a)
for i in range(len(m)):
    for j in range(len(m[i])):
        m[i][j] = int(m[i][j])
for i in range(len(m)):
    k = 0
    for j in range(len(m[i])):
        if m[i][j] != m[k][j] and i!= k and m[i][j] != m[i][k] and j!=k:
            k +=1
        elif abs(m[k][j]-m[i][j]) != abs(m[i][k]-m[i][j]):
            k += 1
        else:
            k=0
if(k ==0):
    print('YES')
else:
    print('NO')
"""