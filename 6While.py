#1 List of squares
"""N = int(input())
e = 1
while e**2 <= N:
    print(e**2)
    e = e+1"""

#2 Least divisor
"""
N = int(input())
e = N
d = []
while e > 1:
    if N % e == 0:
        d.append(e)
    e = e -1
print(d[-1])"""

"""
Model
n = int(input())
i = 2
while n % i != 0:
    i += 1
print(i)
"""

#3 The power of two
N = int(input())
x = 1
while 2**x <= N:
    x += 1
if(2**x> N):
    x -= 1
print(x , 2**x)

"""
Model
n = int(input())
two_in_power = 2
power = 1
while two_in_power <= n:
    two_in_power *= 2
    power += 1
print(power - 1, two_in_power // 2)
"""

#4 Morning jog
x = int(input())
y = int(input())
e = x
days = 1
while e <= y:
    if(e==y):
        break
    e = e + 0.1*e
    days += 1
print(days)

"""
Model
x = int(input())
y = int(input())
i = 1
while x < y:
    x *= 1.1
    i += 1
print(i)
"""

#5 Lenght of the sequence
c = 0
e = 1
while e != 0:
    n = int(input())
    e = n
    c += 1
    if e == 0:
        c -= 1
print(c)

"""
Model Solutions
len = 0
while int(input()) != 0:
    len += 1
print(len)
"""

#6 sum of the sequence
total = 0
s = 1
while s !=0:
    s = int(input())
    total += s
print(total)

#7 average of elements of sequence
total_sum = 0
total = 0
i = 0
s = int(input())
while s!= 0:
    total_sum += s
    i += 1
    s = int(input())
total = total_sum/i
print(total)

#8 The maximum of the sequence
i = 0
s = 1
while s !=0:
    s = int(input())
    if(s > i):
        i = s
print(i)

#9 The index of the maximum number
i = 0
s = -1
a = []
while s!=0:
    s = int(input())
    a.append(s)
maximum = max(a)
print(a.index(maximum)+1)
"""
Model solution
max = 0
index_of_max = -1
element = -1
len = 1
while element != 0:
    element = int(input())
    if element > max:
        max = element
        index_of_max = len
    len += 1
print(index_of_max)
"""

#10  number of even elements of sequence
n = -1
i = 0
while n!=0:
    n = int(input())
    if n%2 ==0:
        i = i + 1
    if n ==0:
        i -=1
print(i) 

"""
Model solution
num_even = -1
element = -1
while element != 0:
    element = int(input())
    if element % 2 == 0:
        num_even += 1
print(num_even)
"""

#11 number of elements greater than previous one
n = -1
i = -1
previous=0
while n!=0:
    n = int(input())
    if(n > previous):
        i +=1
    previous = n
print(i)

"""
Model solution
prev = int(input())
answer = 0
while prev != 0:
    next = int(input())
    if next != 0 and prev < next:
        answer += 1
    prev = next
print(answer)
"""

#12 The second maximum
i = 0
s = 1
d = []
while s !=0:
    s = int(input())
    if(s > i):
        d.append(s)
d.sort()
print(d[-2])

"""
Model solution
first_max = int(input())
second_max = int(input())
if first_max < second_max:
    first_max, second_max = second_max, first_max
element = int(input())
while element != 0:
    if element > first_max:
        second_max, first_max = first_max, element
    elif element > second_max:
        second_max = element
    element = int(input())
print(second_max)
"""

#13 Nº of elements equal to the maximum
n = -1
i=0
d = []
d_max = []
c = 0
while n != 0:
    n = int(input())
    d.append(n)
d.sort()
max_v = max(d)
while i < len(d):
    if(d[i] == max_v):
        c += 1
    i +=1
print(c)

"""
Model Solution
maximum = 0
num_maximal = 0
element = -1
while element != 0:
    element = int(input())
    if element > maximum:
        maximum, num_maximal = element, 1
    elif element == maximum:
        num_maximal += 1        
print(num_maximal)

"""

#14 find nth fibonacci num
num = int(input())
f = [0,1,1,2,3,5]
fib = 0
if num<6:
    fib = f[num]
else:
    t = 5
    fib = 5  
    while t< num:
        fib = round(fib*1.6180339)
        t += 1
print(fib)

"""
Model
n = int(input())
if n == 0:
    print(0)
else:
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    print(b)
"""

#15 index of a FIbonnaci number (por resolver)

n = int(input())
d= [0,1]
c = -1
if n == 0:
    print(0)
else:
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
        d.append(b)
for i in range(len(d)):
    if(n == d[i]):
        print(i)
        c += 1
    else:
        print(c)
"""
import math
n = int(input())
print(round(math.log(n*math.sqrt(5)+0.5)/math.log(1.61803398875)-1)+1)
"""
#16 maximum number of consecutive equal elements (por resolver)
n = -1
d = []
counter = 1
i = 0
while n != 0:
    n = int(input())
    d.append(n)
prev = 0
next = 0
while i< len(d)-1:
    prev = d[i]
    next = d[i+1]
    if(prev == next):
        counter += 1
    i += 1
print(counter)