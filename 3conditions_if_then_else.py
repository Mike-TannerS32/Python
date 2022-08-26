#1
"""Given two integers, print the smaller value."""
a = int(input())
b = int(input())
if a < b:
    print(a)
else:
    print(b)

#2
"""For the given integer X print 1 if it's positive, -1 if it's negative, or 0 if it's equal to zero.

Try to use the cascade if-elif-else for it. 
"""
X = int(input())
if(X > 0):
    print(1)
elif(X<0):
    print(-1)
else:
    print(0)

#3
"""Given three integers, print the smallest value."""
I1= int(input())
I2= int(input())
I3= int(input())
if I1 < I2 and I1 < I3:
    print(I1)
elif I2< I1 and I2<I3:
    print(I2)
elif I3<I1 and I3<I2:
    print(I3)

#4
"""Given three integers, determine how many of them are equal to each other.
The program must print one of these numbers: 
3 (if all are the same), 2 (if two of them are equal to each other 
and the third is different) or 0 (if all numbers are different)."""
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print(3)
elif a==b and a!=c or b==c and a!=c or a==c and a!=b:
    print(2)
else:
    print(0)

"""soluçao modelo
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)
"""

#5
"""
Chess rook moves horizontally or vertically. 
Given two different cells of the chessboard, 
determine whether a rook can go from the first cell to the second 
in one move.

The program receives the input of four numbers from 1 to 8, 
each specifying the column and row number, first two - for the first cell,
and then the last two - for the second cell. 
The program should output YES if a rook can go from the first cell to the 
second in one move, or NO otherwise. 
"""
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x2!=x1 and y2!=y1:
    print("NO")
else:
    print("YES")

#6
"""
Given two cells of a chessboard. If they are painted in one color, 
print the word YES, and if in a different color - NO.

The program receives the input of four numbers from 1 to 8, 
each specifying the column and row number, 
first two - for the first cell, 
and then the last two - for the second cell. 
"""
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
r1= (x1+y1)%2
r2= (x2+b2)%2
if r1==r2:
    print("YES")
else:
    print("NO")
#se a soma das coordenadas for um num par, 
#então elas são iguais, senão não são

#7
""" 
Chess king moves horizontally, vertically or diagonally 
to any adjacent cell. Given two different cells of the 
chessboard, determine whether a king can go from the 
first cell to the second in one move.

The program receives the input of four numbers from 1 to 8
, each specifying the column and row number, first two - 
for the first cell, and then the last two - for the 
second cell. The program should output YES if a king 
can go from the first cell to the second in one move, 
or NO otherwise
"""
col = int(input())
row = int(input())
colNew = int(input())
rowNew = int(input())

if (col == colNew + 1 or col == colNew - 1 or col == colNew) 
and (row == rowNew + 1 or row == rowNew - 1 or row == rowNew):
    print ("YES")
else:
    print ("NO")

#8
"""
In chess, the bishop moves diagonally, 
any number of squares. Given two different squares 
of the chessboard, determine whether a bishop can go 
from the first to the second in one move. 
"""
r1 = int(input())
c1 = int(input())
r2 = int(input())
c2 = int(input())
dx = abs(r2-r1)
dy = abs(c2-c1)
if(dx == dy) and dx>0:
    print("YES")
else:
    print("NO")

#9 Queen move
"""
Chess queen moves horizontally, 
vertically or diagonally to any number of cells. 
Given two different cells of the chessboard, 
determine whether a queen can go from the first cell to the 
second in one move. 
 """
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1-x2)==abs(y1-y2) or x1==x2 or y1==y2:
    print("YES")
else:
    print("NO")

#10 Knight move
"""  
Chess knight moves like the letter L. It can move two cells 
horizontally and one cell vertically, or two cells vertically and 
one cells horizontally. Given two different cells of the chessboard, 
determine whether a knight can go from the first cell to the second 
in one move. 
"""
m1 = int(input())
n1 = int(input())
m2 = int(input())
n2 = int(input())
if (m2 == m1+1 or m2 == m1-1) and (n2== n1-2 or n2 == n1+2):
    print("YES")
elif (n2 == n1-1 or n2 == n1+1) and (m2 == m1-2 or m2== m1+2):
    print("YES") 
else:
    print("NO")

#11
"""
Chocolate bar has the form of a rectangle divided into n×m portions. Chocolate bar can be split into two rectangular parts by breaking it along a selected straight line on its pattern. Determine whether it is possible to split it so that one of the parts will have exactly k squares.  
"""
n= int(input())
m= int(input())
k= int(input())
if (k % n == 0 and k/n < m) or (k%m==0 and k/m <n):
    print("YES")
else:
    print("NO")

#12 Leap Year
year = int(input())
if (year %4 == 0 and year %100 != 0):
    print("LEAP")
elif year % 400==0:
    print("LEAP")
else:
    print("COMMON")