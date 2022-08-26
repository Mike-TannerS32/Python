#1 length of the segment
import math
def distance(x1,y1,x2,y2):
    d1 = (x2-x1)**2
    d2 = (y2-y1)**2
    d = math.sqrt(d1 + d2)
    return round(d, 5)
#print(distance(float(input()), float(input()),float(input()),float(input())))

#2 Negative exponent
def power(a,n):
    return a**n
#print(power(float(input()),float(input())))

"""
def power(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0:
        return res
    else:
        return 1 / res

print(power(float(input()), int(input())))
"""
#3 Uppercase
def capitalize(lower_case_word):
    return lower_case_word.title()
"print(capitalize(input()))"

"""
def capitalize(word):
    first_letter_small = word[0]
    first_letter_big = chr(ord(first_letter_small) - ord('a') + ord('A'))
    return first_letter_big + word[1:]

source = input().split()
res = []
for word in source:
    res.append(capitalize(word))
print(' '.join(res))
"""
#4 exponentiation
def power(a,n):
    if n ==0:
        return 1
    elif n == 1:
        return a
    else:
        return a * power(a,n-1)
"""print(power(float(input()),int(input())))"""

#5 Reverse sequence
"""
s = ''
string = ''
i = 0
while s != '0':
    s = input()
    string +=s
i = len(string)-1
while i >= 0:
    print(string[i])
    i -= 1
"""

"""
Model solution
def reverse():
    x = int(input())
    if x != 0:
        reverse()
    print(x)

reverse()
"""

#6 Fibonnacci
def fib(n):
    phi = (1+math.sqrt(5))/2
    return round(pow(phi,n)) / math.sqrt(5)
print(fib(int(input())))

"""
Model solution
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(int(input())))
"""