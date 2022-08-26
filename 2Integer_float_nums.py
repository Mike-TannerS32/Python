import math

#last digit of integer
"""
number = int(input())
n = str(number)
print(n[1])
"""
#tens digit
"""
num = 15
pos_num= []
while num !=0 :
    pos_num.append(num%10)
    num = num //10
print(pos_num[1])
"""

#sum of digits
"""
num = 123
alg= []
while num!=0:
    alg.append(num%10)
    num = num//10
print(alg[0]+alg[1]+alg[2])
"""
#fractional part
num = 12.4
frac = num%1
#print(round(frac, 1))

#first digit after decimal point
"""
dec = "1.73"
res = dec.index('.')
val = dec[res+1]
print(val)
"""
"""
#car route
N = int(input())
M = int(input())
i = 0
while M>0:
    M = M - N
    i = i + 1
print(i)

"""

"""
#digital clock
N = 150
min = 0
h = 0
if(N <60):
    min += N
    N = N - min
elif( 60< N< 120):
    h += 1
    min = N - 60 
else:
    h += 2
    min = N - 120
print(h,min)
"""

#total cost
A = "2"
B = "3"
N = 5
price =float(A+B)/ 10
cost = price * N
#print(cost)

#clock face - 1
hour = int(input())
min = int(input())
sec = int(input())
angle = (hour+(min/60) + (sec/3600))*30
print(angle)

#clock face 2
M = float(input())
M = M%30
print(M*12)
