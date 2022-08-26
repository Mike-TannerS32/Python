#1 series 1
A= int(input())
B= int(input())
for i in range(A,B+1):
    print(i)

#2 Series 2
A = int(input())
B = int(input())
if A < B:
    for i in range(A, B+1):
        print(i)
if A >= B:
    for i in range(A, B-1, -1):
        print(i)

#3 Sum of ten numbers
result = 0
for n in range(10):
    a = int(input())
    result += a
print(result)

#4 sum of n numbers
sum = 0
n = int(input())
for i in range(n):
    a = int(input())
    sum += a
print(sum)

#5 sum of cubes
N = int(input())
sum = 0
for i in range(1,N+1):
    sum += i**3
print(sum)

#6 Factorial
n = int(input())
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)

#7 Zeros
c = 0
N = int(input())
for i in range(N):
    a = int(input())
    if(a == 0):
        c += 1
print(c)

"""
Model solution
num_zeroes = 0
for i in range(int(input())):
    if int(input()) == 0:
        num_zeroes += 1
print(num_zeroes)
"""

#8 Factorial Sum
sum = 0
N = int(input())
for i in range(1, N+1):
    a=1
    for i in range(1, i+1):
        a = i*a
    sum = sum+a
print(sum)
"""
Model solution
n = int(input())
partial_factorial = 1
partial_sum = 0
for i in range(1, n + 1):
    partial_factorial *= i
    partial_sum += partial_factorial
print(partial_sum)
"""

#9 ladder
n = int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end='')
    print('')

#10 Lost card
"""
There was a set of cards with numbers from 1 to N. 
One of the card is now lost. Determine the number 
on that lost card given the numbers for the 
remaining cards.

Given a number N, followed by N − 1 integers - 
representing the numbers on the remaining cards 
(distinct integers in the range from 1 to N). 
Find and print the number on the lost card. 
"""
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