#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python Program to Find LCM?
# 2. Write a Python Program to Find HCF?
# 3. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?
# 4. Write a Python Program To Find ASCII value of a character?
# 5. Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?

# In[6]:


a = 6
b = 15
num = 1
for i in range(1,max(a,b)):
    if a % i == 0 and b % i == 0:
        num = i
print((a*b)/num)


# In[10]:


a = 12
b = 18
num = 1
for i in range(1,max(a,b)):
    if a % i == 0 and b % i == 0:
        num = i
lcm = (a*b)/num
hcf = (a*b)/lcm
print(hcf)


# In[85]:


num = 910
a=num 
m = str()
n = str()
o = str()
while a > 0:
    x = int(a / 2)
    y = int(a % 2)
    m=m+str(y)
    a = x
print(f"Binary of {num} is: {m[::-1]}")

a=num 
while a > 0:
    x = int(a / 8)
    y = int(a % 8)
    n=n+str(y)
    a = x
print(f"Octal of {num} is: {n[::-1]}")

a=num 
while a > 0:
    x = int(a / 16)
    y = int(a % 16)
    if y > 9:
        y = 55 + y
        y = chr(y)
    o=o+str(y)
    a = x
print(f"Hexadecimal of {num} is: {o[::-1]}")


# In[67]:


a = 'A'
ord(a)


# In[7]:


a = 10
b = 5
print(f"""Addition of {a} and {b} is: {a+b}\n
Subtraction of {a} and {b} is: {a-b}\n
Multiplication of {a} and {b} is: {a*b}\n
Division of {a} and {b} is: {a/b}""")

