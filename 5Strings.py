#1 String
"""
You are given a string.

In the first line, print the third character of this string.

In the second line, print the second to last character of this string.

In the third line, print the first five characters of this string.

In the fourth line, print all but the last two characters of this string.

In the fifth line, print all the characters of this string with even indices (remember indexing starts at 0, so the characters are displayed starting with the first).

In the sixth line, print all the characters of this string with odd indices (i.e. starting with the second character in the string).

In the seventh line, print all the characters of the string in reverse order.

In the eighth line, print every second character of the string in reverse order, starting from the last one.

In the ninth line, print the length of the given string. 
"""
"""
string = "Abrakadabra"
print(string[2])
print(string[-2])
print(string[:5])
print(string[:-2])
print(string[0::2])
print(string[1::2])
print(string[::-1])
print(string[::-2])
print(len(string))
"""
#2
"""
s = input()
s1 = s.split(" ")
print(len(s1))
"""
"""
Model solution
print(input().count(' ') + 1)
"""

#3 two halves
"""
s = input()
count = len(s)//2
s1 = s[:count]
s2 = s[count:]
if len(s2) > len(s1):
    s1 = s[:count+1]
    s2 = s[count+1:]
print(s2+s1)
"""
"""
Model solution
s = input()
print(s[(len(s) + 1) // 2:] + s[:(len(s) + 1) // 2])
"""
"""
#4 Swap two words
s = input()
s1 = s[:s.find(' ')]
s2 = s[s.find(' ') + 1:]
print(s1+ ' ' + s2)

#5 first and last location of char
s=input()
s1=s.count("f")
if(s1==1):
    print(s.find("f"))
elif s1>=2:
    print(s.find("f"), s.rfind("f"))
"""
#6 second ocurrence of char
"""s=input()
s1 = s.count("f")
if s1==1:
    print(-1)
elif s1==0:
    print(-2)
else:
    i = s.index("f")
    print(s.index("f", i+1))"""

"""
Model Solution
s = input()
if s.count('f') == 1:
    print(-1)
elif s.count('f') < 1:
    print(-2)
else:
    print(s.find('f', s.find('f') + 1))
"""

#7 Remove fragment
"""s = input()
s1=s[:s.find("h")]
s2=s[s.rfind("h")+1:]
print(s1,s2)"""
"""
#8 Reverse fragment
s = input()
s1 = s[s.rfind("h")+1:]
s2 = s[:s.find("h")]
s3= s[s.find("h"):s.rfind("h")+1]
s4 = s3[::-1]
print(s2 + s4 + s1)

#9 Replace substring
s= input()
print(s.replace('1', "one"))

#10 Delete char
s = input()
print(s.replace('@',''))"""
"""
Model
print(input().replace('@', ''))
"""

#11 Replace within fragment
"""s = input()
s1= s[:s.find("h")+1]
s2= s[s.rfind("h"):]
s3= s[s.find("h")+1:s.rfind("h")]
s4 = s3.replace("h","H") 
print(s1+s4+s2)"""

#12 Replace every third character
s = input()
p= ""
for i in range(0,len(s)):
    if(i%3!=0):
        p += s[i]
print(p)
